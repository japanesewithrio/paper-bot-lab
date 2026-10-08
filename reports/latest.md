# Paper Bot Lab — Latest Report

Updated: 2026-10-08T09:43:17.594589-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,019.81 | 0.20% | $8,000.00 | $10,019.96 | $0.00 | $19.81 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,963.33 | -0.37% | $4,991.15 | $10,007.62 | $-8.85 | $-27.82 | AAPL, AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,901.45 | -0.99% | $2,500.00 | $10,000.00 | $0.00 | $-98.55 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $336.94 | $335.01 | $322.26 | 51.5 | 0.95% | $345.28 | 0.62 | +2 |
| NVDA | $234.14 | $226.36 | $221.47 | 67.6 | 0.06% | $243.34 | 0.95 | +2 |
| AMD | $635.76 | $594.08 | $526.80 | 70.9 | 0.32% | $658.45 | 0.83 | +3 |
| MSFT | $530.84 | $508.54 | $498.94 | 78.9 | 2.61% | $535.69 | 1.76 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
