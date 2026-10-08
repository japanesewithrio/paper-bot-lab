# Paper Bot Lab — Latest Report

Updated: 2026-10-08T13:07:56.413324-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,031.68 | 0.32% | $8,000.00 | $10,031.68 | $0.00 | $31.68 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,920.78 | -0.79% | $4,991.29 | $10,007.62 | $-8.71 | $-70.52 | AAPL, AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,787.32 | -2.13% | $2,500.00 | $10,000.00 | $0.00 | $-212.68 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $338.91 | $335.13 | $322.31 | 54.3 | 1.55% | $345.28 | 1.17 | +1 |
| NVDA | $232.06 | $226.24 | $221.42 | 63.1 | -0.83% | $243.34 | 0.72 | +0 |
| AMD | $620.82 | $593.47 | $526.55 | 66.3 | -2.04% | $658.45 | 0.55 | +3 |
| MSFT | $523.46 | $508.13 | $498.78 | 71.5 | 1.19% | $535.69 | 1.28 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
