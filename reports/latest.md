# Paper Bot Lab — Latest Report

Updated: 2026-10-08T14:46:02.200884-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,039.71 | 0.40% | $8,000.00 | $10,039.71 | $0.00 | $39.71 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,902.08 | -0.98% | $7,525.80 | $10,007.62 | $25.80 | $-123.73 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,745.27 | -2.55% | $2,500.00 | $10,000.00 | $0.00 | $-254.73 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $340.25 | $335.18 | $322.33 | 55.3 | 1.95% | $345.28 | 1.54 | -2 |
| NVDA | $230.19 | $226.16 | $221.39 | 60.7 | -1.63% | $243.34 | 0.50 | +0 |
| AMD | $617.28 | $593.28 | $526.48 | 65.0 | -2.60% | $658.45 | 0.48 | +1 |
| MSFT | $521.58 | $508.02 | $498.74 | 69.5 | 0.82% | $535.69 | 1.14 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
