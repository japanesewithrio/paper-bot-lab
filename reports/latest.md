# Paper Bot Lab — Latest Report

Updated: 2026-10-13T13:08:39.296549-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,012.91 | 0.13% | $7,996.35 | $10,046.82 | $-4.57 | $17.47 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,947.70 | -0.52% | $7,457.39 | $10,007.62 | $-51.71 | $-0.59 | AAPL |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,774.18 | -2.26% | $7,200.12 | $10,000.00 | $-299.88 | $74.06 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.89 | $336.43 | $323.85 | 57.5 | 2.17% | $348.11 | 2.03 | +0 |
| NVDA | $227.36 | $228.27 | $223.01 | 52.5 | -4.23% | $243.34 | -0.15 | +1 |
| AMD | $598.39 | $607.79 | $533.65 | 43.9 | -7.36% | $658.45 | -0.29 | +1 |
| MSFT | $544.98 | $514.25 | $503.12 | 78.1 | 2.88% | $551.08 | 1.94 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
