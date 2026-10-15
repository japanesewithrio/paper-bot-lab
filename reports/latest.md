# Paper Bot Lab — Latest Report

Updated: 2026-10-15T15:06:26.294262-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,003.76 | 0.04% | $7,996.35 | $10,046.82 | $-4.57 | $8.32 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,821.26 | -1.79% | $9,821.26 | $10,009.55 | $-178.74 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,754.15 | -2.46% | $7,200.12 | $10,000.00 | $-299.88 | $54.03 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.34 | $337.09 | $325.11 | 51.7 | 1.74% | $348.11 | 1.37 | +0 |
| NVDA | $217.77 | $228.62 | $223.20 | 41.4 | -5.05% | $243.34 | -1.99 | -1 |
| AMD | $557.50 | $611.82 | $536.28 | 30.3 | -8.28% | $658.45 | -2.23 | +2 |
| MSFT | $540.74 | $518.48 | $504.97 | 67.0 | 1.04% | $551.08 | 1.44 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
