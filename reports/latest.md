# Paper Bot Lab — Latest Report

Updated: 2026-10-13T13:43:18.811774-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,007.89 | 0.08% | $7,996.35 | $10,046.82 | $-4.57 | $12.46 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,782.33 | -2.18% | $7,200.12 | $10,000.00 | $-299.88 | $82.21 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.04 | $336.39 | $323.84 | 56.8 | 1.92% | $348.11 | 1.84 | -1 |
| NVDA | $227.18 | $228.27 | $223.01 | 52.5 | -4.30% | $243.34 | -0.18 | +1 |
| AMD | $595.00 | $607.75 | $533.64 | 43.6 | -7.88% | $658.45 | -0.39 | +1 |
| MSFT | $546.70 | $514.32 | $503.15 | 78.5 | 3.21% | $551.08 | 2.02 | +2 |

## Actions this run

- BOT_C SELL AAPL @ 342.87 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
