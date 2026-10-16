# Paper Bot Lab — Latest Report

Updated: 2026-10-16T11:23:08.475352-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,025.34 | 0.25% | $7,996.35 | $10,046.82 | $-4.57 | $29.90 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,945.94 | -0.54% | $7,455.20 | $10,007.62 | $-59.73 | $5.67 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,792.13 | -2.08% | $4,910.94 | $10,009.55 | $-178.74 | $-29.13 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,705.10 | -2.95% | $7,200.12 | $10,000.00 | $-299.88 | $4.98 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $346.01 | $337.58 | $325.77 | 59.1 | 1.46% | $348.11 | 1.98 | +3 |
| NVDA | $216.40 | $228.32 | $223.14 | 34.5 | -4.44% | $243.34 | -2.00 | -1 |
| AMD | $553.25 | $610.97 | $537.35 | 30.8 | -6.91% | $658.45 | -2.18 | +2 |
| MSFT | $530.36 | $520.28 | $505.55 | 64.4 | -1.98% | $551.08 | 0.70 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
