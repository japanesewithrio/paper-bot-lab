# Paper Bot Lab — Latest Report

Updated: 2026-11-04T15:11:31.207363-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,932.01 | -0.68% | $9,932.01 | $10,051.61 | $-67.99 | $0.00 | — |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,882.86 | -1.17% | $7,413.07 | $10,007.62 | $-115.90 | $-1.23 | MSFT |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,554.00 | -4.46% | $7,223.97 | $10,009.55 | $-368.03 | $-77.97 | AMD |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $352.00 | $343.07 | $334.93 | 57.6 | 0.87% | $354.47 | 1.98 | -1 |
| NVDA | $202.40 | $216.25 | $221.26 | 36.0 | -5.29% | $237.05 | -1.67 | +0 |
| AMD | $481.25 | $545.67 | $548.73 | 36.9 | -15.05% | $643.44 | -1.50 | +3 |
| MSFT | $558.04 | $531.17 | $515.40 | 57.8 | 5.21% | $558.35 | 2.66 | +2 |

## Actions this run

- BOT_C BUY MSFT @ 558.32 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
