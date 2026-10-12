# Paper Bot Lab — Latest Report

Updated: 2026-10-12T13:42:52.004671-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,984.41 | -0.16% | $7,996.35 | $10,046.82 | $-4.57 | $-11.03 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,924.20 | -0.76% | $7,428.79 | $10,007.62 | $-103.46 | $27.66 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,754.15 | -2.46% | $7,200.12 | $10,000.00 | $-299.88 | $54.03 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.03 | $335.72 | $323.01 | 49.5 | 1.59% | $345.28 | 1.00 | +1 |
| NVDA | $226.31 | $227.51 | $222.60 | 46.3 | -5.37% | $243.34 | -0.17 | +2 |
| AMD | $588.39 | $602.92 | $531.30 | 38.9 | -9.41% | $658.45 | -0.36 | +1 |
| MSFT | $540.74 | $511.82 | $501.96 | 77.6 | 2.14% | $542.70 | 1.99 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
