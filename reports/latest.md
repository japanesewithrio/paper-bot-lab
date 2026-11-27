# Paper Bot Lab — Latest Report

Updated: 2026-11-27T12:30:31.191471-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,894.14 | -1.06% | $7,886.46 | $10,051.61 | $-141.92 | $36.07 | AAPL |
| 2 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,228.86 | -7.71% | $6,898.65 | $10,007.62 | $-801.80 | $30.66 | AAPL |
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
| AAPL | $357.89 | $349.22 | $343.52 | 66.1 | 4.22% | $360.81 | 1.34 | +1 |
| NVDA | $149.23 | $169.28 | $202.27 | 35.3 | 18.77% | $209.97 | -0.92 | -1 |
| AMD | $418.15 | $481.70 | $545.76 | 46.7 | -1.45% | $593.93 | -1.26 | +0 |
| MSFT | $491.70 | $515.31 | $519.49 | 31.4 | 1.31% | $559.12 | -1.24 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
