# Paper Bot Lab — Latest Report

Updated: 2026-10-20T11:59:15.632856-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.64 | -0.04% | $7,996.35 | $10,046.82 | $-4.57 | $0.20 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,743.02 | -2.57% | $4,910.94 | $10,009.55 | $-178.74 | $-78.24 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,711.50 | -2.88% | $7,200.12 | $10,000.00 | $-299.88 | $11.38 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $340.95 | $337.70 | $326.96 | 63.1 | -0.60% | $348.11 | 0.77 | -1 |
| NVDA | $217.54 | $227.13 | $222.96 | 37.6 | -1.78% | $243.34 | -1.37 | +0 |
| AMD | $539.15 | $602.48 | $539.68 | 32.7 | -5.57% | $658.45 | -1.82 | +2 |
| MSFT | $531.71 | $523.50 | $506.71 | 62.3 | -0.44% | $551.08 | 0.63 | +1 |

## Actions this run

- BOT_C SELL AAPL @ 340.78 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
