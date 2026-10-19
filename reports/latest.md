# Paper Bot Lab — Latest Report

Updated: 2026-10-19T11:08:50.200063-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,007.48 | 0.07% | $7,996.35 | $10,046.82 | $-4.57 | $12.05 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,924.02 | -0.76% | $7,455.20 | $10,007.62 | $-59.73 | $-16.25 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,805.96 | -1.94% | $4,910.94 | $10,009.55 | $-178.74 | $-15.30 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,719.39 | -2.81% | $7,200.12 | $10,000.00 | $-299.88 | $19.27 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.97 | $337.65 | $326.31 | 71.7 | 0.48% | $348.11 | 1.26 | +1 |
| NVDA | $218.16 | $227.75 | $222.98 | 39.8 | -4.52% | $243.34 | -1.46 | +1 |
| AMD | $551.86 | $607.15 | $538.47 | 36.3 | -8.85% | $658.45 | -1.79 | +0 |
| MSFT | $533.38 | $521.85 | $506.22 | 66.1 | -1.86% | $551.08 | 0.82 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
