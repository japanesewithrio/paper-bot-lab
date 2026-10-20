# Paper Bot Lab — Latest Report

Updated: 2026-10-20T13:55:19.046517-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,988.28 | -0.12% | $7,996.35 | $10,046.82 | $-4.57 | $-7.16 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,742.97 | -2.57% | $4,910.94 | $10,009.55 | $-178.74 | $-78.28 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,714.83 | -2.85% | $7,200.12 | $10,000.00 | $-299.88 | $14.71 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.69 | $337.66 | $326.95 | 61.2 | -0.97% | $348.11 | 0.48 | -1 |
| NVDA | $217.40 | $227.13 | $222.96 | 37.5 | -1.85% | $243.34 | -1.39 | -1 |
| AMD | $539.50 | $602.42 | $539.66 | 32.3 | -5.51% | $658.45 | -1.81 | +2 |
| MSFT | $532.41 | $523.54 | $506.73 | 63.0 | -0.30% | $551.08 | 0.68 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
