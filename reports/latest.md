# Paper Bot Lab — Latest Report

Updated: 2026-10-23T10:11:52.917876-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,036.39 | 0.36% | $7,996.35 | $10,051.61 | $-4.57 | $40.96 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,914.01 | -0.86% | $7,431.19 | $10,007.62 | $-91.75 | $5.76 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,561.30 | -4.39% | $4,762.78 | $10,009.55 | $-391.29 | $-47.41 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $347.90 | $338.97 | $329.50 | 72.5 | 1.43% | $351.68 | 1.68 | +0 |
| NVDA | $212.85 | $225.66 | $222.54 | 23.1 | -1.95% | $243.34 | -1.53 | +1 |
| AMD | $523.73 | $587.20 | $542.26 | 26.4 | -2.62% | $658.45 | -1.46 | +0 |
| MSFT | $524.06 | $526.63 | $508.39 | 48.3 | -1.80% | $551.08 | -0.25 | +0 |

## Actions this run

- BOT_B BUY AMD @ 523.99 — Dip / Mean Reversion entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
