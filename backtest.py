"""Backtest of the four Paper Bot Lab strategies on daily history (simulation only, no orders).

Uses the SAME entry/exit rules and signal maths as bot_runner.py (imported, not copied).
Simplifications, stated in the report:
- one decision per trading day, at the daily close, with 5 bps slippage each way;
- BOT_C's news filter cannot be replayed (no historical news score), so BOT_C is tested as
  "momentum part only" (news treated as neutral-positive);
- the live portfolio stops (-20% floor, -15% from peak) are applied in the "with live stops"
  run; a second run without the permanent stops shows the raw strategy.
"""
from __future__ import annotations

import dataclasses
import os
import sys
from datetime import datetime, timezone

import pandas as pd

import bot_runner as B

START = os.getenv("BT_START", "2016-01-01")
SYMBOLS = list(B.WATCHLIST)
BENCH = "SPY"
# The 28 largest US companies at the START of 2016 (approx. market-cap order then), chosen so that the
# test does not only contain stocks we already know became winners (GE, INTC, IBM, T ... are in it too).
TOP2016 = ["AAPL", "GOOGL", "MSFT", "XOM", "BRK.B", "AMZN", "GE", "META", "JNJ", "WFC", "JPM", "PG", "T", "PFE", "WMT",
           "VZ", "CVX", "KO", "PEP", "INTC", "ORCL", "MRK", "HD", "DIS", "CSCO", "IBM", "BAC", "C"]
COOLDOWN_DAYS = 20


def fetch(symbols=None):
    symbols = symbols or SYMBOLS
    from alpaca.data.enums import Adjustment, DataFeed
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame

    cl = StockHistoricalDataClient(os.environ["ALPACA_API_KEY"].strip(), os.environ["ALPACA_SECRET_KEY"].strip())
    end = datetime.now(timezone.utc) - pd.Timedelta(days=1)
    out = {}
    for feed in (DataFeed.SIP, DataFeed.IEX):
        try:
            req = StockBarsRequest(symbol_or_symbols=symbols + [BENCH], timeframe=TimeFrame.Day, start=pd.Timestamp(START, tz="UTC"),
                                   end=end, adjustment=Adjustment.ALL, feed=feed, limit=100000)
            df = cl.get_stock_bars(req).df
            for s in symbols + [BENCH]:
                if s not in df.index.get_level_values("symbol"):
                    print("no data:", s)
                    continue
                d = df.xs(s, level="symbol").sort_index()
                d.index = pd.to_datetime(d.index).tz_convert("America/New_York").normalize().tz_localize(None)
                out[s] = d[["open", "high", "low", "close"]].astype(float)
            print("data feed:", feed, {s: len(v) for s, v in out.items()})
            return out, str(feed)
        except Exception as e:
            print("feed", feed, "failed:", type(e).__name__, str(e)[:200])
    raise SystemExit("no historical data")


_SIG = {}


def signal(bars, s, day, price):
    """signals depend only on the stock and the day, so compute them once for all bots and rule variants"""
    k = (s, day)
    if k not in _SIG:
        b = bars[s]
        hist = b.loc[:day].iloc[:-1].tail(220)
        _SIG[k] = B.calculate_signal(hist, price) if len(hist) >= 55 else None
    return _SIG[k]


_REGIME = {}


def risk_on(bars, day):
    """market filter: S&P 500 (SPY) above its 200-day average, using completed bars only"""
    if day not in _REGIME:
        c = bars[BENCH]["close"].loc[:day].iloc[:-1]
        _REGIME[day] = len(c) < 200 or float(c.iloc[-1]) > float(c.tail(200).mean())
    return _REGIME[day]


def rank_key(bot, sg):
    return sg.zscore20 if bot == "BOT_B" else -sg.ret5_pct      # most oversold first for B, strongest move first for others


