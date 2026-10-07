# Paper Bot Lab — Latest Report

Updated: 2026-10-07T15:39:46.042872-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,012.92 | 0.13% | $8,000.00 | $10,019.96 | $0.00 | $12.92 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $10,001.35 | 0.01% | $4,991.15 | $10,007.62 | $-8.85 | $10.20 | AAPL, AMD |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,969.90 | -0.30% | $2,500.00 | $10,000.00 | $0.00 | $-30.10 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $335.78 | $334.45 | $322.27 | 48.1 | 1.62% | $345.28 | 0.38 | +2 |
| NVDA | $236.94 | $225.55 | $220.58 | 75.9 | 2.55% | $243.34 | 1.40 | -1 |
| AMD | $647.88 | $587.64 | $522.73 | 78.8 | 5.21% | $658.45 | 1.14 | +3 |
| MSFT | $529.28 | $506.54 | $496.12 | 72.7 | 3.23% | $535.69 | 1.92 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
