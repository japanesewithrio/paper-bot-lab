# Paper Bot Lab — Latest Report

Updated: 2026-10-23T11:03:04.865774-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,033.72 | 0.34% | $7,996.35 | $10,051.61 | $-4.57 | $38.29 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,910.76 | -0.89% | $7,431.19 | $10,007.62 | $-91.75 | $2.51 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,566.90 | -4.33% | $4,762.78 | $10,009.55 | $-391.29 | $-41.81 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $347.44 | $338.95 | $329.49 | 71.8 | 1.30% | $351.68 | 1.61 | +0 |
| NVDA | $212.74 | $225.66 | $222.54 | 23.1 | -2.00% | $243.34 | -1.55 | +1 |
| AMD | $525.23 | $587.40 | $542.34 | 27.6 | -2.34% | $658.45 | -1.44 | +0 |
| MSFT | $524.78 | $526.76 | $508.44 | 49.9 | -1.66% | $551.08 | -0.20 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
