# Paper Bot Lab — Latest Report

Updated: 2026-11-05T15:25:13.626473-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,931.02 | -0.69% | $7,945.61 | $10,051.61 | $-67.99 | $-0.99 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,780.68 | -2.19% | $9,780.68 | $10,007.62 | $-219.32 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,223.71 | -7.76% | $6,918.65 | $10,009.55 | $-775.14 | $-1.15 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.87 | $343.20 | $335.51 | 51.5 | 0.03% | $355.29 | 0.39 | +2 |
| NVDA | $183.41 | $213.79 | $220.69 | 28.0 | -10.43% | $233.89 | -2.90 | +1 |
| AMD | $413.48 | $535.78 | $547.58 | 33.9 | -18.16% | $626.98 | -2.57 | -1 |
| MSFT | $535.22 | $531.74 | $516.15 | 52.6 | 2.54% | $559.12 | 0.36 | -2 |

## Actions this run

- BOT_B SELL AMD @ 413.27 — stop -7%
- BOT_C SELL MSFT @ 534.95 — negative news
- BOT_B BUY NVDA @ 183.50 — Dip / Mean Reversion entry rule satisfied
- BOT_D BUY AAPL @ 345.04 — Conservative Confirmation entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
