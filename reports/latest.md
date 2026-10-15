# Paper Bot Lab — Latest Report

Updated: 2026-10-15T10:23:41.573111-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,018.60 | 0.19% | $7,996.35 | $10,046.82 | $-4.57 | $23.16 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,821.26 | -1.79% | $9,821.26 | $10,009.55 | $-178.74 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,727.63 | -2.72% | $7,200.12 | $10,000.00 | $-299.88 | $27.51 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.87 | $337.21 | $325.15 | 54.5 | 2.50% | $348.11 | 1.90 | -2 |
| NVDA | $216.30 | $228.55 | $223.17 | 40.0 | -5.69% | $243.34 | -2.18 | -1 |
| AMD | $540.00 | $610.76 | $535.85 | 27.1 | -11.16% | $658.45 | -2.62 | +2 |
| MSFT | $535.12 | $518.08 | $504.81 | 62.3 | -0.01% | $551.08 | 1.13 | +1 |

## Actions this run

- BOT_B SELL AMD @ 539.73 — stop -7%

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
