# Paper Bot Lab — Latest Report

Updated: 2026-10-07T10:07:35.733971-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,008.06 | 0.08% | $8,000.00 | $10,008.06 | $0.00 | $8.06 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,942.18 | -0.58% | $2,496.50 | $10,000.00 | $-17.65 | $-40.17 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,932.41 | -0.68% | $2,500.00 | $10,000.00 | $0.00 | $-67.59 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $334.98 | $334.42 | $322.25 | 47.3 | 1.37% | $345.28 | 0.16 | +3 |
| NVDA | $238.51 | $225.63 | $220.61 | 79.6 | 3.24% | $243.34 | 1.57 | +1 |
| AMD | $636.69 | $587.21 | $522.56 | 75.1 | 3.40% | $658.45 | 0.94 | +1 |
| MSFT | $526.97 | $506.43 | $496.07 | 70.4 | 2.78% | $535.69 | 1.76 | +3 |

## Actions this run

- BOT_C BUY MSFT @ 527.23 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
