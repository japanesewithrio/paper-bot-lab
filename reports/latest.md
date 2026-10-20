# Paper Bot Lab — Latest Report

Updated: 2026-10-20T09:31:40.680570-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,000.97 | 0.01% | $7,996.35 | $10,046.82 | $-4.57 | $5.54 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,916.03 | -0.84% | $7,455.20 | $10,007.62 | $-59.73 | $-24.24 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,736.88 | -2.63% | $4,910.94 | $10,009.55 | $-178.74 | $-84.38 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,713.91 | -2.86% | $7,200.12 | $10,000.00 | $-299.88 | $13.79 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.86 | $337.69 | $326.96 | 62.6 | -0.34% | $348.11 | 0.99 | +0 |
| NVDA | $215.20 | $227.04 | $222.92 | 35.7 | -2.84% | $243.34 | -1.66 | +0 |
| AMD | $543.76 | $601.93 | $539.46 | 30.0 | -4.76% | $658.45 | -1.63 | +2 |
| MSFT | $532.22 | $523.57 | $506.74 | 63.6 | -0.34% | $551.08 | 0.66 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
