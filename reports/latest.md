# Paper Bot Lab — Latest Report

Updated: 2026-10-16T10:58:16.097004-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,022.00 | 0.22% | $7,996.35 | $10,046.82 | $-4.57 | $26.56 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,941.83 | -0.58% | $7,455.20 | $10,007.62 | $-59.73 | $1.57 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,826.84 | -1.73% | $4,910.94 | $10,009.55 | $-178.74 | $5.58 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,737.81 | -2.62% | $7,200.12 | $10,000.00 | $-299.88 | $37.69 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.44 | $337.56 | $325.76 | 58.5 | 1.29% | $348.11 | 1.87 | +3 |
| NVDA | $217.53 | $228.39 | $223.17 | 35.9 | -3.94% | $243.34 | -1.86 | +0 |
| AMD | $558.25 | $611.21 | $537.44 | 31.7 | -6.07% | $658.45 | -2.04 | +2 |
| MSFT | $537.28 | $520.51 | $505.64 | 68.7 | -0.70% | $551.08 | 1.14 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
