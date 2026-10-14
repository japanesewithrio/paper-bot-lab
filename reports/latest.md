# Paper Bot Lab — Latest Report

Updated: 2026-10-14T14:31:46.765174-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,007.89 | 0.08% | $7,996.35 | $10,046.82 | $-4.57 | $12.46 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,962.90 | -0.37% | $7,500.00 | $10,009.55 | $0.00 | $-37.10 | AMD |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,721.96 | -2.78% | $7,200.12 | $10,000.00 | $-299.88 | $21.84 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.04 | $336.83 | $324.48 | 58.0 | 0.77% | $348.11 | 1.71 | -1 |
| NVDA | $220.50 | $228.67 | $223.21 | 45.1 | -4.37% | $243.34 | -1.53 | +3 |
| AMD | $572.66 | $611.17 | $534.75 | 33.3 | -7.76% | $658.45 | -1.48 | +2 |
| MSFT | $533.92 | $516.33 | $503.91 | 71.7 | 2.15% | $551.08 | 1.15 | -2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
