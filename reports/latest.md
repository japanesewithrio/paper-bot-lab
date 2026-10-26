# Paper Bot Lab — Latest Report

Updated: 2026-10-26T11:07:13.892038-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,031.91 | 0.32% | $7,996.35 | $10,051.61 | $-4.57 | $36.47 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,900.11 | -1.00% | $7,426.01 | $10,007.62 | $-98.65 | $-1.24 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,654.55 | -3.45% | $4,762.78 | $10,009.55 | $-391.29 | $45.83 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $347.13 | $339.38 | $330.31 | 69.6 | 2.20% | $351.68 | 1.40 | +1 |
| NVDA | $217.76 | $225.01 | $222.35 | 30.6 | 0.62% | $243.34 | -0.84 | +3 |
| AMD | $531.97 | $583.26 | $542.55 | 24.7 | -0.44% | $658.45 | -1.14 | +2 |
| MSFT | $529.58 | $527.69 | $509.09 | 49.4 | -0.46% | $551.08 | 0.20 | +1 |

## Actions this run

- BOT_C BUY AAPL @ 347.31 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
