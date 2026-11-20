# Paper Bot Lab — Latest Report

Updated: 2026-11-20T15:52:05.563367-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,858.08 | -1.42% | $9,858.08 | $10,051.61 | $-141.92 | $0.00 | — |
| 2 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,198.20 | -8.02% | $9,198.20 | $10,007.62 | $-801.80 | $0.00 | — |
| 4 | BOT_B | STOPPED | Dip / Mean Reversion | $8,374.65 | -16.25% | $8,374.65 | $10,009.55 | $-1,625.35 | $0.00 | — |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.66 | $347.57 | $341.85 | 53.6 | -2.59% | $360.81 | -0.66 | +1 |
| NVDA | $127.56 | $181.56 | $207.05 | 14.0 | -18.31% | $219.91 | -2.05 | -2 |
| AMD | $426.20 | $509.14 | $553.11 | 46.0 | -15.46% | $593.93 | -1.75 | -2 |
| MSFT | $484.78 | $523.03 | $519.87 | 42.8 | -6.45% | $559.12 | -2.38 | +2 |

## Actions this run

- BOT_B SELL NVDA @ 127.49 — stop -7%
- BOT_C SELL AMD @ 425.99 — negative news, price<SMA20, stop -6%
- BOT_D SELL AAPL @ 343.49 — price<SMA20
- BOT_B STOPPED — peak drawdown >= 15%

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
