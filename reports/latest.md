# Paper Bot Lab — Latest Report

Updated: 2026-10-15T15:54:41.039327-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,005.25 | 0.05% | $7,996.35 | $10,046.82 | $-4.57 | $9.82 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,821.26 | -1.79% | $9,821.26 | $10,009.55 | $-178.74 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,751.01 | -2.49% | $7,200.12 | $10,000.00 | $-299.88 | $50.89 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.59 | $337.08 | $325.10 | 51.4 | 1.82% | $348.11 | 1.44 | +0 |
| NVDA | $217.68 | $228.62 | $223.20 | 41.4 | -5.09% | $243.34 | -2.00 | -1 |
| AMD | $556.99 | $612.03 | $536.36 | 31.0 | -8.37% | $658.45 | -2.29 | +2 |
| MSFT | $540.08 | $518.42 | $504.95 | 66.4 | 0.91% | $551.08 | 1.40 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
