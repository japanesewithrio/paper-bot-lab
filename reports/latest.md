# Paper Bot Lab — Latest Report

Updated: 2026-10-19T14:19:09.008397-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,010.00 | 0.10% | $7,996.35 | $10,046.82 | $-4.57 | $14.57 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,927.11 | -0.73% | $7,455.20 | $10,007.62 | $-59.73 | $-13.16 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,772.49 | -2.28% | $4,910.94 | $10,009.55 | $-178.74 | $-48.76 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,724.77 | -2.75% | $7,200.12 | $10,000.00 | $-299.88 | $24.66 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.40 | $337.67 | $326.31 | 72.3 | 0.61% | $348.11 | 1.36 | +1 |
| NVDA | $217.61 | $227.72 | $222.97 | 39.1 | -4.77% | $243.34 | -1.53 | +0 |
| AMD | $545.67 | $606.60 | $538.25 | 32.8 | -9.88% | $658.45 | -1.90 | +1 |
| MSFT | $534.52 | $521.83 | $506.21 | 65.9 | -1.65% | $551.08 | 0.90 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
