# Paper Bot Lab — Latest Report

Updated: 2026-10-08T11:43:52.337037-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,026.32 | 0.26% | $8,000.00 | $10,026.32 | $0.00 | $26.32 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,970.27 | -0.30% | $4,991.29 | $10,007.62 | $-8.71 | $-21.02 | AAPL, AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,915.76 | -0.84% | $2,500.00 | $10,000.00 | $0.00 | $-84.24 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $338.02 | $335.07 | $322.28 | 52.9 | 1.28% | $345.28 | 0.93 | +2 |
| NVDA | $235.58 | $226.43 | $221.50 | 70.6 | 0.68% | $243.34 | 1.11 | +1 |
| AMD | $635.41 | $594.18 | $526.84 | 71.8 | 0.26% | $658.45 | 0.82 | +3 |
| MSFT | $530.96 | $508.49 | $498.93 | 78.6 | 2.64% | $535.69 | 1.79 | -1 |

## Actions this run

- BOT_C SELL MSFT @ 530.70 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
