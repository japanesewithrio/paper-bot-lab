# Paper Bot Lab — Latest Report

Updated: 2026-10-16T11:57:01.030388-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,023.67 | 0.24% | $7,996.35 | $10,046.82 | $-4.57 | $28.23 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,943.88 | -0.56% | $7,455.20 | $10,007.62 | $-59.73 | $3.62 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,742.43 | -2.58% | $4,910.94 | $10,009.55 | $-178.74 | $-78.82 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,693.98 | -3.06% | $7,200.12 | $10,000.00 | $-299.88 | $-6.14 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.73 | $337.57 | $325.76 | 58.8 | 1.37% | $348.11 | 1.93 | +2 |
| NVDA | $217.60 | $228.38 | $223.17 | 35.7 | -3.91% | $243.34 | -1.85 | -1 |
| AMD | $538.88 | $611.07 | $537.39 | 31.2 | -9.33% | $658.45 | -2.75 | +2 |
| MSFT | $528.00 | $520.23 | $505.53 | 63.5 | -2.42% | $551.08 | 0.54 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
