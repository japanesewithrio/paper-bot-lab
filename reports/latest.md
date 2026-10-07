# Paper Bot Lab — Latest Report

Updated: 2026-10-07T14:07:49.350668-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,019.90 | 0.20% | $8,000.00 | $10,019.90 | $0.00 | $19.90 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $10,007.62 | 0.08% | $4,991.15 | $10,007.62 | $-8.85 | $16.47 | AAPL, AMD |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,973.96 | -0.26% | $2,500.00 | $10,000.00 | $0.00 | $-26.04 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $336.95 | $334.51 | $322.29 | 49.8 | 1.97% | $345.28 | 0.68 | +2 |
| NVDA | $237.19 | $225.56 | $220.59 | 76.5 | 2.66% | $243.34 | 1.43 | -2 |
| AMD | $647.24 | $587.58 | $522.70 | 78.2 | 5.11% | $658.45 | 1.13 | +2 |
| MSFT | $530.12 | $506.59 | $496.14 | 73.2 | 3.39% | $535.69 | 1.97 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
