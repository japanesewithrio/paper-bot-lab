# Paper Bot Lab — Latest Report

Updated: 2026-10-08T15:08:32.497175-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,044.36 | 0.44% | $8,000.00 | $10,044.36 | $0.00 | $44.36 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,900.15 | -1.00% | $7,525.80 | $10,007.62 | $25.80 | $-125.65 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,743.35 | -2.57% | $2,500.00 | $10,000.00 | $0.00 | $-256.65 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.03 | $335.22 | $322.34 | 56.2 | 2.18% | $345.28 | 1.73 | -2 |
| NVDA | $230.37 | $226.18 | $221.40 | 61.1 | -1.55% | $243.34 | 0.52 | +0 |
| AMD | $616.78 | $593.17 | $526.43 | 64.2 | -2.68% | $658.45 | 0.48 | +1 |
| MSFT | $521.19 | $508.02 | $498.74 | 69.3 | 0.75% | $535.69 | 1.11 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
