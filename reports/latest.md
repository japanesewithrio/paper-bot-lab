# Paper Bot Lab — Latest Report

Updated: 2026-10-19T15:07:26.252120-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,008.30 | 0.08% | $7,996.35 | $10,046.82 | $-4.57 | $12.87 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,925.03 | -0.75% | $7,455.20 | $10,007.62 | $-59.73 | $-15.24 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,772.50 | -2.27% | $4,910.94 | $10,009.55 | $-178.74 | $-48.76 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,725.65 | -2.74% | $7,200.12 | $10,000.00 | $-299.88 | $25.53 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.11 | $337.66 | $326.31 | 71.8 | 0.52% | $348.11 | 1.30 | +1 |
| NVDA | $217.33 | $227.71 | $222.97 | 38.8 | -4.89% | $243.34 | -1.57 | +1 |
| AMD | $546.38 | $606.69 | $538.28 | 33.4 | -9.76% | $658.45 | -1.89 | +1 |
| MSFT | $534.71 | $521.86 | $506.22 | 66.1 | -1.62% | $551.08 | 0.91 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
