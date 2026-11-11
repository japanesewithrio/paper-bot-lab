# Paper Bot Lab — Latest Report

Updated: 2026-11-11T14:57:04.412350-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,921.07 | -0.79% | $7,937.65 | $10,051.61 | $-77.94 | $-0.99 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,778.24 | -2.22% | $4,890.65 | $10,007.62 | $-219.32 | $-2.44 | AAPL, AMD |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,016.49 | -9.84% | $6,763.21 | $10,009.55 | $-982.38 | $-1.13 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $354.75 | $344.87 | $337.89 | 54.3 | 2.95% | $355.33 | 2.05 | +2 |
| NVDA | $175.65 | $203.90 | $217.17 | 27.9 | -3.27% | $222.18 | -1.77 | +1 |
| AMD | $559.28 | $517.78 | $550.50 | 55.7 | 38.63% | $578.89 | 0.97 | +2 |
| MSFT | $520.41 | $530.56 | $518.22 | 49.6 | -2.96% | $559.12 | -1.03 | -1 |

## Actions this run

- BOT_B BUY NVDA @ 175.74 — Dip / Mean Reversion entry rule satisfied
- BOT_C BUY AAPL @ 354.93 — News + Momentum entry rule satisfied
- BOT_C BUY AMD @ 559.56 — News + Momentum entry rule satisfied
- BOT_D BUY AAPL @ 354.93 — Conservative Confirmation entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
