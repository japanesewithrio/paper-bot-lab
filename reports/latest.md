# Paper Bot Lab — Latest Report

Updated: 2026-10-13T12:45:04.118863-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,016.92 | 0.17% | $7,996.35 | $10,046.82 | $-4.57 | $21.49 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,952.66 | -0.47% | $7,457.39 | $10,007.62 | $-51.71 | $4.37 | AAPL |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,781.22 | -2.19% | $7,200.12 | $10,000.00 | $-299.88 | $81.10 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.58 | $336.47 | $323.87 | 58.3 | 2.38% | $348.11 | 2.15 | +0 |
| NVDA | $226.64 | $228.24 | $223.00 | 51.6 | -4.53% | $243.34 | -0.26 | +1 |
| AMD | $599.28 | $607.89 | $533.69 | 44.7 | -7.22% | $658.45 | -0.26 | +0 |
| MSFT | $546.47 | $514.28 | $503.13 | 78.3 | 3.17% | $551.08 | 2.02 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
