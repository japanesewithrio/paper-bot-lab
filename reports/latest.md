# Paper Bot Lab — Latest Report

Updated: 2026-10-21T10:59:15.981232-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,006.87 | 0.07% | $7,996.35 | $10,046.82 | $-4.57 | $11.43 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,797.22 | -2.03% | $4,910.94 | $10,009.55 | $-178.74 | $-24.04 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,705.27 | -2.95% | $7,200.12 | $10,000.00 | $-299.88 | $5.15 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.87 | $337.93 | $327.69 | 69.6 | 0.28% | $348.11 | 1.14 | +0 |
| NVDA | $219.08 | $226.80 | $222.99 | 37.7 | 0.81% | $243.34 | -1.07 | +3 |
| AMD | $547.51 | $598.58 | $540.94 | 32.8 | -2.61% | $658.45 | -1.36 | +2 |
| MSFT | $530.39 | $525.01 | $507.25 | 61.5 | -1.66% | $551.08 | 0.45 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
