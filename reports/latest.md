# Paper Bot Lab — Latest Report

Updated: 2026-10-14T14:00:05.306645-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,001.47 | 0.01% | $7,996.35 | $10,046.82 | $-4.57 | $6.04 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,993.91 | -0.06% | $7,500.00 | $10,009.55 | $0.00 | $-6.09 | AMD |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,729.52 | -2.70% | $7,200.12 | $10,000.00 | $-299.88 | $29.40 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.94 | $336.77 | $324.45 | 56.9 | 0.45% | $348.11 | 1.46 | -1 |
| NVDA | $221.07 | $228.67 | $223.21 | 45.1 | -4.12% | $243.34 | -1.42 | +3 |
| AMD | $579.88 | $611.09 | $534.72 | 33.0 | -6.60% | $658.45 | -1.20 | +2 |
| MSFT | $535.53 | $516.38 | $503.93 | 72.5 | 2.45% | $551.08 | 1.25 | -2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
