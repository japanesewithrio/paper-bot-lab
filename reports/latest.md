# Paper Bot Lab — Latest Report

Updated: 2026-10-22T15:58:34.370116-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,037.36 | 0.37% | $7,996.35 | $10,046.82 | $-4.57 | $41.92 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,915.18 | -0.85% | $7,431.19 | $10,007.62 | $-91.75 | $6.93 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,552.82 | -4.47% | $7,153.40 | $10,009.55 | $-391.29 | $-55.90 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $348.06 | $338.61 | $328.64 | 71.7 | 1.36% | $348.28 | 1.93 | +2 |
| NVDA | $211.99 | $226.26 | $222.79 | 29.4 | -1.00% | $243.34 | -1.82 | +0 |
| AMD | $507.21 | $592.89 | $541.59 | 23.6 | -4.08% | $658.45 | -2.08 | +2 |
| MSFT | $520.88 | $526.28 | $507.86 | 52.0 | -1.53% | $551.08 | -0.52 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
