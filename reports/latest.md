# Paper Bot Lab — Latest Report

Updated: 2026-10-19T09:34:54.086342-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,019.77 | 0.20% | $7,996.35 | $10,046.82 | $-4.57 | $24.33 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,939.10 | -0.61% | $7,455.20 | $10,007.62 | $-59.73 | $-1.17 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,836.14 | -1.64% | $4,910.94 | $10,009.55 | $-178.74 | $14.88 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,710.49 | -2.90% | $7,200.12 | $10,000.00 | $-299.88 | $10.37 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.06 | $337.64 | $326.31 | 71.2 | 1.09% | $348.11 | 1.77 | +1 |
| NVDA | $216.08 | $227.65 | $222.94 | 37.1 | -5.44% | $243.34 | -1.72 | +0 |
| AMD | $564.10 | $607.14 | $538.46 | 36.3 | -6.83% | $658.45 | -1.39 | +0 |
| MSFT | $531.50 | $521.67 | $506.14 | 64.4 | -2.21% | $551.08 | 0.71 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