def simulate(bars, bot, mode="permanent", symbols=None, regime=False):
    """mode: permanent = live rule (stop forever) · cooldown = sit out COOLDOWN_DAYS, then restart from current equity · none"""
    symbols = [s for s in (symbols or SYMBOLS) if s in bars]
    frac = B.BOT_CONFIG[bot]["position_fraction"]
    days = sorted(set.union(*[set(bars[s].index) for s in symbols]))
    cash, pos, status, peak, resume = 10000.0, {}, "ACTIVE", 10000.0, None
    base = 10000.0
    curve, trades, stops = [], [], 0
    for i, day in enumerate(days):
        price, sig = {}, {}
        for s in symbols:
            b = bars[s]
            if day in b.index:
                price[s] = float(b.loc[day, "close"])
                sg = signal(bars, s, day, price[s])
                if sg is not None:
                    sig[s] = dataclasses.replace(sg, news_score=1) if bot == "BOT_C" else sg
        if status == "COOLDOWN" and i >= resume:
            status = "ACTIVE"
        exited = set()
        for s in list(pos):
            if s not in sig:
                continue
            q, cost = pos[s]
            ok, why = B.should_exit(bot, sig[s], (price[s] / cost - 1) * 100)
            if ok:
                fill = B.simulated_fill(price[s], "SELL")
                cash += q * fill
                trades.append((day, s, "SELL", fill, (fill - cost) * q, why))
                del pos[s]
                exited.add(s)
        val = lambda: cash + sum(q * price.get(s, c) for s, (q, c) in pos.items())
        equity = val()
        peak = max(peak, equity)
        if mode != "none" and status == "ACTIVE" and (equity <= base * B.HARD_FLOOR_PCT or equity <= peak * (1 - B.MAX_PEAK_DRAWDOWN_PCT)):
            for s in list(pos):
                q, cost = pos[s]
                fill = B.simulated_fill(price.get(s, cost), "SELL")
                cash += q * fill
                trades.append((day, s, "SELL", fill, (fill - cost) * q, "portfolio stop"))
                del pos[s]
            equity = cash
            stops += 1
            if mode == "permanent":
                status = "STOPPED"
            else:
                status, resume, peak, base = "COOLDOWN", i + COOLDOWN_DAYS, equity, equity
        if status == "ACTIVE" and (not regime or risk_on(bars, day)):
            cands = sorted((s for s in sig if s not in pos and s not in exited and B.should_enter(bot, sig[s])), key=lambda s: rank_key(bot, sig[s]))
            for s in cands:
                if len(pos) >= B.MAX_POSITIONS:
                    break
                amt = min(cash, equity * frac)
                if amt < 50:
                    break
                fill = B.simulated_fill(price[s], "BUY")
                pos[s] = (amt / fill, fill)
                cash -= amt
                trades.append((day, s, "BUY", fill, 0.0, "entry"))
        curve.append((day, val()))
    return pd.Series(dict(curve)), trades, status, stops


def stats(curve):
    r = curve.pct_change().dropna()
    yrs = max((curve.index[-1] - curve.index[0]).days / 365.25, 0.01)
    cagr = (curve.iloc[-1] / curve.iloc[0]) ** (1 / yrs) - 1
    dd = (curve / curve.cummax() - 1).min()
    sharpe = (r.mean() / r.std() * (252 ** 0.5)) if r.std() > 0 else 0.0
    return curve.iloc[-1] / curve.iloc[0] - 1, cagr, dd, sharpe


