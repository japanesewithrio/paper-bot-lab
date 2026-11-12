# Paper Bot Lab — Latest Report

Updated: 2026-11-12T15:34:35.616251-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,923.97 | -0.76% | $7,937.65 | $10,051.61 | $-77.94 | $1.92 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,866.45 | -1.34% | $7,336.95 | $10,007.62 | $-218.18 | $84.63 | AMD |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $8,857.14 | -11.43% | $8,857.14 | $10,009.55 | $-1,142.86 | $0.00 | — |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $355.27 | $345.60 | $338.52 | 55.1 | 3.76% | $359.33 | 1.80 | -1 |
| NVDA | $163.31 | $201.11 | $215.91 | 23.6 | -12.53% | $222.18 | -2.09 | -2 |
| AMD | $578.93 | $518.39 | $552.85 | 57.0 | 29.38% | $593.93 | 1.39 | +2 |
| MSFT | $522.07 | $529.70 | $518.73 | 49.2 | -1.60% | $559.12 | -0.78 | -1 |

## Actions this run

- BOT_B SELL NVDA @ 163.23 — stop -7%
- BOT_C SELL AAPL @ 355.10 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
