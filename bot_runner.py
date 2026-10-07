from __future__ import annotations

import json
import logging
import math
import os
import tempfile
from dataclasses import dataclass
from datetime import datetime, timedelta, time
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd

try:
    from alpaca.data.enums import DataFeed
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.historical.news import NewsClient
    from alpaca.data.requests import (
        NewsRequest,
        StockBarsRequest,
        StockLatestQuoteRequest,
        StockLatestTradeRequest,
    )
    from alpaca.data.timeframe import TimeFrame
    from alpaca.trading.client import TradingClient
except ImportError:  # Allows pure strategy unit tests without the SDK installed.
    DataFeed = None
    StockHistoricalDataClient = None
    NewsClient = None
    NewsRequest = None
    StockBarsRequest = None
    StockLatestQuoteRequest = None
    StockLatestTradeRequest = None
    TimeFrame = None
    TradingClient = None

NY = ZoneInfo("America/New_York")
WATCHLIST = ["AAPL", "NVDA", "AMD", "MSFT"]
STATE_PATH = Path("bot_state.json")
REPORT_PATH = Path("reports/latest.md")
SLIPPAGE_BPS = 5.0
MAX_POSITIONS = 3

# Portfolio-level risk controls. These apply independently to every virtual bot.
HARD_FLOOR_PCT = 0.80          # Permanently stop at 80% of starting equity (-20%).
MAX_PEAK_DRAWDOWN_PCT = 0.15  # Permanently stop after a 15% drawdown from peak equity.
DAILY_PAUSE_LOSS_PCT = 0.05   # Pause NEW entries for the rest of the day after a 5% daily equity loss.

POS_WORDS = {
    "beat", "beats", "growth", "strong", "record", "upgrade", "upgraded",
    "partnership", "deal", "approval", "launch", "demand", "contract",
    "profit", "wins", "raise", "raised", "outperform", "guidance raised",
}
NEG_WORDS = {
    "miss", "misses", "weak", "cut", "cuts", "downgrade", "downgraded",
    "lawsuit", "probe", "ban", "delay", "recall", "investigation",
    "restriction", "decline", "loss", "risk", "warning", "guidance cut",
}

# New entries scale with CURRENT equity so winners can compound while losing bots
# naturally shrink their position sizes. There is intentionally no profit ceiling.
BOT_CONFIG = {
    "BOT_A": {"strategy": "Trend / Breakout", "position_fraction": 0.25},
    "BOT_B": {"strategy": "Dip / Mean Reversion", "position_fraction": 0.25},
    "BOT_C": {"strategy": "News + Momentum", "position_fraction": 0.25},
    "BOT_D": {"strategy": "Conservative Confirmation", "position_fraction": 0.20},
}


@dataclass(frozen=True)
class Signal:
    price: float
    sma20: float
    sma50: float
    rsi14: float
    ret5_pct: float
    prior20_high: float
    zscore20: float
    news_score: int
    news_headlines: tuple[str, ...]


def utc_iso() -> str:
    return datetime.now(tz=ZoneInfo("UTC")).isoformat()


def _f(value: Any, default: float = 0.0) -> float:
    try:
        out = float(value)
        return out if math.isfinite(out) else default
    except (TypeError, ValueError):
        return default


def atomic_json_write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", delete=False, dir=path.parent, encoding="utf-8") as tmp:
        json.dump(data, tmp, indent=2, ensure_ascii=False, sort_keys=True)
        tmp.write("\n")
        temp_name = tmp.name
    os.replace(temp_name, path)


