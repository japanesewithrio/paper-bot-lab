# Paper Bot Lab — Latest Report

Updated: 2026-10-13T10:47:53.410387-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,025.46 | 0.25% | $7,996.35 | $10,046.82 | $-4.57 | $30.02 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,977.40 | -0.23% | $4,937.89 | $10,007.62 | $-103.46 | $80.86 | AAPL, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,793.35 | -2.07% | $7,200.12 | $10,000.00 | $-299.88 | $93.24 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $346.03 | $336.54 | $323.90 | 59.5 | 2.81% | $348.11 | 2.41 | +1 |
| NVDA | $225.77 | $228.19 | $222.98 | 50.0 | -4.90% | $243.34 | -0.40 | +2 |
| AMD | $588.73 | $607.49 | $533.53 | 41.8 | -8.85% | $658.45 | -0.57 | +1 |
| MSFT | $549.04 | $514.39 | $503.18 | 78.9 | 3.65% | $551.08 | 2.15 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
