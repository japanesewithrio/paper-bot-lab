# Paper Bot Lab — Latest Report

Updated: 2026-10-23T15:53:57.774769-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,034.13 | 0.34% | $7,996.35 | $10,051.61 | $-4.57 | $38.70 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,901.35 | -0.99% | $9,901.35 | $10,007.62 | $-98.65 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,495.72 | -5.04% | $4,762.78 | $10,009.55 | $-391.29 | $-112.99 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $347.51 | $338.94 | $329.49 | 71.5 | 1.32% | $351.68 | 1.63 | +1 |
| NVDA | $211.50 | $225.60 | $222.52 | 21.9 | -2.58% | $243.34 | -1.67 | +2 |
| AMD | $512.70 | $587.14 | $542.24 | 26.1 | -4.67% | $658.45 | -1.71 | +0 |
| MSFT | $523.86 | $526.75 | $508.44 | 49.8 | -1.83% | $551.08 | -0.29 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
