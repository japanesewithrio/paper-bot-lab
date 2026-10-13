# Paper Bot Lab — Latest Report

Updated: 2026-10-13T14:10:40.649957-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,006.75 | 0.07% | $7,996.35 | $10,046.82 | $-4.57 | $11.32 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,784.71 | -2.15% | $7,200.12 | $10,000.00 | $-299.88 | $84.59 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.85 | $336.36 | $323.83 | 56.2 | 1.86% | $348.11 | 1.82 | -1 |
| NVDA | $227.44 | $228.28 | $223.02 | 52.9 | -4.19% | $243.34 | -0.14 | +1 |
| AMD | $595.77 | $607.79 | $533.65 | 43.9 | -7.76% | $658.45 | -0.37 | +1 |
| MSFT | $547.21 | $514.31 | $503.14 | 78.4 | 3.31% | $551.08 | 2.06 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
