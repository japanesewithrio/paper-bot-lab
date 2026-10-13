# Paper Bot Lab — Latest Report

Updated: 2026-10-13T14:52:41.020417-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,003.58 | 0.04% | $7,996.35 | $10,046.82 | $-4.57 | $8.15 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,780.84 | -2.19% | $7,200.12 | $10,000.00 | $-299.88 | $80.72 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.31 | $336.36 | $323.83 | 56.3 | 1.70% | $348.11 | 1.67 | -1 |
| NVDA | $227.28 | $228.26 | $223.01 | 52.3 | -4.26% | $243.34 | -0.16 | +1 |
| AMD | $596.34 | $607.72 | $533.62 | 43.3 | -7.67% | $658.45 | -0.35 | +1 |
| MSFT | $546.39 | $514.28 | $503.13 | 78.3 | 3.15% | $551.08 | 2.02 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
