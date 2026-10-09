# Paper Bot Lab — Latest Report

Updated: 2026-10-09T09:43:31.382307-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,897.50 | -1.03% | $7,525.80 | $10,007.62 | $25.80 | $-128.31 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,765.10 | -2.35% | $2,500.00 | $10,000.00 | $0.00 | $-234.90 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $333.03 | $335.22 | $322.33 | 43.4 | -0.02% | $345.28 | -0.66 | +0 |
| NVDA | $231.44 | $226.86 | $222.13 | 56.6 | -3.16% | $243.34 | 0.58 | +1 |
| AMD | $616.09 | $598.53 | $529.20 | 50.5 | -2.51% | $658.45 | 0.38 | +0 |
| MSFT | $524.00 | $509.69 | $500.29 | 69.1 | -0.19% | $535.69 | 1.16 | +0 |

## Actions this run

- BOT_D SELL AAPL @ 332.87 — price<SMA20

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
