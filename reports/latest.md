# Paper Bot Lab — Latest Report

Updated: 2026-10-07T09:41:32.283616-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,007.01 | 0.07% | $8,000.00 | $10,007.01 | $0.00 | $7.01 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,953.93 | -0.46% | $4,982.35 | $10,000.00 | $-17.65 | $-28.42 | AAPL, AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,935.47 | -0.65% | $2,500.00 | $10,000.00 | $0.00 | $-64.53 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $334.80 | $334.40 | $322.25 | 46.9 | 1.32% | $345.28 | 0.11 | +2 |
| NVDA | $237.67 | $225.60 | $220.60 | 78.3 | 2.87% | $243.34 | 1.47 | -2 |
| AMD | $639.76 | $587.41 | $522.64 | 76.8 | 3.89% | $658.45 | 0.99 | +1 |
| MSFT | $526.98 | $506.46 | $496.09 | 71.1 | 2.78% | $535.69 | 1.75 | +2 |

## Actions this run

- BOT_C SELL NVDA @ 237.55 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
