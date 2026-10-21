# Paper Bot Lab — Latest Report

Updated: 2026-10-21T15:08:05.915652-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,011.94 | 0.12% | $7,996.35 | $10,046.82 | $-4.57 | $16.50 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,909.06 | -0.91% | $4,910.94 | $10,009.55 | $-178.74 | $87.81 | AMD, NVDA |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,711.12 | -2.89% | $7,200.12 | $10,000.00 | $-299.88 | $11.01 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.73 | $337.98 | $327.72 | 70.7 | 0.53% | $348.11 | 1.31 | +0 |
| NVDA | $220.81 | $226.84 | $223.01 | 38.7 | 1.60% | $243.34 | -0.84 | -1 |
| AMD | $568.50 | $599.03 | $541.12 | 35.6 | 1.13% | $658.45 | -0.83 | +2 |
| MSFT | $531.63 | $525.04 | $507.26 | 61.9 | -1.43% | $551.08 | 0.55 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
