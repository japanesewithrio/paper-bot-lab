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

import os
import sys
from datetime import datetime, timezone

import pandas as pd

import bot_runner as B

START = os.getenv("BT_START", "2016-01-01")
SYMBOLS = list(B.WATCHLIST)
BENCH = "SPY"


def fetch():
    from alpaca.data.enums import Adjustment, DataFeed
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame

    cl = StockHistoricalDataClient(os.environ["ALPACA_API_KEY"].strip(), os.environ["ALPACA_SECRET_KEY"].strip())
    end = datetime.now(timezone.utc) - pd.Timedelta(days=1)
    out = {}
    for feed in (DataFeed.SIP, DataFeed.IEX):
        try:
            req = StockBarsRequest(symbol_or_symbols=SYMBOLS + [BENCH], timeframe=TimeFrame.Day, start=pd.Timestamp(START, tz="UTC"),
                                   end=end, adjustment=Adjustment.ALL, feed=feed, limit=100000)
            df = cl.get_stock_bars(req).df
            for s in SYMBOLS + [BENCH]:
                d = df.xs(s, level="symbol").sort_index()
                d.index = pd.to_datetime(d.index).tz_convert("America/New_York").normalize().tz_localize(None)
                out[s] = d[["open", "high", "low", "close"]].astype(float)
            print("data feed:", feed, {s: len(v) for s, v in out.items()})
            return out, str(feed)
        except Exception as e:
            print("feed", feed, "failed:", type(e).__name__, str(e)[:200])
    raise SystemExit("no historical data")


def simulate(bars, bot, live_stops=True):
    frac = B.BOT_CONFIG[bot]["position_fraction"]
    days = sorted(set.intersection(*[set(bars[s].index) for s in SYMBOLS]))
    cash, pos, status, peak = 10000.0, {}, "ACTIVE", 10000.0
    curve, trades = [], []
    for i, day in enumerate(days):
        price = {s: float(bars[s].loc[day, "close"]) for s in SYMBOLS}
        sig = {}
        for s in SYMBOLS:
            hist = bars[s].loc[:day].iloc[:-1].tail(220)      # completed bars before today
            if len(hist) >= 55:
                sig[s] = B.calculate_signal(hist, price[s], news_score=1 if bot == "BOT_C" else 0)
        # exits
        exited = set()
        for s in list(pos):
            if s not in sig:
                continue
            q, cost = pos[s]
            pl = (price[s] / cost - 1) * 100
            ok, why = B.should_exit(bot, sig[s], pl)
            if ok or status != "ACTIVE":
                fill = B.simulated_fill(price[s], "SELL")
                cash += q * fill
                trades.append((day, s, "SELL", fill, (fill - cost) * q, why or "portfolio stop"))
                del pos[s]
                exited.add(s)
        equity = cash + sum(q * price[s] for s, (q, c) in pos.items())
        peak = max(peak, equity)
        if live_stops and status == "ACTIVE" and (equity <= 10000 * B.HARD_FLOOR_PCT or equity <= peak * (1 - B.MAX_PEAK_DRAWDOWN_PCT)):
            status = "STOPPED"
            for s in list(pos):
                q, cost = pos[s]
                fill = B.simulated_fill(price[s], "SELL")
                cash += q * fill
                trades.append((day, s, "SELL", fill, (fill - cost) * q, "portfolio stop"))
                del pos[s]
            equity = cash
        # entries
        if status == "ACTIVE":
            for s in SYMBOLS:
                if s in sig and s not in pos and s not in exited and len(pos) < B.MAX_POSITIONS and B.should_enter(bot, sig[s]):
                    amt = min(cash, equity * frac)
                    if amt < 50:
                        continue
                    fill = B.simulated_fill(price[s], "BUY")
                    pos[s] = (amt / fill, fill)
                    cash -= amt
                    trades.append((day, s, "BUY", fill, 0.0, "entry"))
        equity = cash + sum(q * price[s] for s, (q, c) in pos.items())
        curve.append((day, equity))
    return pd.Series(dict(curve)), trades, status


def stats(curve):
    r = curve.pct_change().dropna()
    yrs = max((curve.index[-1] - curve.index[0]).days / 365.25, 0.01)
    cagr = (curve.iloc[-1] / curve.iloc[0]) ** (1 / yrs) - 1
    dd = (curve / curve.cummax() - 1).min()
    sharpe = (r.mean() / r.std() * (252 ** 0.5)) if r.std() > 0 else 0.0
    return curve.iloc[-1] / curve.iloc[0] - 1, cagr, dd, sharpe