def load_state(path: Path = STATE_PATH) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        state = json.load(fh)

    # Schema v2 adds portfolio risk state while remaining backward compatible
    # with the state imported from Colab/schema v1.
    state["schema_version"] = max(2, int(state.get("schema_version", 1)))
    state.setdefault("trades", [])
    state.setdefault("last_run", None)

    for name, cfg in BOT_CONFIG.items():
        bot = state.setdefault("bots", {}).setdefault(name, {})
        bot.setdefault("strategy", cfg["strategy"])
        bot.setdefault("starting_cash", 10000.0)
        bot.setdefault("cash", 10000.0)
        bot.setdefault("realized_pl", 0.0)
        bot.setdefault("positions", {})
        bot.setdefault("trade_count", 0)
        bot.setdefault("last_exit_date", {})

        # Portfolio-level risk bookkeeping.
        start = _f(bot.get("starting_cash"), 10000.0)
        bot.setdefault("status", "ACTIVE")
        bot.setdefault("peak_equity", start)
        bot.setdefault("last_equity", start)
        bot.setdefault("risk_date", None)
        bot.setdefault("day_start_equity", start)
        bot.setdefault("entry_paused_date", None)
        bot.setdefault("stop_reason", None)
        bot.setdefault("stopped_at", None)

    return state


def rsi14(closes: pd.Series) -> float:
    if len(closes) < 15:
        return float("nan")
    delta = closes.diff()
    gains = delta.clip(lower=0).rolling(14).mean()
    losses = (-delta.clip(upper=0)).rolling(14).mean()
    loss = losses.iloc[-1]
    gain = gains.iloc[-1]
    if pd.isna(loss) or pd.isna(gain):
        return float("nan")
    if loss == 0:
        return 100.0 if gain > 0 else 50.0
    rs = gain / loss
    return float(100 - (100 / (1 + rs)))


def calculate_signal(
    df: pd.DataFrame,
    current_price: float,
    news_score: int = 0,
    headlines: tuple[str, ...] = (),
) -> Signal:
    if len(df) < 55:
        raise ValueError("Need at least 55 completed daily bars")
    closes = df["close"].astype(float)
    highs = df["high"].astype(float)
    sma20 = float(closes.tail(20).mean())
    sma50 = float(closes.tail(50).mean())
    std20 = float(closes.tail(20).std(ddof=0))
    z = 0.0 if std20 == 0 else (current_price - sma20) / std20
    ret5 = (current_price / float(closes.iloc[-5]) - 1.0) * 100.0
    return Signal(
        price=float(current_price),
        sma20=sma20,
        sma50=sma50,
        rsi14=rsi14(closes),
        ret5_pct=ret5,
        prior20_high=float(highs.tail(20).max()),
        zscore20=float(z),
        news_score=int(news_score),
        news_headlines=headlines,
    )


def should_enter(bot: str, s: Signal) -> bool:
    if bot == "BOT_A":
        return s.price > s.prior20_high and s.sma20 > s.sma50 and s.ret5_pct > 0
    if bot == "BOT_B":
        return s.rsi14 < 35 and s.zscore20 < -1.2
    if bot == "BOT_C":
        return s.news_score > 0 and s.ret5_pct > 1 and s.price > s.sma20
    if bot == "BOT_D":
        return (
            s.price > s.sma20 > s.sma50
            and 50 <= s.rsi14 <= 65
            and 0 < s.ret5_pct < 5
            and s.news_score >= 0
        )
    raise KeyError(bot)


def should_exit(bot: str, s: Signal, position_pl_pct: float) -> tuple[bool, str]:
    reasons: list[str] = []
    if bot == "BOT_A":
        if s.price < s.sma20:
            reasons.append("price<SMA20")
        if position_pl_pct <= -6:
            reasons.append("stop -6%")
        if position_pl_pct >= 12:
            reasons.append("take +12%")
    elif bot == "BOT_B":
        if s.price >= s.sma20:
            reasons.append("mean reversion to SMA20")
        if position_pl_pct <= -7:
            reasons.append("stop -7%")
        if position_pl_pct >= 8:
            reasons.append("take +8%")
    elif bot == "BOT_C":
        if s.news_score < 0:
            reasons.append("negative news")
        if s.price < s.sma20:
            reasons.append("price<SMA20")
        if position_pl_pct <= -6:
            reasons.append("stop -6%")
        if position_pl_pct >= 10:
            reasons.append("take +10%")
    elif bot == "BOT_D":
        if s.price < s.sma20:
            reasons.append("price<SMA20")
        if s.rsi14 > 75:
            reasons.append("RSI>75")
        if position_pl_pct <= -4:
            reasons.append("stop -4%")
        if position_pl_pct >= 8:
            reasons.append("take +8%")
    else:
        raise KeyError(bot)
    return bool(reasons), ", ".join(reasons)


