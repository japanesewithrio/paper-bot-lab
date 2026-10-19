# Paper Bot Lab — Latest Report

Updated: 2026-10-19T15:58:46.047072-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,007.69 | 0.08% | $7,996.35 | $10,046.82 | $-4.57 | $12.25 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,924.27 | -0.76% | $7,455.20 | $10,007.62 | $-59.73 | $-16.00 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,719.98 | -2.80% | $7,200.12 | $10,000.00 | $-299.88 | $19.86 | MSFT |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,717.77 | -2.82% | $4,910.94 | $10,009.55 | $-178.74 | $-103.49 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.00 | $337.65 | $326.31 | 71.7 | 0.49% | $348.11 | 1.27 | +1 |
| NVDA | $217.22 | $227.71 | $222.97 | 38.9 | -4.94% | $243.34 | -1.58 | +2 |
| AMD | $534.23 | $606.60 | $538.24 | 32.8 | -11.77% | $658.45 | -2.26 | +1 |
| MSFT | $533.50 | $521.81 | $506.20 | 65.7 | -1.84% | $551.08 | 0.83 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
