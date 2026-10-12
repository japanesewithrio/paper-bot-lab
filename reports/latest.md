# Paper Bot Lab — Latest Report

Updated: 2026-10-12T10:49:10.442488-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,923.87 | -0.76% | $7,428.79 | $10,007.62 | $-103.46 | $27.33 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,753.82 | -2.46% | $7,200.12 | $10,000.00 | $-299.88 | $53.70 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $341.14 | $335.81 | $323.05 | 51.5 | 2.22% | $345.28 | 1.55 | -1 |
| NVDA | $225.51 | $227.48 | $222.58 | 45.5 | -5.71% | $243.34 | -0.28 | +1 |
| AMD | $584.27 | $602.83 | $531.26 | 38.4 | -10.05% | $658.45 | -0.46 | +2 |
| MSFT | $540.67 | $511.80 | $501.95 | 77.5 | 2.13% | $542.06 | 1.99 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
