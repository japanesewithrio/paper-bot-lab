# Paper Bot Lab — Latest Report

Updated: 2026-10-23T13:56:17.713811-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,027.01 | 0.27% | $7,996.35 | $10,051.61 | $-4.57 | $31.57 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,902.59 | -0.97% | $7,431.19 | $10,007.62 | $-91.75 | $-5.66 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,511.72 | -4.88% | $4,762.78 | $10,009.55 | $-391.29 | $-96.99 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $346.30 | $338.88 | $329.46 | 69.0 | 0.97% | $351.68 | 1.43 | +0 |
| NVDA | $211.78 | $225.62 | $222.52 | 22.0 | -2.44% | $243.34 | -1.64 | +2 |
| AMD | $515.50 | $587.20 | $542.26 | 26.4 | -4.15% | $658.45 | -1.65 | +0 |
| MSFT | $522.24 | $526.72 | $508.43 | 49.5 | -2.14% | $551.08 | -0.44 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