def can_open_position(bot_state: dict[str, Any], symbol: str, today: str) -> bool:
    if bot_state.get("status", "ACTIVE") != "ACTIVE":
        return False
    if bot_state.get("entry_paused_date") == today:
        return False
    if symbol in bot_state["positions"]:
        return False
    if len(bot_state["positions"]) >= MAX_POSITIONS:
        return False
    if bot_state.get("last_exit_date", {}).get(symbol) == today:
        return False
    return True


def simulated_fill(mid_price: float, side: str, slippage_bps: float = SLIPPAGE_BPS) -> float:
    slip = slippage_bps / 10000.0
    return mid_price * (1 + slip if side == "BUY" else 1 - slip)


def fetch_prices(stock: StockHistoricalDataClient) -> dict[str, float]:
    prices: dict[str, float] = {}
    quotes = stock.get_stock_latest_quote(
        StockLatestQuoteRequest(symbol_or_symbols=WATCHLIST, feed=DataFeed.IEX)
    )
    for symbol in WATCHLIST:
        q = quotes.get(symbol)
        if q is not None:
            bid, ask = _f(getattr(q, "bid_price", 0)), _f(getattr(q, "ask_price", 0))
            if bid > 0 and ask > 0 and ask >= bid:
                prices[symbol] = (bid + ask) / 2.0
    missing = [s for s in WATCHLIST if s not in prices]
    if missing:
        trades = stock.get_stock_latest_trade(
            StockLatestTradeRequest(symbol_or_symbols=missing, feed=DataFeed.IEX)
        )
        for symbol in missing:
            t = trades.get(symbol)
            price = _f(getattr(t, "price", 0)) if t is not None else 0
            if price > 0:
                prices[symbol] = price
    return prices


def fetch_completed_bars(stock: StockHistoricalDataClient, now_et: datetime) -> dict[str, pd.DataFrame]:
    start = now_et - timedelta(days=220)
    end = now_et.replace(hour=0, minute=0, second=0, microsecond=0)
    req = StockBarsRequest(
        symbol_or_symbols=WATCHLIST,
        timeframe=TimeFrame.Day,
        start=start,
        end=end,
        feed=DataFeed.IEX,
        limit=10000,
    )
    bars = stock.get_stock_bars(req).df
    out: dict[str, pd.DataFrame] = {}
    for symbol in WATCHLIST:
        try:
            if isinstance(bars.index, pd.MultiIndex):
                sdf = bars.xs(symbol, level="symbol").sort_index()
            else:
                sdf = bars.sort_index()
            out[symbol] = sdf
        except (KeyError, ValueError):
            logging.warning("No completed bars for %s", symbol)
    return out


def _news_items(payload: Any) -> list[Any]:
    if payload is None:
        return []
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        return list(payload.get("news", payload.get("data", [])) or [])
    data = getattr(payload, "data", None)
    if isinstance(data, dict):
        return list(data.get("news", []) or [])
    if isinstance(data, list):
        return data
    news = getattr(payload, "news", None)
    return list(news or [])


