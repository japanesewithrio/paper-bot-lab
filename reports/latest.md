# Paper Bot Lab — Latest Report

Updated: 2026-10-13T11:11:07.096490-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,024.17 | 0.24% | $7,996.35 | $10,046.82 | $-4.57 | $28.73 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,969.49 | -0.31% | $4,937.89 | $10,007.62 | $-103.46 | $72.95 | AAPL, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,786.88 | -2.13% | $7,200.12 | $10,000.00 | $-299.88 | $86.77 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.81 | $336.53 | $323.89 | 59.3 | 2.74% | $348.11 | 2.37 | +0 |
| NVDA | $224.64 | $228.14 | $222.96 | 48.6 | -5.37% | $243.34 | -0.58 | +2 |
| AMD | $589.43 | $607.29 | $533.45 | 40.6 | -8.74% | $658.45 | -0.54 | +1 |
| MSFT | $547.67 | $514.31 | $503.15 | 78.4 | 3.39% | $551.08 | 2.09 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
