# Paper Bot Lab — Latest Report

Updated: 2026-10-22T09:34:34.574773-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,025.10 | 0.25% | $7,996.35 | $10,046.82 | $-4.57 | $29.67 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,708.27 | -2.92% | $7,200.12 | $10,000.00 | $-299.88 | $8.15 | MSFT |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,624.18 | -3.76% | $7,153.40 | $10,009.55 | $-391.29 | $15.47 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.98 | $338.48 | $328.59 | 69.4 | 0.75% | $348.11 | 1.60 | +1 |
| NVDA | $218.30 | $226.57 | $222.91 | 33.2 | 1.95% | $243.34 | -1.12 | -1 |
| AMD | $510.43 | $593.61 | $541.87 | 25.1 | -3.47% | $658.45 | -2.09 | +2 |
| MSFT | $531.02 | $526.81 | $508.08 | 59.6 | 0.38% | $551.08 | 0.41 | -1 |

## Actions this run

- BOT_B SELL AMD @ 510.17 — stop -7%

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
