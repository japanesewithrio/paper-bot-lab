# Paper Bot Lab — Latest Report

Updated: 2026-10-30T14:21:15.305877-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,007.37 | 0.07% | $7,996.35 | $10,051.61 | $-4.57 | $11.93 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,884.10 | -1.16% | $9,884.10 | $10,007.62 | $-115.90 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,630.76 | -3.69% | $7,223.97 | $10,009.55 | $-368.03 | $-1.20 | AMD |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.95 | $342.03 | $333.03 | 52.6 | -0.28% | $351.68 | 0.21 | -1 |
| NVDA | $201.63 | $221.33 | $221.71 | 29.2 | -6.66% | $243.34 | -2.00 | -2 |
| AMD | $497.11 | $570.04 | $548.12 | 34.5 | -6.45% | $658.45 | -1.63 | -3 |
| MSFT | $520.23 | $531.03 | $512.91 | 35.3 | -2.31% | $551.08 | -1.79 | +1 |

## Actions this run

- BOT_B SELL NVDA @ 201.53 — stop -7%
- BOT_B BUY AMD @ 497.36 — Dip / Mean Reversion entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
