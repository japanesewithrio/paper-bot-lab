# Paper Bot Lab — Latest Report

Updated: 2026-10-21T14:24:16.985545-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,017.92 | 0.18% | $7,996.35 | $10,046.82 | $-4.57 | $22.49 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,865.08 | -1.35% | $4,910.94 | $10,009.55 | $-178.74 | $43.82 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,716.41 | -2.84% | $7,200.12 | $10,000.00 | $-299.88 | $16.30 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.75 | $338.03 | $327.73 | 71.5 | 0.83% | $348.11 | 1.51 | +0 |
| NVDA | $221.78 | $226.88 | $223.02 | 39.9 | 2.05% | $243.34 | -0.71 | +1 |
| AMD | $556.00 | $599.06 | $541.13 | 35.8 | -1.10% | $658.45 | -1.17 | +2 |
| MSFT | $532.75 | $525.12 | $507.30 | 63.0 | -1.23% | $551.08 | 0.63 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
