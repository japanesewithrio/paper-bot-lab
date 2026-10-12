# Paper Bot Lab — Latest Report

Updated: 2026-10-12T13:07:43.596849-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,988.51 | -0.11% | $7,996.35 | $10,046.82 | $-4.57 | $-6.92 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,918.61 | -0.81% | $7,428.79 | $10,007.62 | $-103.46 | $22.07 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,748.44 | -2.52% | $7,200.12 | $10,000.00 | $-299.88 | $48.32 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.74 | $335.74 | $323.02 | 50.0 | 1.80% | $345.28 | 1.19 | +1 |
| NVDA | $226.54 | $227.52 | $222.60 | 46.6 | -5.28% | $243.34 | -0.14 | +1 |
| AMD | $591.86 | $602.99 | $531.33 | 39.3 | -8.88% | $658.45 | -0.28 | +1 |
| MSFT | $539.53 | $511.73 | $501.92 | 77.0 | 1.92% | $542.70 | 1.94 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
