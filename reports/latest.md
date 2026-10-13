# Paper Bot Lab — Latest Report

Updated: 2026-10-13T15:21:15.436058-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,999.98 | -0.00% | $7,996.35 | $10,046.82 | $-4.57 | $4.54 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,776.09 | -2.24% | $7,200.12 | $10,000.00 | $-299.88 | $75.97 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.69 | $336.32 | $323.81 | 55.4 | 1.52% | $348.11 | 1.54 | -1 |
| NVDA | $227.89 | $228.30 | $223.02 | 53.4 | -4.01% | $243.34 | -0.07 | +1 |
| AMD | $589.10 | $607.86 | $533.68 | 44.4 | -8.79% | $658.45 | -0.57 | +1 |
| MSFT | $545.38 | $514.25 | $503.12 | 78.1 | 2.96% | $551.08 | 1.96 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
