# Paper Bot Lab — Latest Report

Updated: 2026-10-20T15:56:11.403484-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $9,984.73 | -0.15% | $7,996.35 | $10,046.82 | $-4.57 | $-10.70 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,746.43 | -2.54% | $4,910.94 | $10,009.55 | $-178.74 | $-74.83 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,714.90 | -2.85% | $7,200.12 | $10,000.00 | $-299.88 | $14.78 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $339.09 | $337.62 | $326.93 | 59.9 | -1.14% | $348.11 | 0.35 | -2 |
| NVDA | $216.61 | $227.09 | $222.94 | 36.5 | -2.20% | $243.34 | -1.48 | +0 |
| AMD | $542.32 | $602.16 | $539.55 | 30.7 | -5.02% | $658.45 | -1.70 | +2 |
| MSFT | $532.43 | $523.49 | $506.71 | 62.1 | -0.30% | $551.08 | 0.68 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
