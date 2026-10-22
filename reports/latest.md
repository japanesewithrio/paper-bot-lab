# Paper Bot Lab — Latest Report

Updated: 2026-10-22T10:25:12.059864-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,013.70 | 0.14% | $7,996.35 | $10,046.82 | $-4.57 | $18.26 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,593.74 | -4.06% | $7,153.40 | $10,009.55 | $-391.29 | $-14.98 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.03 | $338.41 | $328.56 | 67.8 | 0.19% | $348.11 | 1.23 | +1 |
| NVDA | $215.61 | $226.44 | $222.85 | 31.4 | 0.69% | $243.34 | -1.43 | -1 |
| AMD | $518.46 | $593.44 | $541.80 | 24.7 | -1.95% | $658.45 | -1.87 | +2 |
| MSFT | $524.08 | $526.43 | $507.92 | 53.9 | -0.93% | $551.08 | -0.23 | -1 |

## Actions this run

- BOT_A SELL MSFT @ 523.82 — price<SMA20

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
