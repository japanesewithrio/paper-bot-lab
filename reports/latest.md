# Paper Bot Lab — Latest Report

Updated: 2026-10-13T09:49:54.809199-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,012.38 | 0.12% | $7,996.35 | $10,046.82 | $-4.57 | $16.94 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,962.39 | -0.38% | $4,937.89 | $10,007.62 | $-103.46 | $65.84 | AAPL, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,794.51 | -2.05% | $7,200.12 | $10,000.00 | $-299.88 | $94.39 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.81 | $336.40 | $323.84 | 57.1 | 2.15% | $348.11 | 2.04 | +1 |
| NVDA | $224.88 | $228.14 | $222.96 | 48.6 | -5.28% | $243.34 | -0.54 | +2 |
| AMD | $596.71 | $607.27 | $533.45 | 40.5 | -7.62% | $658.45 | -0.32 | +1 |
| MSFT | $549.29 | $514.45 | $503.20 | 79.2 | 3.70% | $551.01 | 2.14 | +1 |

## Actions this run

- BOT_C BUY AAPL @ 343.98 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