def main():
    bars, feed = fetch()
    days = sorted(set.intersection(*[set(bars[s].index) for s in SYMBOLS]))[55:]
    first = days[0]
    rows, curves = [], {}
    for live in (True, False):
        for bot in B.BOT_CONFIG:
            c, tr, st = simulate(bars, bot, live)
            c = c.loc[first:]
            sells = [t for t in tr if t[2] == "SELL"]
            wins = sum(1 for t in sells if t[4] > 0)
            tot, cagr, dd, sh = stats(c)
            label = "%s%s" % (bot, "" if live else " (no permanent stop)")
            rows.append([label, B.BOT_CONFIG[bot]["strategy"], tot, cagr, dd, sh, len(sells), wins / len(sells) if sells else 0, st if live else "-",
                         str(c[c.diff() != 0].index[-1].date()) if live and st == "STOPPED" else ""])
            curves[label] = c
    # benchmarks
    ew = sum(10000 / 4 * bars[s].loc[first:, "close"] / bars[s].loc[first, "close"] for s in SYMBOLS)
    spy = 10000 * bars[BENCH].loc[first:, "close"] / bars[BENCH].loc[first, "close"]
    for label, c in (("Buy & hold 4 stocks", ew), ("Buy & hold SPY (S&P 500)", spy)):
        tot, cagr, dd, sh = stats(c.dropna())
        rows.append([label, "benchmark", tot, cagr, dd, sh, 0, 0, "-", ""])
        curves[label] = c
    # yearly returns (raw strategies)
    yearly = {}
    for label, c in curves.items():
        if "(no permanent stop)" in label or label.startswith("Buy"):
            y = c.groupby(c.index.year).last()
            prev = y.shift(1)
            prev.iloc[0] = c.iloc[0]
            yearly[label.replace(" (no permanent stop)", "")] = (y / prev - 1) * 100
    ydf = pd.DataFrame(yearly).round(1)

    pct = lambda v: "%+.1f%%" % (v * 100)
    md = ["# Paper Bot Lab — Backtest", "", "Generated: %s · data: Alpaca daily bars (%s, split/dividend adjusted) · %s → %s" % (
        datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), feed, first.date(), days[-1].date()), "",
          "> Simulation only. Past results do not predict future results. Not financial advice.", "",
          "| Bot / benchmark | Strategy | Total return | CAGR | Max drawdown | Sharpe | Trades | Win rate | Status | Stopped on |",
          "|---|---|---:|---:|---:|---:|---:|---:|---|---|"]
    for r in rows:
        md.append("| %s | %s | %s | %s | %s | %.2f | %d | %s | %s | %s |" % (r[0], r[1], pct(r[2]), pct(r[3]), pct(r[4]), r[5], r[6],
                                                                         "%.0f%%" % (r[7] * 100) if r[6] else "-", r[8], r[9]))
    md += ["", "## Return by year (%, strategies without the permanent stop)", "", ydf.to_markdown(), "",
           "## How this test works", "",
           "- One decision per trading day at the close, same rules as `bot_runner.py`, 5 bps slippage on every fill.",
           "- BOT_C: the news filter cannot be replayed, so only its price rules are tested (news treated as positive).",
           "- \"With live stops\" rows apply the live rules (stop forever at -20% or -15% from peak). The \"no permanent stop\" rows show the strategy itself.",
           "- The 4 stocks were chosen after they became big winners (selection bias), so buy & hold of these 4 looks better than it would have looked in advance."]
    os.makedirs("reports", exist_ok=True)
    open("reports/backtest.md", "w").write("\n".join(md) + "\n")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10, 5.5))
        for label, c in curves.items():
            if "(no permanent stop)" in label or label.startswith("Buy"):
                ax.plot(c.index, c.values, label=label.replace(" (no permanent stop)", ""), lw=1.6 if label.startswith("Buy") else 1.2,
                        ls="--" if label.startswith("Buy") else "-")
        ax.set_yscale("log"); ax.set_ylabel("equity ($, log)"); ax.grid(alpha=.3); ax.legend(fontsize=8)
        ax.set_title("Paper Bot Lab backtest — $10,000 start (no permanent stop)")
        fig.tight_layout(); fig.savefig("reports/backtest.png", dpi=110)
    except Exception as e:
        print("chart skipped:", e)
    print("\n".join(md))


if __name__ == "__main__":
    sys.exit(main())
