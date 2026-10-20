# Paper Bot Lab — Latest Report

Updated: 2026-10-20T15:07:15.054146-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,986.90 | -0.13% | $7,996.35 | $10,046.82 | $-4.57 | $-8.53 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,750.81 | -2.49% | $4,910.94 | $10,009.55 | $-178.74 | $-70.45 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,717.78 | -2.82% | $7,200.12 | $10,000.00 | $-299.88 | $17.66 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.46 | $337.63 | $326.93 | 60.1 | -1.03% | $348.11 | 0.44 | -2 |
| NVDA | $216.83 | $227.10 | $222.95 | 36.7 | -2.10% | $243.34 | -1.46 | +0 |
| AMD | $542.75 | $602.30 | $539.61 | 31.5 | -4.94% | $658.45 | -1.70 | +2 |
| MSFT | $533.04 | $523.52 | $506.72 | 62.6 | -0.19% | $551.08 | 0.73 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
