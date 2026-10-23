# Paper Bot Lab — Latest Report

Updated: 2026-10-23T13:27:35.350944-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,025.66 | 0.26% | $7,996.35 | $10,051.61 | $-4.57 | $30.23 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,900.95 | -0.99% | $7,431.19 | $10,007.62 | $-91.75 | $-7.30 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,523.62 | -4.76% | $4,762.78 | $10,009.55 | $-391.29 | $-85.09 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $346.07 | $338.86 | $329.45 | 68.2 | 0.90% | $351.68 | 1.40 | +0 |
| NVDA | $211.74 | $225.61 | $222.52 | 21.9 | -2.46% | $243.34 | -1.64 | +1 |
| AMD | $518.22 | $587.13 | $542.23 | 26.0 | -3.64% | $658.45 | -1.58 | +0 |
| MSFT | $524.81 | $526.75 | $508.44 | 49.9 | -1.66% | $551.08 | -0.19 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
