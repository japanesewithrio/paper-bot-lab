# Paper Bot Lab — Latest Report

Updated: 2026-10-23T14:20:11.781692-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,027.01 | 0.27% | $7,996.35 | $10,051.61 | $-4.57 | $31.57 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,901.35 | -0.99% | $9,901.35 | $10,007.62 | $-98.65 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,511.67 | -4.88% | $4,762.78 | $10,009.55 | $-391.29 | $-97.05 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $346.30 | $338.88 | $329.46 | 68.9 | 0.97% | $351.68 | 1.44 | -1 |
| NVDA | $211.77 | $225.61 | $222.52 | 22.0 | -2.45% | $243.34 | -1.64 | +2 |
| AMD | $515.50 | $587.28 | $542.29 | 26.9 | -4.15% | $658.45 | -1.66 | +0 |
| MSFT | $524.53 | $526.74 | $508.43 | 49.7 | -1.71% | $551.08 | -0.22 | +3 |

## Actions this run

- BOT_C SELL AAPL @ 346.13 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
