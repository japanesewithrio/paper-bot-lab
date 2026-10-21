# Paper Bot Lab — Latest Report

Updated: 2026-10-21T12:59:53.896419-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,014.08 | 0.14% | $7,996.35 | $10,046.82 | $-4.57 | $18.64 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,848.02 | -1.52% | $4,910.94 | $10,009.55 | $-178.74 | $26.77 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,703.68 | -2.96% | $7,200.12 | $10,000.00 | $-299.88 | $3.57 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.10 | $338.00 | $327.72 | 71.0 | 0.64% | $348.11 | 1.38 | +1 |
| NVDA | $220.52 | $226.86 | $223.02 | 39.4 | 1.47% | $243.34 | -0.88 | +2 |
| AMD | $555.37 | $598.95 | $541.09 | 35.1 | -1.21% | $658.45 | -1.18 | +2 |
| MSFT | $530.06 | $525.12 | $507.30 | 63.1 | -1.73% | $551.08 | 0.41 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
