# Paper Bot Lab — Latest Report

Updated: 2026-11-27T09:31:00.996719-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,896.78 | -1.03% | $7,886.46 | $10,051.61 | $-141.92 | $38.70 | AAPL |
| 2 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,231.92 | -7.68% | $6,898.65 | $10,007.62 | $-801.80 | $33.72 | AAPL |
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
| AAPL | $358.37 | $349.24 | $343.52 | 66.3 | 4.36% | $360.81 | 1.40 | +1 |
| NVDA | $149.68 | $169.30 | $202.28 | 35.4 | 19.12% | $209.97 | -0.90 | -1 |
| AMD | $418.47 | $481.65 | $545.74 | 46.6 | -1.38% | $593.93 | -1.25 | +0 |
| MSFT | $486.58 | $515.69 | $519.64 | 36.0 | 0.26% | $559.12 | -1.56 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
