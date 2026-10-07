# Paper Bot Lab — Latest Report

Updated: 2026-10-07T10:41:39.702775-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,008.42 | 0.08% | $8,000.00 | $10,008.42 | $0.00 | $8.42 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,961.35 | -0.39% | $2,496.50 | $10,000.00 | $-17.65 | $-21.00 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,947.31 | -0.53% | $2,500.00 | $10,000.00 | $0.00 | $-52.69 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $335.03 | $334.42 | $322.26 | 47.4 | 1.39% | $345.28 | 0.17 | +3 |
| NVDA | $238.15 | $225.60 | $220.60 | 78.4 | 3.08% | $243.34 | 1.53 | +2 |
| AMD | $642.25 | $587.38 | $522.62 | 76.5 | 4.30% | $658.45 | 1.04 | +1 |
| MSFT | $526.40 | $506.40 | $496.06 | 69.8 | 2.67% | $535.69 | 1.73 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
