# Paper Bot Lab — Latest Report

Updated: 2026-10-20T13:03:16.525068-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,993.06 | -0.07% | $7,996.35 | $10,046.82 | $-4.57 | $-2.38 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,738.56 | -2.61% | $4,910.94 | $10,009.55 | $-178.74 | $-82.70 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,708.76 | -2.91% | $7,200.12 | $10,000.00 | $-299.88 | $8.64 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $340.51 | $337.68 | $326.95 | 61.9 | -0.73% | $348.11 | 0.67 | -1 |
| NVDA | $217.01 | $227.11 | $222.95 | 36.9 | -2.02% | $243.34 | -1.43 | -2 |
| AMD | $539.50 | $602.30 | $539.61 | 31.5 | -5.51% | $658.45 | -1.79 | +2 |
| MSFT | $531.13 | $523.51 | $506.71 | 62.4 | -0.54% | $551.08 | 0.58 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
