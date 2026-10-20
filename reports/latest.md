# Paper Bot Lab — Latest Report

Updated: 2026-10-20T11:01:36.219207-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,978.19 | -0.22% | $7,996.35 | $10,046.82 | $-4.57 | $-17.24 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,888.06 | -1.12% | $7,455.20 | $10,007.62 | $-59.73 | $-52.21 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,712.02 | -2.88% | $4,910.94 | $10,009.55 | $-178.74 | $-109.23 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,703.02 | -2.97% | $7,200.12 | $10,000.00 | $-299.88 | $2.90 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $337.98 | $337.69 | $326.96 | 62.5 | -1.47% | $348.11 | 0.07 | +1 |
| NVDA | $217.88 | $227.15 | $222.97 | 38.1 | -1.63% | $243.34 | -1.33 | +1 |
| AMD | $531.21 | $602.62 | $539.73 | 33.6 | -6.96% | $658.45 | -2.07 | +2 |
| MSFT | $529.91 | $523.47 | $506.70 | 61.9 | -0.77% | $551.08 | 0.49 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
