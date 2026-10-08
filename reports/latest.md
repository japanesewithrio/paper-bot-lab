# Paper Bot Lab — Latest Report

Updated: 2026-10-08T14:07:17.492521-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,031.74 | 0.32% | $8,000.00 | $10,031.74 | $0.00 | $31.74 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,900.89 | -0.99% | $7,525.80 | $10,007.62 | $25.80 | $-124.92 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,735.37 | -2.65% | $2,500.00 | $10,000.00 | $0.00 | $-264.63 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $338.93 | $335.11 | $322.30 | 53.9 | 1.55% | $345.28 | 1.19 | -2 |
| NVDA | $230.49 | $226.18 | $221.40 | 61.3 | -1.50% | $243.34 | 0.54 | +1 |
| AMD | $616.97 | $593.37 | $526.51 | 65.6 | -2.65% | $658.45 | 0.48 | +2 |
| MSFT | $519.08 | $507.92 | $498.70 | 67.5 | 0.34% | $535.69 | 0.95 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
