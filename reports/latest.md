# Paper Bot Lab — Latest Report

Updated: 2026-10-16T12:21:53.294261-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,018.65 | 0.19% | $7,996.35 | $10,046.82 | $-4.57 | $23.22 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,937.73 | -0.62% | $7,455.20 | $10,007.62 | $-59.73 | $-2.54 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,814.27 | -1.86% | $4,910.94 | $10,009.55 | $-178.74 | $-6.99 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,707.04 | -2.93% | $7,200.12 | $10,000.00 | $-299.88 | $6.92 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.88 | $337.53 | $325.74 | 57.9 | 1.12% | $348.11 | 1.77 | +2 |
| NVDA | $217.39 | $228.38 | $223.16 | 35.5 | -4.01% | $243.34 | -1.88 | -1 |
| AMD | $555.75 | $611.09 | $537.40 | 31.3 | -6.49% | $658.45 | -2.11 | +1 |
| MSFT | $530.76 | $520.21 | $505.52 | 63.2 | -1.91% | $551.08 | 0.73 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
