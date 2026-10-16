# Paper Bot Lab — Latest Report

Updated: 2026-10-16T09:30:35.558835-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,027.24 | 0.27% | $7,996.35 | $10,046.82 | $-4.57 | $31.81 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,821.26 | -1.79% | $9,821.26 | $10,009.55 | $-178.74 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,756.40 | -2.44% | $7,200.12 | $10,000.00 | $-299.88 | $56.28 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $346.34 | $337.07 | $325.10 | 51.1 | 2.93% | $348.11 | 2.44 | +3 |
| NVDA | $215.52 | $228.61 | $223.19 | 41.1 | -6.03% | $243.34 | -2.38 | +3 |
| AMD | $563.02 | $611.96 | $536.34 | 30.8 | -7.38% | $658.45 | -2.03 | +2 |
| MSFT | $541.22 | $518.42 | $504.94 | 66.3 | 1.12% | $551.08 | 1.48 | +2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
