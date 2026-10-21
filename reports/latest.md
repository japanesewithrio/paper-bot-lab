# Paper Bot Lab — Latest Report

Updated: 2026-10-21T15:56:31.712996-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,013.02 | 0.13% | $7,996.35 | $10,046.82 | $-4.57 | $17.59 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,857.08 | -1.43% | $4,910.94 | $10,009.55 | $-178.74 | $35.82 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,718.23 | -2.82% | $7,200.12 | $10,000.00 | $-299.88 | $18.11 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.92 | $337.99 | $327.72 | 70.8 | 0.59% | $348.11 | 1.35 | +0 |
| NVDA | $221.98 | $226.89 | $223.03 | 40.2 | 2.14% | $243.34 | -0.69 | -1 |
| AMD | $553.66 | $598.98 | $541.10 | 35.3 | -1.51% | $658.45 | -1.23 | +2 |
| MSFT | $533.13 | $525.12 | $507.30 | 63.0 | -1.15% | $551.08 | 0.66 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
