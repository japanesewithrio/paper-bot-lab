# Paper Bot Lab — Latest Report

Updated: 2026-10-22T14:21:09.986260-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,030.65 | 0.31% | $7,996.35 | $10,046.82 | $-4.57 | $35.21 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,907.01 | -0.93% | $7,431.19 | $10,007.62 | $-91.75 | $-1.24 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,564.19 | -4.36% | $7,153.40 | $10,009.55 | $-391.29 | $-44.52 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $346.92 | $338.54 | $328.61 | 70.5 | 1.03% | $348.11 | 1.75 | +2 |
| NVDA | $213.00 | $226.32 | $222.81 | 30.0 | -0.53% | $243.34 | -1.72 | +3 |
| AMD | $514.95 | $593.05 | $541.65 | 23.9 | -2.61% | $658.45 | -1.91 | +2 |
| MSFT | $524.33 | $526.45 | $507.93 | 54.2 | -0.88% | $551.08 | -0.21 | +2 |

## Actions this run

- BOT_C BUY AAPL @ 347.09 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
