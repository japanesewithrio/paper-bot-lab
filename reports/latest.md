# Paper Bot Lab — Latest Report

Updated: 2026-11-25T12:00:33.276262-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,858.08 | -1.42% | $9,858.08 | $10,051.61 | $-141.92 | $0.00 | — |
| 2 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,198.20 | -8.02% | $9,198.20 | $10,007.62 | $-801.80 | $0.00 | — |
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
| AAPL | $349.00 | $348.46 | $342.97 | 54.5 | -0.03% | $360.81 | 0.09 | +1 |
| NVDA | $142.07 | $172.14 | $203.53 | 35.8 | -2.68% | $215.32 | -1.27 | +0 |
| AMD | $375.47 | $487.61 | $547.70 | 47.3 | -23.29% | $593.93 | -2.07 | +1 |
| MSFT | $482.52 | $516.90 | $519.48 | 27.1 | -3.19% | $559.12 | -1.80 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
