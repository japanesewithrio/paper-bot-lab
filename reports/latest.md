# Paper Bot Lab — Latest Report

Updated: 2026-10-19T12:25:11.563477-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,000.97 | 0.01% | $7,996.35 | $10,046.82 | $-4.57 | $5.54 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,916.03 | -0.84% | $7,455.20 | $10,007.62 | $-59.73 | $-24.24 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,865.47 | -1.35% | $4,910.94 | $10,009.55 | $-178.74 | $44.22 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,717.93 | -2.82% | $7,200.12 | $10,000.00 | $-299.88 | $17.81 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.86 | $337.59 | $326.28 | 68.9 | 0.16% | $348.11 | 1.03 | +1 |
| NVDA | $218.69 | $227.78 | $222.99 | 40.6 | -4.30% | $243.34 | -1.39 | +1 |
| AMD | $564.06 | $607.03 | $538.42 | 35.6 | -6.84% | $658.45 | -1.38 | +0 |
| MSFT | $533.07 | $521.81 | $506.20 | 65.7 | -1.92% | $551.08 | 0.80 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
