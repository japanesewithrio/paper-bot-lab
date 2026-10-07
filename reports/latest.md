# Paper Bot Lab — Latest Report

Updated: 2026-10-07T11:47:24.810487-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,007.61 | 0.08% | $8,000.00 | $10,008.42 | $0.00 | $7.61 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,980.76 | -0.19% | $2,496.50 | $10,000.00 | $-17.65 | $-1.59 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,959.92 | -0.40% | $2,500.00 | $10,000.00 | $0.00 | $-40.08 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $334.90 | $334.44 | $322.26 | 47.8 | 1.35% | $345.28 | 0.13 | +3 |
| NVDA | $237.40 | $225.58 | $220.59 | 77.0 | 2.75% | $243.34 | 1.45 | +3 |
| AMD | $644.86 | $587.59 | $522.71 | 78.3 | 4.72% | $658.45 | 1.08 | +2 |
| MSFT | $528.61 | $506.52 | $496.11 | 72.1 | 3.10% | $535.69 | 1.87 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
