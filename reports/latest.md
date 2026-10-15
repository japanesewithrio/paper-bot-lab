# Paper Bot Lab — Latest Report

Updated: 2026-10-15T12:19:28.539514-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,009.98 | 0.10% | $7,996.35 | $10,046.82 | $-4.57 | $14.54 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,821.26 | -1.79% | $9,821.26 | $10,009.55 | $-178.74 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,749.31 | -2.51% | $7,200.12 | $10,000.00 | $-299.88 | $49.19 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.39 | $337.14 | $325.12 | 53.0 | 2.06% | $348.11 | 1.60 | -2 |
| NVDA | $216.87 | $228.58 | $223.18 | 40.7 | -5.44% | $243.34 | -2.11 | -1 |
| AMD | $546.38 | $611.33 | $536.08 | 28.8 | -10.11% | $658.45 | -2.54 | +2 |
| MSFT | $539.72 | $518.43 | $504.95 | 66.5 | 0.84% | $551.08 | 1.38 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
