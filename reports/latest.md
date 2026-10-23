# Paper Bot Lab — Latest Report

Updated: 2026-10-23T12:03:18.470247-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,034.43 | 0.34% | $7,996.35 | $10,051.61 | $-4.57 | $38.99 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,911.61 | -0.88% | $7,431.19 | $10,007.62 | $-91.75 | $3.37 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,532.96 | -4.67% | $4,762.78 | $10,009.55 | $-391.29 | $-75.76 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $347.56 | $338.94 | $329.49 | 71.5 | 1.33% | $351.68 | 1.64 | +0 |
| NVDA | $212.85 | $225.67 | $222.54 | 23.3 | -1.95% | $243.34 | -1.53 | +0 |
| AMD | $517.50 | $587.43 | $542.35 | 27.8 | -3.78% | $658.45 | -1.62 | +0 |
| MSFT | $525.13 | $526.78 | $508.45 | 50.2 | -1.59% | $551.08 | -0.16 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
