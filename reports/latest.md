# Paper Bot Lab — Latest Report

Updated: 2026-10-14T15:57:56.018247-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,002.88 | 0.03% | $7,996.35 | $10,046.82 | $-4.57 | $7.44 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,940.69 | -0.59% | $7,500.00 | $10,009.55 | $0.00 | $-59.31 | AMD |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,718.33 | -2.82% | $7,200.12 | $10,000.00 | $-299.88 | $18.21 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.19 | $336.82 | $324.47 | 57.8 | 0.52% | $348.11 | 1.48 | +0 |
| NVDA | $221.15 | $228.69 | $223.22 | 45.7 | -4.09% | $243.34 | -1.42 | +3 |
| AMD | $567.50 | $611.10 | $534.72 | 33.0 | -8.59% | $658.45 | -1.67 | +2 |
| MSFT | $533.15 | $516.27 | $503.88 | 70.6 | 2.00% | $551.08 | 1.11 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
