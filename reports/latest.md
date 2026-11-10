# Paper Bot Lab — Latest Report

Updated: 2026-11-10T15:07:44.223380-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,922.06 | -0.78% | $9,922.06 | $10,051.61 | $-77.94 | $0.00 | — |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,780.68 | -2.19% | $9,780.68 | $10,007.62 | $-219.32 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,017.62 | -9.82% | $9,017.62 | $10,009.55 | $-982.38 | $0.00 | — |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $348.27 | $344.29 | $337.30 | 53.1 | -0.37% | $355.29 | 0.93 | +2 |
| NVDA | $167.10 | $206.08 | $217.96 | 18.5 | -16.52% | $225.97 | -2.54 | -1 |
| AMD | $513.50 | $518.37 | $548.51 | 45.8 | 5.07% | $591.07 | -0.11 | +2 |
| MSFT | $532.90 | $531.20 | $517.82 | 49.9 | -4.17% | $559.12 | 0.18 | +3 |

## Actions this run

- BOT_B SELL NVDA @ 167.01 — stop -7%

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
