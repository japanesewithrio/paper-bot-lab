# Paper Bot Lab — Latest Report

Updated: 2026-10-13T12:09:57.100000-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,017.16 | 0.17% | $7,996.35 | $10,046.82 | $-4.57 | $21.72 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,952.95 | -0.47% | $7,457.39 | $10,007.62 | $-51.71 | $4.66 | AAPL |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,780.11 | -2.20% | $7,200.12 | $10,000.00 | $-299.88 | $79.99 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.62 | $336.47 | $323.87 | 58.3 | 2.39% | $348.11 | 2.16 | +0 |
| NVDA | $225.98 | $228.20 | $222.98 | 50.4 | -4.81% | $243.34 | -0.37 | +1 |
| AMD | $593.71 | $607.53 | $533.55 | 42.0 | -8.08% | $658.45 | -0.42 | +1 |
| MSFT | $546.24 | $514.29 | $503.14 | 78.3 | 3.12% | $551.08 | 2.00 | -1 |

## Actions this run

- BOT_C SELL MSFT @ 545.96 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
