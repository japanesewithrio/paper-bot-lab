# Paper Bot Lab — Latest Report

Updated: 2026-10-20T10:23:00.541173-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,002.23 | 0.02% | $7,996.35 | $10,046.82 | $-4.57 | $6.80 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,917.57 | -0.82% | $7,455.20 | $10,007.62 | $-59.73 | $-22.69 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,711.60 | -2.88% | $7,200.12 | $10,000.00 | $-299.88 | $11.48 | MSFT |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,705.86 | -2.94% | $4,910.94 | $10,009.55 | $-178.74 | $-115.40 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.08 | $337.77 | $326.99 | 65.8 | -0.27% | $348.11 | 1.01 | +1 |
| NVDA | $217.34 | $227.13 | $222.96 | 37.3 | -1.87% | $243.34 | -1.40 | +0 |
| AMD | $531.21 | $602.39 | $539.65 | 32.1 | -6.96% | $658.45 | -2.04 | +2 |
| MSFT | $531.73 | $523.47 | $506.70 | 61.8 | -0.43% | $551.08 | 0.63 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
