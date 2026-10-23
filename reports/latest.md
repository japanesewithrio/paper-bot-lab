# Paper Bot Lab — Latest Report

Updated: 2026-10-23T15:06:03.174877-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,028.30 | 0.28% | $7,996.35 | $10,051.61 | $-4.57 | $32.86 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,901.35 | -0.99% | $9,901.35 | $10,007.62 | $-98.65 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,509.23 | -4.91% | $4,762.78 | $10,009.55 | $-391.29 | $-99.48 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $346.52 | $338.90 | $329.47 | 69.9 | 1.03% | $351.68 | 1.46 | +1 |
| NVDA | $211.56 | $225.60 | $222.52 | 21.9 | -2.55% | $243.34 | -1.66 | +2 |
| AMD | $515.50 | $587.20 | $542.26 | 26.4 | -4.15% | $658.45 | -1.65 | +0 |
| MSFT | $524.04 | $526.72 | $508.42 | 49.4 | -1.80% | $551.08 | -0.26 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
