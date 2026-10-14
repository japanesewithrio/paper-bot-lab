# Paper Bot Lab — Latest Report

Updated: 2026-10-14T15:24:34.369435-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,008.54 | 0.09% | $7,996.35 | $10,046.82 | $-4.57 | $13.10 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,974.67 | -0.25% | $7,500.00 | $10,009.55 | $0.00 | $-25.33 | AMD |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,722.41 | -2.78% | $7,200.12 | $10,000.00 | $-299.88 | $22.29 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.15 | $336.83 | $324.48 | 58.1 | 0.80% | $348.11 | 1.73 | -1 |
| NVDA | $221.13 | $228.69 | $223.22 | 45.5 | -4.09% | $243.34 | -1.42 | +3 |
| AMD | $575.40 | $611.12 | $534.73 | 33.1 | -7.32% | $658.45 | -1.37 | +2 |
| MSFT | $534.02 | $516.33 | $503.91 | 71.6 | 2.16% | $551.08 | 1.16 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
