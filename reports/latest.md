# Paper Bot Lab — Latest Report

Updated: 2026-10-15T09:32:07.093505-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,031.38 | 0.31% | $7,996.35 | $10,046.82 | $-4.57 | $35.94 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,837.47 | -1.63% | $7,500.00 | $10,009.55 | $0.00 | $-162.53 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,721.70 | -2.78% | $7,200.12 | $10,000.00 | $-299.88 | $21.59 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $347.04 | $337.29 | $325.19 | 56.3 | 3.14% | $348.11 | 2.32 | -2 |
| NVDA | $213.64 | $228.42 | $223.11 | 37.8 | -6.85% | $243.34 | -2.49 | -1 |
| AMD | $543.50 | $610.77 | $535.86 | 27.2 | -10.59% | $658.45 | -2.50 | +2 |
| MSFT | $533.87 | $518.12 | $504.83 | 63.1 | -0.25% | $551.08 | 1.05 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
