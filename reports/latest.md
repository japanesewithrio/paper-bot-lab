# Paper Bot Lab — Latest Report

Updated: 2026-10-22T12:59:43.678037-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,023.52 | 0.24% | $7,996.35 | $10,046.82 | $-4.57 | $28.09 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,560.29 | -4.40% | $7,153.40 | $10,009.55 | $-391.29 | $-48.43 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.70 | $338.49 | $328.59 | 69.4 | 0.67% | $348.11 | 1.54 | +2 |
| NVDA | $212.65 | $226.32 | $222.81 | 30.0 | -0.69% | $243.34 | -1.76 | +2 |
| AMD | $515.50 | $593.05 | $541.65 | 23.9 | -2.51% | $658.45 | -1.90 | +2 |
| MSFT | $525.37 | $526.50 | $507.95 | 55.0 | -0.68% | $551.08 | -0.11 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
