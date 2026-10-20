# Paper Bot Lab — Latest Report

Updated: 2026-10-20T14:21:30.375312-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,990.68 | -0.09% | $7,996.35 | $10,046.82 | $-4.57 | $-4.75 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,738.73 | -2.61% | $4,910.94 | $10,009.55 | $-178.74 | $-82.53 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,709.52 | -2.90% | $7,200.12 | $10,000.00 | $-299.88 | $9.40 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $340.11 | $337.66 | $326.95 | 61.4 | -0.85% | $348.11 | 0.58 | -2 |
| NVDA | $217.02 | $227.11 | $222.95 | 36.9 | -2.02% | $243.34 | -1.43 | -1 |
| AMD | $539.50 | $602.35 | $539.63 | 31.8 | -5.51% | $658.45 | -1.80 | +2 |
| MSFT | $531.29 | $523.54 | $506.73 | 62.9 | -0.51% | $551.08 | 0.59 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
