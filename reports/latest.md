# Paper Bot Lab — Latest Report

Updated: 2026-10-14T10:58:23.162520-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,017.39 | 0.17% | $7,996.35 | $10,046.82 | $-4.57 | $21.96 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,744.30 | -2.56% | $7,200.12 | $10,000.00 | $-299.88 | $44.19 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.66 | $336.91 | $324.51 | 59.5 | 1.24% | $348.11 | 2.04 | -1 |
| NVDA | $224.19 | $228.85 | $223.28 | 49.5 | -2.76% | $243.34 | -0.90 | -2 |
| AMD | $584.25 | $611.73 | $534.97 | 35.6 | -5.89% | $658.45 | -1.09 | +1 |
| MSFT | $538.65 | $516.57 | $504.00 | 75.9 | 3.05% | $551.08 | 1.42 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
