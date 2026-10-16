# Paper Bot Lab — Latest Report

Updated: 2026-10-16T15:00:36.135073-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,999.33 | -0.01% | $7,996.35 | $10,046.82 | $-4.57 | $3.90 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,914.01 | -0.86% | $7,455.20 | $10,007.62 | $-59.73 | $-26.26 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,704.44 | -2.96% | $4,910.94 | $10,009.55 | $-178.74 | $-116.82 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,687.04 | -3.13% | $7,200.12 | $10,000.00 | $-299.88 | $-13.08 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.58 | $337.35 | $325.67 | 53.7 | 0.16% | $348.11 | 1.09 | +2 |
| NVDA | $213.81 | $228.20 | $223.09 | 32.5 | -5.59% | $243.34 | -2.31 | -2 |
| AMD | $539.99 | $610.60 | $537.20 | 29.6 | -9.14% | $658.45 | -2.56 | +0 |
| MSFT | $526.53 | $520.07 | $505.47 | 60.9 | -2.69% | $551.08 | 0.45 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
