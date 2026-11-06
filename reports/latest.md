# Paper Bot Lab — Latest Report

Updated: 2026-11-06T14:46:28.821331-05:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,922.06 | -0.78% | $9,922.06 | $10,051.61 | $-77.94 | $0.00 | — |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,780.68 | -2.19% | $9,780.68 | $10,007.62 | $-219.32 | $0.00 | — |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,273.41 | -7.27% | $6,918.65 | $10,009.55 | $-775.14 | $48.55 | NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.48 | $343.53 | $336.09 | 50.7 | 1.41% | $355.29 | -0.01 | +0 |
| NVDA | $187.37 | $211.60 | $219.84 | 30.0 | -7.34% | $228.79 | -2.10 | +0 |
| AMD | $444.77 | $527.03 | $546.70 | 38.3 | -4.71% | $606.19 | -1.65 | +0 |
| MSFT | $528.73 | $531.64 | $516.72 | 49.6 | 4.29% | $559.12 | -0.30 | +3 |

## Actions this run

- BOT_D SELL AAPL @ 343.31 — price<SMA20

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
