# Paper Bot Lab — Latest Report

Updated: 2026-11-13T15:12:15.489625-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,933.45 | -0.67% | $7,937.65 | $10,051.61 | $-77.94 | $11.39 | AAPL |
| 2 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,666.97 | -3.33% | $7,336.95 | $10,007.62 | $-218.18 | $-114.84 | AMD |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $8,856.03 | -11.44% | $6,642.86 | $10,009.55 | $-1,142.86 | $-1.11 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $356.97 | $346.25 | $339.08 | 58.8 | 1.84% | $360.81 | 1.83 | +0 |
| NVDA | $162.93 | $198.70 | $214.66 | 19.1 | -8.79% | $222.18 | -1.85 | +0 |
| AMD | $533.28 | $518.92 | $554.52 | 50.3 | 4.84% | $593.93 | 0.33 | +1 |
| MSFT | $524.37 | $529.53 | $519.04 | 47.2 | -3.82% | $559.12 | -0.52 | -1 |

## Actions this run

- BOT_B BUY NVDA @ 163.01 — Dip / Mean Reversion entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
