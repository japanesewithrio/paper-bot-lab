# Paper Bot Lab — Latest Report

Updated: 2026-10-07T15:08:23.168802-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,019.96 | 0.20% | $8,000.00 | $10,019.96 | $0.00 | $19.96 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $10,001.71 | 0.02% | $4,991.15 | $10,007.62 | $-8.85 | $10.56 | AAPL, AMD |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,964.66 | -0.35% | $2,500.00 | $10,000.00 | $0.00 | $-35.34 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $336.96 | $334.52 | $322.30 | 50.0 | 1.97% | $345.28 | 0.68 | +2 |
| NVDA | $236.56 | $225.53 | $220.57 | 75.1 | 2.39% | $243.34 | 1.36 | -1 |
| AMD | $645.68 | $587.42 | $522.64 | 76.8 | 4.86% | $658.45 | 1.11 | +2 |
| MSFT | $530.79 | $506.63 | $496.15 | 73.5 | 3.53% | $535.69 | 2.01 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
