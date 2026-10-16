# Paper Bot Lab — Latest Report

Updated: 2026-10-16T15:51:34.510564-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,009.15 | 0.09% | $7,996.35 | $10,046.82 | $-4.57 | $13.72 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,926.07 | -0.74% | $7,455.20 | $10,007.62 | $-59.73 | $-14.20 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,689.92 | -3.10% | $7,200.12 | $10,000.00 | $-299.88 | $-10.20 | MSFT |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,656.35 | -3.44% | $4,910.94 | $10,009.55 | $-178.74 | $-164.90 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.25 | $337.47 | $325.72 | 56.8 | 0.65% | $348.11 | 1.42 | +2 |
| NVDA | $214.55 | $228.23 | $223.10 | 33.0 | -5.26% | $243.34 | -2.22 | -2 |
| AMD | $527.14 | $610.36 | $537.10 | 28.9 | -11.30% | $658.45 | -2.95 | +0 |
| MSFT | $527.14 | $520.14 | $505.50 | 62.0 | -2.58% | $551.08 | 0.49 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
