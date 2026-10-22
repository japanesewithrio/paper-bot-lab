# Paper Bot Lab — Latest Report

Updated: 2026-10-22T15:07:18.938262-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,033.64 | 0.34% | $7,996.35 | $10,046.82 | $-4.57 | $38.20 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,910.65 | -0.89% | $7,431.19 | $10,007.62 | $-91.75 | $2.40 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,550.67 | -4.49% | $7,153.40 | $10,009.55 | $-391.29 | $-58.05 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $347.43 | $338.56 | $328.62 | 70.9 | 1.18% | $348.11 | 1.84 | +2 |
| NVDA | $211.80 | $226.25 | $222.78 | 29.2 | -1.09% | $243.34 | -1.83 | +0 |
| AMD | $502.85 | $592.77 | $541.54 | 23.3 | -4.90% | $658.45 | -2.17 | +2 |
| MSFT | $520.67 | $526.31 | $507.87 | 52.4 | -1.57% | $551.08 | -0.54 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
