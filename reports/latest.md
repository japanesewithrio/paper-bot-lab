# Paper Bot Lab — Latest Report

Updated: 2026-10-23T09:30:22.498076-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,051.61 | 0.52% | $7,996.35 | $10,051.61 | $-4.57 | $56.17 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,932.53 | -0.67% | $7,431.19 | $10,007.62 | $-91.75 | $24.28 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,534.20 | -4.66% | $7,153.40 | $10,009.55 | $-391.29 | $-74.51 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $350.50 | $338.62 | $328.64 | 71.8 | 2.07% | $348.34 | 2.42 | +0 |
| NVDA | $210.34 | $226.28 | $222.79 | 29.5 | -1.77% | $243.34 | -2.03 | +1 |
| AMD | $522.25 | $592.89 | $541.59 | 23.6 | -1.23% | $658.45 | -1.72 | +0 |
| MSFT | $518.24 | $526.32 | $507.88 | 52.6 | -2.03% | $551.08 | -0.78 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
