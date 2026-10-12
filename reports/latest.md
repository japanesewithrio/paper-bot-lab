# Paper Bot Lab — Latest Report

Updated: 2026-10-12T15:09:00.659448-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,991.06 | -0.09% | $7,996.35 | $10,046.82 | $-4.57 | $-4.37 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,924.01 | -0.76% | $7,428.79 | $10,007.62 | $-103.46 | $27.47 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,753.96 | -2.46% | $7,200.12 | $10,000.00 | $-299.88 | $53.84 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $340.17 | $335.75 | $323.03 | 50.3 | 1.93% | $345.28 | 1.32 | +3 |
| NVDA | $226.48 | $227.52 | $222.60 | 46.6 | -5.31% | $243.34 | -0.15 | +2 |
| AMD | $590.39 | $602.94 | $531.31 | 39.0 | -9.11% | $658.45 | -0.31 | +1 |
| MSFT | $540.70 | $511.78 | $501.94 | 77.3 | 2.14% | $542.70 | 2.00 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