def score_news(news_client: NewsClient, symbol: str, now_et: datetime) -> tuple[int, tuple[str, ...]]:
    try:
        req = NewsRequest(
            symbols=symbol,
            start=now_et - timedelta(days=3),
            end=now_et,
            limit=30,
        )
        raw = _news_items(news_client.get_news(req))
    except Exception as exc:  # keep a symbol-specific news error from killing the run
        logging.warning("News fetch failed for %s: %s", symbol, exc)
        return 0, ()

    seen: set[str] = set()
    headlines: list[str] = []
    total = 0
    for item in raw:
        headline = str(
            getattr(item, "headline", "")
            or (item.get("headline", "") if isinstance(item, dict) else "")
        ).strip()
        summary = str(
            getattr(item, "summary", "")
            or (item.get("summary", "") if isinstance(item, dict) else "")
        ).strip()
        key = headline.lower()
        if not headline or key in seen:
            continue
        seen.add(key)
        text = f"{headline} {summary}".lower()
        pos = sum(1 for w in POS_WORDS if w in text)
        neg = sum(1 for w in NEG_WORDS if w in text)
        # Conservative: only count a headline when one side clearly dominates.
        if pos >= 1 and neg == 0:
            total += 1
        elif neg >= 1 and pos == 0:
            total -= 1
        headlines.append(headline)
        if len(headlines) >= 5:
            break
    return max(-3, min(3, total)), tuple(headlines)


def append_trade(
    state: dict[str, Any],
    bot: str,
    action: str,
    symbol: str,
    qty: float,
    fill: float,
    notional: float,
    realized_pl: float,
    reason: str,
    now_et: datetime,
) -> None:
    state["trades"].append(
        {
            "timestamp": now_et.isoformat(),
            "bot": bot,
            "action": action,
            "symbol": symbol,
            "qty": round(qty, 10),
            "fill_price": round(fill, 6),
            "notional": round(notional, 2),
            "realized_pl": round(realized_pl, 2),
            "reason": reason,
        }
    )
    if len(state["trades"]) > 2000:
        state["trades"] = state["trades"][-2000:]


def mark_bot(bot_state: dict[str, Any], prices: dict[str, float]) -> dict[str, float]:
    market_value = 0.0
    unrealized = 0.0
    for symbol, pos in bot_state["positions"].items():
        price = prices.get(symbol, _f(pos.get("avg_price")))
        qty = _f(pos.get("qty"))
        avg = _f(pos.get("avg_price"))
        market_value += qty * price
        unrealized += qty * (price - avg)
    equity = _f(bot_state.get("cash")) + market_value
    return {
        "market_value": market_value,
        "unrealized_pl": unrealized,
        "equity": equity,
        "return_pct": (equity / _f(bot_state.get("starting_cash"), 10000.0) - 1) * 100,
    }


def refresh_daily_risk(bot: dict[str, Any], equity: float, today: str) -> None:
    """Roll the daily baseline and clear an old one-day entry pause."""
    if bot.get("risk_date") != today:
        previous_equity = _f(bot.get("last_equity"), equity)
        bot["risk_date"] = today
        bot["day_start_equity"] = previous_equity if previous_equity > 0 else equity
        if bot.get("entry_paused_date") != today:
            bot["entry_paused_date"] = None


def portfolio_stop_reason(bot: dict[str, Any], equity: float) -> str | None:
    """Return a permanent-stop reason, or None when portfolio risk remains valid."""
    start = _f(bot.get("starting_cash"), 10000.0)
    peak = max(_f(bot.get("peak_equity"), start), equity)
    bot["peak_equity"] = peak

    if equity <= start * HARD_FLOOR_PCT:
        return f"hard floor: equity <= {HARD_FLOOR_PCT:.0%} of starting equity"
    if peak > 0 and equity <= peak * (1 - MAX_PEAK_DRAWDOWN_PCT):
        return f"peak drawdown >= {MAX_PEAK_DRAWDOWN_PCT:.0%}"
    return None


def update_daily_pause(bot: dict[str, Any], equity: float, today: str) -> bool:
    """Pause only NEW entries for the current day after a large daily loss."""
    start = _f(bot.get("day_start_equity"), equity)
    if start > 0 and equity <= start * (1 - DAILY_PAUSE_LOSS_PCT):
        bot["entry_paused_date"] = today
        return True
    return bot.get("entry_paused_date") == today


