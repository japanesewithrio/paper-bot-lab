# Paper Bot Lab — Latest Report

Updated: 2026-10-21T12:05:31.203501-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,016.34 | 0.16% | $7,996.35 | $10,046.82 | $-4.57 | $20.90 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,835.08 | -1.65% | $4,910.94 | $10,009.55 | $-178.74 | $13.82 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,701.18 | -2.99% | $7,200.12 | $10,000.00 | $-299.88 | $1.06 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.48 | $338.01 | $327.73 | 71.2 | 0.75% | $348.11 | 1.46 | +1 |
| NVDA | $220.50 | $226.82 | $223.00 | 38.1 | 1.46% | $243.34 | -0.87 | +2 |
| AMD | $552.49 | $598.82 | $541.03 | 34.3 | -1.72% | $658.45 | -1.25 | +2 |
| MSFT | $529.53 | $525.07 | $507.28 | 62.5 | -1.82% | $551.08 | 0.37 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
