# Paper Bot Lab — Latest Report

Updated: 2026-10-19T11:57:28.865068-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,008.60 | 0.09% | $7,996.35 | $10,046.82 | $-4.57 | $13.16 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,925.39 | -0.75% | $7,455.20 | $10,007.62 | $-59.73 | $-14.88 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,879.08 | -1.21% | $4,910.94 | $10,009.55 | $-178.74 | $57.82 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,725.36 | -2.75% | $7,200.12 | $10,000.00 | $-299.88 | $25.25 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.16 | $337.62 | $326.30 | 70.4 | 0.54% | $348.11 | 1.33 | +1 |
| NVDA | $219.33 | $227.82 | $223.01 | 41.6 | -4.01% | $243.34 | -1.31 | +0 |
| AMD | $565.50 | $607.23 | $538.49 | 36.8 | -6.60% | $658.45 | -1.35 | +0 |
| MSFT | $534.64 | $521.88 | $506.23 | 66.3 | -1.63% | $551.08 | 0.91 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
