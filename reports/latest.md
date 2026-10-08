# Paper Bot Lab — Latest Report

Updated: 2026-10-08T13:41:18.118258-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,028.62 | 0.29% | $8,000.00 | $10,031.68 | $0.00 | $28.62 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,907.47 | -0.93% | $7,525.80 | $10,007.62 | $25.80 | $-118.34 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,770.96 | -2.29% | $2,500.00 | $10,000.00 | $0.00 | $-229.04 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $338.40 | $335.09 | $322.29 | 53.4 | 1.39% | $345.28 | 1.04 | -1 |
| NVDA | $231.33 | $226.22 | $221.42 | 62.7 | -1.14% | $243.34 | 0.63 | +1 |
| AMD | $618.68 | $593.43 | $526.54 | 66.0 | -2.38% | $658.45 | 0.51 | +3 |
| MSFT | $523.35 | $508.12 | $498.78 | 71.3 | 1.17% | $535.69 | 1.27 | -2 |

## Actions this run

- BOT_C SELL AAPL @ 338.24 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
