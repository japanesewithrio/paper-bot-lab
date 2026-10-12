# Paper Bot Lab — Latest Report

Updated: 2026-10-12T11:12:03.686538-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,994.44 | -0.06% | $7,996.35 | $10,046.82 | $-4.57 | $-1.00 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,924.64 | -0.75% | $7,428.79 | $10,007.62 | $-103.46 | $28.09 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,754.60 | -2.45% | $7,200.12 | $10,000.00 | $-299.88 | $54.48 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $340.75 | $335.78 | $323.04 | 50.9 | 2.11% | $345.28 | 1.46 | +0 |
| NVDA | $225.89 | $227.49 | $222.59 | 45.8 | -5.55% | $243.34 | -0.23 | +1 |
| AMD | $586.66 | $602.81 | $531.26 | 38.4 | -9.68% | $658.45 | -0.40 | +2 |
| MSFT | $540.84 | $511.81 | $501.96 | 77.5 | 2.16% | $542.06 | 2.00 | +2 |

## Actions this run

- BOT_D BUY AAPL @ 340.92 — Conservative Confirmation entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
