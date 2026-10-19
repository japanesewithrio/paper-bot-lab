# Paper Bot Lab — Latest Report

Updated: 2026-10-19T13:01:03.688997-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,999.74 | -0.00% | $7,996.35 | $10,046.82 | $-4.57 | $4.31 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,914.52 | -0.85% | $7,455.20 | $10,007.62 | $-59.73 | $-25.75 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,835.49 | -1.65% | $4,910.94 | $10,009.55 | $-178.74 | $14.23 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,718.59 | -2.81% | $7,200.12 | $10,000.00 | $-299.88 | $18.47 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.65 | $337.58 | $326.28 | 68.6 | 0.09% | $348.11 | 0.99 | +1 |
| NVDA | $218.00 | $227.74 | $222.98 | 39.6 | -4.60% | $243.34 | -1.48 | +1 |
| AMD | $559.01 | $606.78 | $538.32 | 34.0 | -7.67% | $658.45 | -1.51 | +1 |
| MSFT | $533.21 | $521.78 | $506.19 | 65.5 | -1.90% | $551.08 | 0.82 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
