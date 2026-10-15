# Paper Bot Lab — Latest Report

Updated: 2026-10-15T13:54:02.599242-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,012.73 | 0.13% | $7,996.35 | $10,046.82 | $-4.57 | $17.30 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,821.26 | -1.79% | $9,821.26 | $10,009.55 | $-178.74 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,749.57 | -2.50% | $7,200.12 | $10,000.00 | $-299.88 | $49.45 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $343.87 | $337.16 | $325.13 | 53.5 | 2.20% | $348.11 | 1.70 | +0 |
| NVDA | $217.20 | $228.60 | $223.19 | 41.0 | -5.30% | $243.34 | -2.07 | +3 |
| AMD | $548.50 | $611.15 | $536.01 | 28.2 | -9.76% | $658.45 | -2.41 | +2 |
| MSFT | $539.77 | $518.42 | $504.95 | 66.4 | 0.85% | $551.08 | 1.38 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
