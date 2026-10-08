# Paper Bot Lab — Latest Report

Updated: 2026-10-08T15:40:57.880562-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,046.82 | 0.47% | $8,000.00 | $10,046.82 | $0.00 | $46.82 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,893.53 | -1.06% | $7,525.80 | $10,007.62 | $25.80 | $-132.27 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,743.19 | -2.57% | $2,500.00 | $10,000.00 | $0.00 | $-256.81 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.44 | $335.23 | $322.35 | 56.4 | 2.30% | $345.28 | 1.83 | -1 |
| NVDA | $230.36 | $226.17 | $221.40 | 61.0 | -1.56% | $243.34 | 0.52 | +0 |
| AMD | $615.06 | $593.21 | $526.45 | 64.5 | -2.95% | $658.45 | 0.44 | +1 |
| MSFT | $522.58 | $508.07 | $498.76 | 70.3 | 1.02% | $535.69 | 1.22 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
