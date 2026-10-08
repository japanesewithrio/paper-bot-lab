# Paper Bot Lab — Latest Report

Updated: 2026-10-08T12:44:14.103685-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,029.88 | 0.30% | $8,000.00 | $10,029.88 | $0.00 | $29.88 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,959.68 | -0.40% | $4,991.29 | $10,007.62 | $-8.71 | $-31.61 | AAPL, AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,881.13 | -1.19% | $2,500.00 | $10,000.00 | $0.00 | $-118.87 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $338.62 | $335.08 | $322.29 | 53.2 | 1.46% | $345.28 | 1.11 | +3 |
| NVDA | $234.71 | $226.40 | $221.49 | 69.2 | 0.31% | $243.34 | 1.01 | +2 |
| AMD | $631.50 | $594.04 | $526.78 | 70.6 | -0.35% | $658.45 | 0.75 | +3 |
| MSFT | $528.75 | $508.37 | $498.88 | 76.8 | 2.21% | $535.69 | 1.65 | -2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
