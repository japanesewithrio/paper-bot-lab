# Paper Bot Lab — Latest Report

Updated: 2026-10-07T13:16:10.664718-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,015.20 | 0.15% | $8,000.00 | $10,015.20 | $0.00 | $15.20 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,992.01 | -0.08% | $2,496.50 | $10,000.00 | $-17.65 | $9.66 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,958.02 | -0.42% | $2,500.00 | $10,000.00 | $0.00 | $-41.98 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $336.17 | $334.48 | $322.28 | 49.0 | 1.73% | $345.28 | 0.47 | +3 |
| NVDA | $237.05 | $225.56 | $220.58 | 76.2 | 2.60% | $243.34 | 1.42 | +3 |
| AMD | $646.06 | $587.62 | $522.72 | 78.5 | 4.92% | $658.45 | 1.10 | +2 |
| MSFT | $528.00 | $506.49 | $496.09 | 71.5 | 2.98% | $535.69 | 1.83 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
