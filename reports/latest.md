# Paper Bot Lab — Latest Report

Updated: 2026-10-14T10:00:40.511955-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,023.32 | 0.23% | $7,996.35 | $10,046.82 | $-4.57 | $27.88 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,757.67 | -2.42% | $7,200.12 | $10,000.00 | $-299.88 | $57.55 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.67 | $336.95 | $324.53 | 60.2 | 1.54% | $348.11 | 2.25 | +0 |
| NVDA | $224.50 | $228.85 | $223.28 | 49.7 | -2.63% | $243.34 | -0.85 | -2 |
| AMD | $585.73 | $611.88 | $535.03 | 36.3 | -5.65% | $658.45 | -1.04 | +1 |
| MSFT | $541.49 | $516.73 | $504.07 | 79.1 | 3.59% | $551.08 | 1.57 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
