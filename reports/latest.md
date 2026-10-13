# Paper Bot Lab — Latest Report

Updated: 2026-10-13T10:12:27.665451-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,024.11 | 0.24% | $7,996.35 | $10,046.82 | $-4.57 | $28.67 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,974.45 | -0.26% | $4,937.89 | $10,007.62 | $-103.46 | $77.90 | AAPL, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,792.03 | -2.08% | $7,200.12 | $10,000.00 | $-299.88 | $91.91 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.81 | $336.51 | $323.89 | 58.9 | 2.74% | $348.11 | 2.41 | +1 |
| NVDA | $226.38 | $228.22 | $222.99 | 51.1 | -4.64% | $243.34 | -0.31 | +2 |
| AMD | $591.32 | $607.46 | $533.52 | 41.6 | -8.45% | $658.45 | -0.49 | +1 |
| MSFT | $548.76 | $514.42 | $503.19 | 79.0 | 3.60% | $551.08 | 2.12 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
