# Paper Bot Lab — Latest Report

Updated: 2026-10-13T11:45:59.275993-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,021.56 | 0.22% | $7,996.35 | $10,046.82 | $-4.57 | $26.12 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,955.74 | -0.44% | $4,937.89 | $10,007.62 | $-103.46 | $59.20 | AAPL, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,776.12 | -2.24% | $7,200.12 | $10,000.00 | $-299.88 | $76.00 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.37 | $336.48 | $323.87 | 58.4 | 2.61% | $348.11 | 2.34 | +0 |
| NVDA | $225.05 | $228.16 | $222.97 | 49.1 | -5.20% | $243.34 | -0.51 | +2 |
| AMD | $583.22 | $607.30 | $533.46 | 40.7 | -9.70% | $658.45 | -0.73 | +1 |
| MSFT | $545.39 | $514.26 | $503.12 | 78.1 | 2.96% | $551.08 | 1.96 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
