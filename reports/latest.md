# Paper Bot Lab — Latest Report

Updated: 2026-11-03T14:54:45.528042-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,932.01 | -0.68% | $9,932.01 | $10,051.61 | $-67.99 | $0.00 | — |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,884.10 | -1.16% | $9,884.10 | $10,007.62 | $-115.90 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,574.14 | -4.26% | $7,223.97 | $10,009.55 | $-368.03 | $-57.83 | AMD |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $330.26 | $342.25 | $334.06 | 37.4 | -4.01% | $351.68 | -2.76 | +0 |
| NVDA | $206.35 | $218.02 | $221.48 | 36.2 | -4.18% | $239.08 | -1.32 | +0 |
| AMD | $485.41 | $554.02 | $548.74 | 36.7 | -16.08% | $648.31 | -1.51 | -2 |
| MSFT | $521.31 | $529.82 | $514.10 | 42.9 | -2.05% | $551.08 | -1.06 | -2 |

## Actions this run

- BOT_D SELL AAPL @ 330.10 — price<SMA20

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
