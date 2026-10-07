# Paper Bot Lab — Latest Report

Updated: 2026-10-07T14:45:48.679617-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,016.79 | 0.17% | $8,000.00 | $10,019.90 | $0.00 | $16.79 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $10,002.99 | 0.03% | $4,991.15 | $10,007.62 | $-8.85 | $11.84 | AAPL, AMD |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,973.44 | -0.27% | $2,500.00 | $10,000.00 | $0.00 | $-26.56 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $336.43 | $334.49 | $322.28 | 49.2 | 1.81% | $345.28 | 0.54 | +2 |
| NVDA | $236.85 | $225.55 | $220.58 | 75.7 | 2.51% | $243.34 | 1.39 | -1 |
| AMD | $647.05 | $587.62 | $522.72 | 78.6 | 5.08% | $658.45 | 1.12 | +2 |
| MSFT | $530.90 | $506.63 | $496.15 | 73.6 | 3.55% | $535.69 | 2.02 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
