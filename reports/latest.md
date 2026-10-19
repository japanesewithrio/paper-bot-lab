# Paper Bot Lab — Latest Report

Updated: 2026-10-19T10:28:29.151298-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,020.30 | 0.20% | $7,996.35 | $10,046.82 | $-4.57 | $24.86 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,939.75 | -0.60% | $7,455.20 | $10,007.62 | $-59.73 | $-0.52 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,796.13 | -2.04% | $4,910.94 | $10,009.55 | $-178.74 | $-25.13 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,721.33 | -2.79% | $7,200.12 | $10,000.00 | $-299.88 | $21.21 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.15 | $337.76 | $326.35 | 74.1 | 1.12% | $348.11 | 1.69 | +1 |
| NVDA | $217.98 | $227.75 | $222.98 | 39.8 | -4.60% | $243.34 | -1.49 | +0 |
| AMD | $550.10 | $607.06 | $538.43 | 35.7 | -9.14% | $658.45 | -1.83 | +0 |
| MSFT | $533.79 | $521.81 | $506.20 | 65.7 | -1.79% | $551.08 | 0.85 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
