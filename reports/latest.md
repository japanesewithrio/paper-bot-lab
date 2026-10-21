# Paper Bot Lab — Latest Report

Updated: 2026-10-21T09:31:36.068522-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,988.16 | -0.12% | $7,996.35 | $10,046.82 | $-4.57 | $-7.27 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,903.56 | -0.96% | $4,910.94 | $10,009.55 | $-178.74 | $82.30 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,703.78 | -2.96% | $7,200.12 | $10,000.00 | $-299.88 | $3.66 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.68 | $337.77 | $327.63 | 65.9 | -0.65% | $348.11 | 0.45 | -1 |
| NVDA | $222.69 | $226.89 | $223.03 | 40.0 | 2.46% | $243.34 | -0.59 | +0 |
| AMD | $562.42 | $598.78 | $541.02 | 34.0 | 0.05% | $658.45 | -0.98 | +2 |
| MSFT | $530.08 | $524.82 | $507.18 | 58.6 | -1.72% | $551.08 | 0.44 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
