# Paper Bot Lab — Latest Report

Updated: 2026-10-16T14:17:09.326192-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,005.58 | 0.06% | $7,996.35 | $10,046.82 | $-4.57 | $10.14 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,921.68 | -0.78% | $7,455.20 | $10,007.62 | $-59.73 | $-18.59 | AAPL |
| 3 | BOT_A | ACTIVE | Trend / Breakout | $9,690.13 | -3.10% | $7,200.12 | $10,000.00 | $-299.88 | $-9.99 | MSFT |
| 4 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,684.47 | -3.16% | $4,910.94 | $10,009.55 | $-178.74 | $-136.78 | AMD, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.64 | $337.40 | $325.69 | 55.1 | 0.47% | $348.11 | 1.33 | +2 |
| NVDA | $214.92 | $228.26 | $223.12 | 33.4 | -5.10% | $243.34 | -2.19 | -1 |
| AMD | $532.59 | $610.70 | $537.24 | 29.9 | -10.39% | $658.45 | -2.86 | +1 |
| MSFT | $527.18 | $520.13 | $505.49 | 61.8 | -2.57% | $551.08 | 0.49 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