def run_universe(bars, symbols, title):
    symbols = [x for x in symbols if x in bars]
    days = sorted(set.union(*[set(bars[x].index) for x in symbols]))[55:]
    first = days[0]
    rows, curves = [], {}
    for mode, tag, reg in (("permanent", "live rule: stop forever (old)", False), ("cooldown", "cooldown (live now)", False),
                           ("cooldown", "cooldown + market filter (SPY > 200-day avg)", True), ("none", "no portfolio stop", False)):
        for bot in B.BOT_CONFIG:
            c, tr, st, n = simulate(bars, bot, mode, symbols, reg)
            c = c.loc[first:]
            sells = [t for t in tr if t[2] == "SELL"]
            wins = sum(1 for t in sells if t[4] > 0)
            tot, cagr, dd, sh = stats(c)
            rows.append([bot, tag, tot, cagr, dd, sh, len(sells), wins / len(sells) if sells else 0, st, n])
            curves[(bot, mode + ("+regime" if reg else ""))] = c
    ew = None
    for x in symbols:
        sr = bars[x]["close"].loc[first:]
        sr = 10000 / len(symbols) * sr / sr.iloc[0]
        ew = sr if ew is None else ew.add(sr, fill_value=0)
    spy = 10000 * bars[BENCH].loc[first:, "close"] / bars[BENCH].loc[first, "close"]
    for label, c in (("Buy & hold these %d stocks" % len(symbols), ew), ("Buy & hold SPY (S&P 500)", spy)):
        tot, cagr, dd, sh = stats(c.dropna())
        rows.append([label, "benchmark", tot, cagr, dd, sh, 0, 0, "-", 0])
        curves[(label, "bench")] = c
    return title, symbols, first, days[-1], rows, curves


def main():
    bars, feed = fetch(sorted(set(SYMBOLS + TOP2016)))
    results = [run_universe(bars, SYMBOLS, "Live watchlist (4 stocks)"), run_universe(bars, TOP2016, "28 biggest US companies of early 2016")]
    pct = lambda v: "%+.1f%%" % (v * 100)
    md = ["# Paper Bot Lab — Backtest", "", "Generated: %s · data: Alpaca daily bars (%s, split/dividend adjusted)" % (
        datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), feed), "",
          "> Simulation only. Past results do not predict future results. Not financial advice.", ""]
    for title, syms, first, last, rows, curves in results:
        md += ["## %s · %s → %s" % (title, first.date(), last.date()), "", "Stocks: " + ", ".join(syms), "",
               "| Bot / benchmark | Rules | Total return | CAGR | Max drawdown | Sharpe | Trades | Win rate | End status | Stops hit |",
               "|---|---|---:|---:|---:|---:|---:|---:|---|---:|"]
        for r in rows:
            md.append("| %s | %s | %s | %s | %s | %.2f | %d | %s | %s | %d |" % (r[0], r[1], pct(r[2]), pct(r[3]), pct(r[4]), r[5], r[6],
                                                                            "%.0f%%" % (r[7] * 100) if r[6] else "-", r[8], r[9]))
        md.append("")
    md += ["## How this test works", "",
           "- One decision per trading day at the close, same entry/exit rules as `bot_runner.py`, 5 bps slippage on every fill, max 3 positions.",
           "- When several stocks qualify on the same day: BOT_B takes the most oversold first, the others the strongest 5-day move first.",
           "- BOT_C: the news filter cannot be replayed, so only its price rules are tested (news treated as positive).",
           "- The 28-stock universe is the largest US companies at the start of 2016, so it includes later losers (GE, INTC, IBM, T ...) and is a fairer test than the 4 hand-picked winners."]
    os.makedirs("reports", exist_ok=True)
    open("reports/backtest.md", "w").write("\n".join(md) + "\n")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
        for ax, (title, syms, first, last, rows, curves) in zip(axs, results):
            for (label, mode), c in curves.items():
                if mode in ("cooldown", "bench"):
                    ax.plot(c.index, c.values, label=label, lw=1.6 if mode == "bench" else 1.2, ls="--" if mode == "bench" else "-")
            ax.set_yscale("log"); ax.grid(alpha=.3); ax.legend(fontsize=8); ax.set_title(title + " (cooldown rule)", fontsize=10)
        axs[0].set_ylabel("equity ($, log, $10,000 start)")
        fig.tight_layout(); fig.savefig("reports/backtest.png", dpi=110)
    except Exception as e:
        print("chart skipped:", e)
    print("\n".join(md))


if __name__ == "__main__":
    sys.exit(main())
