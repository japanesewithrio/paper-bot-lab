# Paper Bot Lab — Latest Report

Updated: 2026-10-14T13:00:00.253526-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,014.49 | 0.14% | $7,996.35 | $10,046.82 | $-4.57 | $19.06 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,952.04 | -0.48% | $7,500.00 | $10,009.55 | $0.00 | $-47.96 | AMD |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,730.72 | -2.69% | $7,200.12 | $10,000.00 | $-299.88 | $30.61 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.16 | $336.89 | $324.50 | 59.1 | 1.10% | $348.11 | 1.94 | -1 |
| NVDA | $222.64 | $228.77 | $223.25 | 47.4 | -3.44% | $243.34 | -1.17 | +2 |
| AMD | $570.14 | $611.25 | $534.78 | 33.6 | -8.16% | $658.45 | -1.59 | +1 |
| MSFT | $535.78 | $516.43 | $503.95 | 73.4 | 2.50% | $551.08 | 1.26 | -2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
