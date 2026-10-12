# Paper Bot Lab — Latest Report

Updated: 2026-10-12T09:57:18.907379-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,915.17 | -0.85% | $7,428.79 | $10,007.62 | $-103.46 | $18.63 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,768.62 | -2.31% | $4,845.19 | $10,000.00 | $-154.81 | $-76.57 | MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $340.67 | $335.78 | $323.04 | 51.0 | 2.08% | $345.28 | 1.44 | -1 |
| NVDA | $227.62 | $227.57 | $222.62 | 48.2 | -4.83% | $243.34 | 0.01 | +1 |
| AMD | $594.32 | $603.27 | $531.44 | 40.8 | -8.50% | $658.45 | -0.22 | +2 |
| MSFT | $538.78 | $511.76 | $501.93 | 77.2 | 1.78% | $542.06 | 1.88 | +1 |

## Actions this run

- BOT_C SELL AAPL @ 340.50 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
