# Paper Bot Lab — Latest Report

Updated: 2026-10-16T13:53:56.880067-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,003.06 | 0.03% | $7,996.35 | $10,046.82 | $-4.57 | $7.62 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,918.58 | -0.81% | $7,455.20 | $10,007.62 | $-59.73 | $-21.69 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,721.81 | -2.78% | $4,910.94 | $10,009.55 | $-178.74 | $-99.45 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,688.24 | -3.12% | $7,200.12 | $10,000.00 | $-299.88 | $-11.88 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.22 | $337.40 | $325.70 | 55.3 | 0.34% | $348.11 | 1.21 | +2 |
| NVDA | $215.34 | $228.27 | $223.12 | 33.7 | -4.91% | $243.34 | -2.14 | -1 |
| AMD | $539.99 | $610.70 | $537.24 | 29.9 | -9.14% | $658.45 | -2.59 | +1 |
| MSFT | $526.79 | $520.14 | $505.50 | 62.0 | -2.64% | $551.08 | 0.46 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
