# Paper Bot Lab — Latest Report

Updated: 2026-10-19T13:53:36.103895-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,006.60 | 0.07% | $7,996.35 | $10,046.82 | $-4.57 | $11.17 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,922.94 | -0.77% | $7,455.20 | $10,007.62 | $-59.73 | $-17.33 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,778.09 | -2.22% | $4,910.94 | $10,009.55 | $-178.74 | $-43.16 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,718.94 | -2.81% | $7,200.12 | $10,000.00 | $-299.88 | $18.82 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.82 | $337.64 | $326.30 | 71.0 | 0.44% | $348.11 | 1.24 | +1 |
| NVDA | $217.17 | $227.70 | $222.96 | 38.3 | -4.96% | $243.34 | -1.58 | +0 |
| AMD | $548.10 | $606.57 | $538.23 | 32.6 | -9.48% | $658.45 | -1.82 | +1 |
| MSFT | $533.29 | $521.81 | $506.20 | 65.7 | -1.88% | $551.08 | 0.82 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
