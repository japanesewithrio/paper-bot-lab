# Paper Bot Lab — Latest Report

Updated: 2026-10-14T13:28:19.877111-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,004.02 | 0.04% | $7,996.35 | $10,046.82 | $-4.57 | $8.59 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,955.74 | -0.44% | $7,500.00 | $10,009.55 | $0.00 | $-44.26 | AMD |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,728.81 | -2.71% | $7,200.12 | $10,000.00 | $-299.88 | $28.69 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.38 | $336.81 | $324.47 | 57.6 | 0.57% | $348.11 | 1.54 | -1 |
| NVDA | $221.37 | $228.71 | $223.23 | 46.1 | -3.99% | $243.34 | -1.39 | +3 |
| AMD | $571.00 | $611.13 | $534.73 | 33.1 | -8.03% | $658.45 | -1.54 | +1 |
| MSFT | $535.38 | $516.39 | $503.93 | 72.7 | 2.42% | $551.08 | 1.24 | -2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
