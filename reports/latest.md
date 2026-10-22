# Paper Bot Lab — Latest Report

Updated: 2026-10-22T13:56:41.264365-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,025.07 | 0.25% | $7,996.35 | $10,046.82 | $-4.57 | $29.64 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,557.18 | -4.43% | $7,153.40 | $10,009.55 | $-391.29 | $-51.54 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.97 | $338.50 | $328.60 | 69.7 | 0.75% | $348.11 | 1.59 | +2 |
| NVDA | $212.38 | $226.30 | $222.80 | 29.8 | -0.82% | $243.34 | -1.79 | +3 |
| AMD | $508.68 | $593.02 | $541.64 | 23.8 | -3.80% | $658.45 | -2.06 | +2 |
| MSFT | $523.49 | $526.44 | $507.93 | 54.1 | -1.04% | $551.08 | -0.29 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
