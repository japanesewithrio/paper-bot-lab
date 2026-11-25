# Paper Bot Lab — Latest Report

Updated: 2026-11-25T12:30:32.227462-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,857.09 | -1.43% | $7,886.46 | $10,051.61 | $-141.92 | $-0.99 | AAPL |
| 2 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,198.20 | -8.02% | $9,198.20 | $10,007.62 | $-801.80 | $0.00 | — |
| 4 | BOT_B | COOLDOWN | Dip / Mean Reversion | $8,374.65 | -16.25% | $8,374.65 | $10,009.55 | $-1,625.35 | $0.00 | — |

## Portfolio risk rules

- Stop at 80% of the equity at the last (re)start, or after a 15% drawdown from the peak.
- A stopped bot sells everything and sits out 28 calendar days (COOLDOWN), then restarts from its current equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $351.29 | $348.56 | $343.01 | 56.8 | 0.63% | $360.81 | 0.46 | +1 |
| NVDA | $144.09 | $172.22 | $203.56 | 36.2 | -1.29% | $215.32 | -1.19 | +0 |
| AMD | $384.10 | $487.99 | $547.84 | 48.0 | -21.52% | $593.93 | -1.95 | +1 |
| MSFT | $485.55 | $517.01 | $519.52 | 27.6 | -2.59% | $559.12 | -1.67 | +2 |

## Actions this run

- BOT_D BUY AAPL @ 351.47 — Conservative Confirmation entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
