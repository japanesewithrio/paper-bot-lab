# Paper Bot Lab — Latest Report

Updated: 2026-10-12T11:45:03.759591-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,988.81 | -0.11% | $7,996.35 | $10,046.82 | $-4.57 | $-6.63 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,932.11 | -0.68% | $7,428.79 | $10,007.62 | $-103.46 | $35.57 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,762.25 | -2.38% | $7,200.12 | $10,000.00 | $-299.88 | $62.13 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.78 | $335.73 | $323.02 | 49.9 | 1.82% | $345.28 | 1.22 | +0 |
| NVDA | $225.99 | $227.49 | $222.59 | 46.0 | -5.51% | $243.34 | -0.22 | +1 |
| AMD | $595.63 | $602.96 | $531.31 | 39.1 | -8.30% | $658.45 | -0.18 | +2 |
| MSFT | $542.45 | $511.89 | $501.99 | 77.9 | 2.47% | $542.70 | 2.08 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
