# Paper Bot Lab — Latest Report

Updated: 2026-10-12T12:42:36.035167-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,989.28 | -0.11% | $7,996.35 | $10,046.82 | $-4.57 | $-6.16 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,923.55 | -0.76% | $7,428.79 | $10,007.62 | $-103.46 | $27.01 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,753.49 | -2.47% | $7,200.12 | $10,000.00 | $-299.88 | $53.37 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.87 | $335.75 | $323.02 | 50.1 | 1.84% | $345.28 | 1.23 | +0 |
| NVDA | $226.47 | $227.52 | $222.60 | 46.7 | -5.31% | $243.34 | -0.15 | +1 |
| AMD | $595.00 | $603.07 | $531.36 | 39.7 | -8.40% | $658.45 | -0.20 | +1 |
| MSFT | $540.60 | $511.81 | $501.96 | 77.5 | 2.12% | $542.70 | 1.98 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
