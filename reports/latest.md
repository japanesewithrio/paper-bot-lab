# Paper Bot Lab — Latest Report

Updated: 2026-10-09T12:42:14.655691-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,870.99 | -1.29% | $9,870.99 | $10,007.62 | $-129.01 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,767.61 | -2.32% | $4,845.19 | $10,000.00 | $-154.81 | $-77.58 | MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $334.52 | $335.31 | $322.36 | 45.2 | 0.42% | $345.28 | -0.24 | +1 |
| NVDA | $229.29 | $226.74 | $222.09 | 53.0 | -4.06% | $243.34 | 0.32 | +1 |
| AMD | $609.51 | $598.17 | $529.05 | 47.9 | -3.55% | $658.45 | 0.24 | +0 |
| MSFT | $534.90 | $510.05 | $500.43 | 72.0 | 1.88% | $535.69 | 1.92 | +0 |

## Actions this run

- BOT_A SELL AMD @ 609.21 — stop -6%
- BOT_C SELL AMD @ 609.21 — stop -6%

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
