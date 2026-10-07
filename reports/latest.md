# Paper Bot Lab — Latest Report

Updated: 2026-10-07T12:10:05.301779-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,005.69 | 0.06% | $8,000.00 | $10,008.42 | $0.00 | $5.69 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,974.73 | -0.25% | $2,496.50 | $10,000.00 | $-17.65 | $-7.63 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,954.60 | -0.45% | $2,500.00 | $10,000.00 | $0.00 | $-45.40 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $334.58 | $334.40 | $322.25 | 46.8 | 1.25% | $345.28 | 0.05 | +3 |
| NVDA | $237.24 | $225.57 | $220.59 | 76.6 | 2.68% | $243.34 | 1.44 | +3 |
| AMD | $644.45 | $587.57 | $522.70 | 78.1 | 4.66% | $658.45 | 1.08 | +2 |
| MSFT | $528.16 | $506.49 | $496.10 | 71.6 | 3.01% | $535.69 | 1.84 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
