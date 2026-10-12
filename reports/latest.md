# Paper Bot Lab — Latest Report

Updated: 2026-10-12T12:09:24.794582-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,990.21 | -0.10% | $7,996.35 | $10,046.82 | $-4.57 | $-5.22 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,925.47 | -0.75% | $7,428.79 | $10,007.62 | $-103.46 | $28.92 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,755.45 | -2.45% | $7,200.12 | $10,000.00 | $-299.88 | $55.33 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $340.02 | $335.75 | $323.02 | 50.2 | 1.89% | $345.28 | 1.28 | +0 |
| NVDA | $226.82 | $227.54 | $222.61 | 47.2 | -5.16% | $243.34 | -0.10 | +1 |
| AMD | $596.56 | $603.11 | $531.38 | 39.9 | -8.16% | $658.45 | -0.16 | +2 |
| MSFT | $541.01 | $511.85 | $501.97 | 77.7 | 2.20% | $542.70 | 2.00 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