def liquidate_virtual_bot(
    state: dict[str, Any],
    bot_name: str,
    bot: dict[str, Any],
    prices: dict[str, float],
    reason: str,
    now_et: datetime,
    actions: list[str],
) -> None:
    """Close every virtual position and permanently stop one bot. No broker order is sent."""
    today = now_et.date().isoformat()
    for symbol in list(bot["positions"].keys()):
        pos = bot["positions"][symbol]
        current = prices.get(symbol)
        if current is None or current <= 0:
            # Fail safe: do not invent a price. Leave the position and retry next run.
            logging.warning("Cannot risk-liquidate %s %s: no valid price", bot_name, symbol)
            continue
        qty = _f(pos.get("qty"))
        avg = _f(pos.get("avg_price"))
        fill = simulated_fill(current, "SELL")
        proceeds = qty * fill
        realized = qty * (fill - avg)
        bot["cash"] = round(_f(bot.get("cash")) + proceeds, 8)
        bot["realized_pl"] = round(_f(bot.get("realized_pl")) + realized, 8)
        bot["trade_count"] = int(bot.get("trade_count", 0)) + 1
        bot.setdefault("last_exit_date", {})[symbol] = today
        del bot["positions"][symbol]
        append_trade(
            state,
            bot_name,
            "SELL",
            symbol,
            qty,
            fill,
            proceeds,
            realized,
            f"portfolio stop — {reason}",
            now_et,
        )
        actions.append(f"{bot_name} SELL {symbol} @ {fill:.2f} — portfolio stop: {reason}")

    # Mark STOPPED only when every virtual position has been safely closed.
    if not bot["positions"]:
        bot["status"] = "STOPPED"
        bot["stop_reason"] = reason
        bot["stopped_at"] = now_et.isoformat()
        bot["entry_paused_date"] = today
        actions.append(f"{bot_name} STOPPED — {reason}")


