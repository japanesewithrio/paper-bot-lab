# Paper Bot Lab — Latest Report

Updated: 2026-10-22T11:32:41.047018-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,016.22 | 0.16% | $7,996.35 | $10,046.82 | $-4.57 | $20.79 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,566.46 | -4.34% | $7,153.40 | $10,009.55 | $-391.29 | $-42.26 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.46 | $338.42 | $328.56 | 68.1 | 0.31% | $348.11 | 1.31 | +1 |
| NVDA | $213.19 | $226.32 | $222.81 | 30.1 | -0.43% | $243.34 | -1.69 | +1 |
| AMD | $509.41 | $593.00 | $541.63 | 23.8 | -3.66% | $658.45 | -2.04 | +2 |
| MSFT | $524.06 | $526.50 | $507.95 | 54.9 | -0.93% | $551.08 | -0.24 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
