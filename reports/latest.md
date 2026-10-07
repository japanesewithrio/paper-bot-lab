# Paper Bot Lab — Latest Report

Updated: 2026-10-07T13:41:44.889767-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,016.10 | 0.16% | $8,000.00 | $10,016.10 | $0.00 | $16.10 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,988.89 | -0.11% | $4,991.15 | $10,000.00 | $-8.85 | $-2.27 | AAPL, AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,954.62 | -0.45% | $2,500.00 | $10,000.00 | $0.00 | $-45.38 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $336.31 | $334.47 | $322.28 | 48.7 | 1.78% | $345.28 | 0.52 | +2 |
| NVDA | $237.01 | $225.56 | $220.58 | 76.1 | 2.58% | $243.34 | 1.41 | +0 |
| AMD | $643.61 | $587.56 | $522.69 | 78.0 | 4.52% | $658.45 | 1.06 | +2 |
| MSFT | $529.37 | $506.55 | $496.12 | 72.8 | 3.25% | $535.69 | 1.92 | -2 |

## Actions this run

- BOT_C SELL MSFT @ 529.10 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
