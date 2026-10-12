# Paper Bot Lab — Latest Report

Updated: 2026-10-12T10:17:39.376392-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,915.45 | -0.85% | $7,428.79 | $10,007.62 | $-103.46 | $18.91 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,745.20 | -2.55% | $7,200.12 | $10,000.00 | $-299.88 | $45.08 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.56 | $335.84 | $323.06 | 52.1 | 2.35% | $345.28 | 1.64 | -1 |
| NVDA | $225.47 | $227.46 | $222.58 | 45.2 | -5.73% | $243.34 | -0.29 | +1 |
| AMD | $597.04 | $603.09 | $531.37 | 39.8 | -8.08% | $658.45 | -0.15 | +2 |
| MSFT | $538.85 | $511.69 | $501.91 | 76.8 | 1.79% | $542.06 | 1.90 | +1 |

## Actions this run

- BOT_A SELL NVDA @ 225.36 — price<SMA20

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