def write_report(
    state: dict[str, Any],
    prices: dict[str, float],
    signals: dict[str, Signal],
    actions: list[str],
    now_et: datetime,
) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for bot_name, bot in state["bots"].items():
        m = mark_bot(bot, prices)
        rows.append((m["equity"], bot_name, bot, m))
    rows.sort(reverse=True)

    lines = [
        "# Paper Bot Lab — Latest Report",
        "",
        f"Updated: {now_et.isoformat()}",
        "",
        "> Simulation only. No Alpaca brokerage orders are submitted.",
        "",
        "## Leaderboard",
        "",
        "| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |",
        "|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for i, (_, bot_name, bot, m) in enumerate(rows, 1):
        positions = ", ".join(sorted(bot["positions"].keys())) or "—"
        status = bot.get("status", "ACTIVE")
        if bot.get("entry_paused_date") == now_et.date().isoformat() and status == "ACTIVE":
            status = "PAUSED-ENTRIES"
        lines.append(
            f"| {i} | {bot_name} | {status} | {bot['strategy']} | ${m['equity']:,.2f} | "
            f"{m['return_pct']:.2f}% | ${_f(bot['cash']):,.2f} | ${_f(bot.get('peak_equity')):,.2f} | "
            f"${_f(bot['realized_pl']):,.2f} | ${m['unrealized_pl']:,.2f} | {positions} |"
        )

    lines += [
        "",
        "## Portfolio risk rules",
        "",
        f"- Permanent stop at {HARD_FLOOR_PCT:.0%} of starting equity (20% total loss).",
        f"- Permanent stop after a {MAX_PEAK_DRAWDOWN_PCT:.0%} drawdown from the bot's peak equity.",
        f"- Pause new entries for the rest of the trading day after a {DAILY_PAUSE_LOSS_PCT:.0%} daily equity loss.",
        "- No profit ceiling: active bots may continue compounding.",
        "- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.",
        "",
        "## Current signals",
        "",
        "| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for symbol in WATCHLIST:
        s = signals.get(symbol)
        if not s:
            lines.append(f"| {symbol} | data unavailable | | | | | | | |")
            continue
        lines.append(
            f"| {symbol} | ${s.price:.2f} | ${s.sma20:.2f} | ${s.sma50:.2f} | {s.rsi14:.1f} | "
            f"{s.ret5_pct:.2f}% | ${s.prior20_high:.2f} | {s.zscore20:.2f} | {s.news_score:+d} |"
        )

    lines += ["", "## Actions this run", ""]
    lines += [f"- {x}" for x in actions] if actions else ["- No virtual trades this run."]
    lines += [
        "",
        "## Notes",
        "",
        "- Prices use IEX market data when available.",
        "- Entries include 5 bps simulated slippage; exits also include 5 bps.",
        "- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.",
        "- Portfolio stops are virtual risk controls only; this program does not submit broker orders.",
        "",
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def run() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    if TradingClient is None:
        raise RuntimeError("alpaca-py is not installed")

    key = os.getenv("ALPACA_API_KEY", "").strip()
    secret = os.getenv("ALPACA_SECRET_KEY", "").strip()
    if not key or not secret:
        raise RuntimeError("Missing ALPACA_API_KEY or ALPACA_SECRET_KEY")

    # TradingClient is used ONLY for the market clock. This project never sends an order.
    trading = TradingClient(key, secret, paper=True)
    clock = trading.get_clock()
    if not bool(clock.is_open):
        logging.info("US regular market is closed. State is unchanged.")
        return 0

    now_et = datetime.now(tz=NY)
    state = load_state()
    stock = StockHistoricalDataClient(key, secret)
    news = NewsClient(key, secret)

    prices = fetch_prices(stock)
    bars_by_symbol = fetch_completed_bars(stock, now_et)
    signals: dict[str, Signal] = {}
    for symbol in WATCHLIST:
        if symbol not in prices or symbol not in bars_by_symbol:
            logging.warning("Skipping %s due to missing price/bars", symbol)
            continue
        try:
            score, headlines = score_news(news, symbol, now_et)
            signals[symbol] = calculate_signal(
                bars_by_symbol[symbol], prices[symbol], score, headlines
            )
        except Exception as exc:
            logging.warning("Signal calculation failed for %s: %s", symbol, exc)

    actions: list[str] = []
    today = now_et.date().isoformat()

    # 1) Strategy/position risk exits first. Permanently stopped bots should normally
    # have no positions; if a prior run could not price one, portfolio liquidation below retries it.
    for bot_name, bot in state["bots"].items():
        if bot.get("status", "ACTIVE") != "ACTIVE":
            continue
        for symbol in list(bot["positions"].keys()):
            s = signals.get(symbol)
            if not s:
                continue
            pos = bot["positions"][symbol]
            avg = _f(pos["avg_price"])
            qty = _f(pos["qty"])
            pl_pct = (s.price / avg - 1.0) * 100 if avg > 0 else 0.0
            exit_now, reason = should_exit(bot_name, s, pl_pct)
            if not exit_now:
                continue
            fill = simulated_fill(s.price, "SELL")
            proceeds = qty * fill
            realized = qty * (fill - avg)
            bot["cash"] = round(_f(bot["cash"]) + proceeds, 8)
            bot["realized_pl"] = round(_f(bot["realized_pl"]) + realized, 8)
            bot["trade_count"] = int(bot.get("trade_count", 0)) + 1
            bot.setdefault("last_exit_date", {})[symbol] = today
            del bot["positions"][symbol]
            append_trade(
                state, bot_name, "SELL", symbol, qty, fill, proceeds, realized, reason, now_et
            )
            actions.append(f"{bot_name} SELL {symbol} @ {fill:.2f} — {reason}")

    # 2) Portfolio-level risk layer. It can stop a bot independently of its strategy.
    # Exits remain allowed even on a daily entry pause.
    for bot_name, bot in state["bots"].items():
        m = mark_bot(bot, prices)
        equity = m["equity"]
        refresh_daily_risk(bot, equity, today)

        if bot.get("status", "ACTIVE") == "ACTIVE":
            reason = portfolio_stop_reason(bot, equity)
            if reason:
                liquidate_virtual_bot(state, bot_name, bot, prices, reason, now_et, actions)
            else:
                if update_daily_pause(bot, equity, today):
                    logging.info("%s new entries paused for %s after daily loss limit", bot_name, today)
        elif bot["positions"]:
            # Retry a previously incomplete virtual liquidation if market data was missing.
            reason = bot.get("stop_reason") or "previous portfolio stop"
            liquidate_virtual_bot(state, bot_name, bot, prices, reason, now_et, actions)

    # 3) Entries only in a safer session window, and only for ACTIVE/non-paused bots.
    next_close = clock.next_close.astimezone(NY)
    earliest_entry = datetime.combine(now_et.date(), time(9, 45), tzinfo=NY)
    latest_entry = next_close - timedelta(minutes=30)
    entry_window = earliest_entry <= now_et <= latest_entry

    if entry_window:
        for bot_name, bot in state["bots"].items():
            if bot.get("status", "ACTIVE") != "ACTIVE":
                continue
            if bot.get("entry_paused_date") == today:
                continue

            fraction = float(BOT_CONFIG[bot_name]["position_fraction"])
            for symbol in WATCHLIST:
                if len(bot["positions"]) >= MAX_POSITIONS:
                    break
                s = signals.get(symbol)
                if not s or not can_open_position(bot, symbol, today) or not should_enter(bot_name, s):
                    continue

                # Dynamic sizing: target a fraction of CURRENT marked equity, not a fixed dollar amount.
                equity_now = mark_bot(bot, prices)["equity"]
                target = max(0.0, equity_now * fraction)
                fill = simulated_fill(s.price, "BUY")
                spend = min(target, _f(bot["cash"]))
                if spend < min(100.0, target * 0.25):
                    continue
                qty = spend / fill
                bot["cash"] = round(_f(bot["cash"]) - spend, 8)
                bot["positions"][symbol] = {
                    "qty": round(qty, 10),
                    "avg_price": round(fill, 6),
                    "entry_time": now_et.isoformat(),
                    "entry_notional": round(spend, 2),
                    "imported": False,
                }
                bot["trade_count"] = int(bot.get("trade_count", 0)) + 1
                reason = f"{bot['strategy']} entry rule satisfied"
                append_trade(state, bot_name, "BUY", symbol, qty, fill, spend, 0.0, reason, now_et)
                actions.append(f"{bot_name} BUY {symbol} @ {fill:.2f} — {reason}")
    else:
        logging.info("Outside new-entry window; exits only.")

    # 4) Persist mark-to-market risk state after all virtual actions.
    for bot_name, bot in state["bots"].items():
        m = mark_bot(bot, prices)
        bot["last_equity"] = round(m["equity"], 8)
        bot["peak_equity"] = round(max(_f(bot.get("peak_equity")), m["equity"]), 8)

    state["last_run"] = now_et.isoformat()
    state["last_prices"] = {k: round(v, 6) for k, v in prices.items()}
    state["last_signals"] = {
        sym: {
            "price": round(s.price, 6),
            "sma20": round(s.sma20, 6),
            "sma50": round(s.sma50, 6),
            "rsi14": round(s.rsi14, 4),
            "ret5_pct": round(s.ret5_pct, 4),
            "prior20_high": round(s.prior20_high, 6),
            "zscore20": round(s.zscore20, 4),
            "news_score": s.news_score,
            "news_headlines": list(s.news_headlines),
        }
        for sym, s in signals.items()
    }
    atomic_json_write(STATE_PATH, state)
    write_report(state, prices, signals, actions, now_et)

    logging.info("Virtual actions: %s", actions or "none")
    for bot_name, bot in state["bots"].items():
        m = mark_bot(bot, prices)
        logging.info(
            "%s status=%s equity=$%.2f return=%.2f%% cash=$%.2f peak=$%.2f",
            bot_name,
            bot.get("status", "ACTIVE"),
            m["equity"],
            m["return_pct"],
            _f(bot["cash"]),
            _f(bot.get("peak_equity")),
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
