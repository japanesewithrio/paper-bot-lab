# Paper Bot Lab — Latest Report

Updated: 2026-10-14T11:28:18.412557-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,024.17 | 0.24% | $7,996.35 | $10,046.82 | $-4.57 | $28.73 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,998.75 | -0.01% | $7,500.00 | $10,000.00 | $0.00 | $-1.25 | AMD |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,741.99 | -2.58% | $7,200.12 | $10,000.00 | $-299.88 | $41.87 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.81 | $336.98 | $324.54 | 60.7 | 1.58% | $348.11 | 2.23 | -3 |
| NVDA | $223.14 | $228.80 | $223.26 | 48.2 | -3.22% | $243.34 | -1.09 | +0 |
| AMD | $581.00 | $611.58 | $534.92 | 35.0 | -6.42% | $658.45 | -1.20 | +1 |
| MSFT | $538.16 | $516.54 | $503.99 | 75.3 | 2.96% | $551.08 | 1.39 | -1 |

## Actions this run

- BOT_B BUY AMD @ 581.29 — Dip / Mean Reversion entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
