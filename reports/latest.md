# Paper Bot Lab — Latest Report

Updated: 2026-11-27T11:00:31.751310-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,902.25 | -0.98% | $7,886.46 | $10,051.61 | $-141.92 | $44.17 | AAPL |
| 2 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,238.27 | -7.62% | $6,898.65 | $10,007.62 | $-801.80 | $40.06 | AAPL |
| 4 | BOT_B | COOLDOWN | Dip / Mean Reversion | $8,374.65 | -16.25% | $8,374.65 | $10,009.55 | $-1,625.35 | $0.00 | — |

## Portfolio risk rules

- Stop at 80% of the equity at the last (re)start, or after a 15% drawdown from the peak.
- A stopped bot sells everything and sits out 28 calendar days (COOLDOWN), then restarts from its current equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $359.34 | $349.28 | $343.54 | 66.9 | 4.64% | $360.81 | 1.53 | +1 |
| NVDA | $147.49 | $169.19 | $202.23 | 34.7 | 17.38% | $209.97 | -0.99 | -1 |
| AMD | $415.97 | $481.53 | $545.70 | 46.3 | -1.96% | $593.93 | -1.30 | +0 |
| MSFT | $491.45 | $515.31 | $519.49 | 31.4 | 1.26% | $559.12 | -1.25 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
