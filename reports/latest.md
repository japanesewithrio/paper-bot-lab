# Paper Bot Lab — Latest Report

Updated: 2026-10-12T14:06:47.635271-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,985.20 | -0.15% | $7,996.35 | $10,046.82 | $-4.57 | $-10.23 | AAPL |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,913.08 | -0.87% | $7,428.79 | $10,007.62 | $-103.46 | $16.53 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,742.77 | -2.57% | $7,200.12 | $10,000.00 | $-299.88 | $42.65 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.17 | $335.73 | $323.02 | 49.7 | 1.63% | $345.28 | 1.03 | +1 |
| NVDA | $226.42 | $227.51 | $222.60 | 46.5 | -5.33% | $243.34 | -0.16 | +2 |
| AMD | $590.85 | $602.91 | $531.29 | 38.8 | -9.03% | $658.45 | -0.30 | +1 |
| MSFT | $538.33 | $511.77 | $501.94 | 77.3 | 1.69% | $542.70 | 1.84 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
