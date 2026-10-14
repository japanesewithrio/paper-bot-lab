# Paper Bot Lab — Latest Report

Updated: 2026-10-14T12:05:32.243752-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,017.69 | 0.18% | $7,996.35 | $10,046.82 | $-4.57 | $22.25 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,009.55 | 0.10% | $7,500.00 | $10,009.55 | $0.00 | $9.55 | AMD |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,735.97 | -2.64% | $7,200.12 | $10,000.00 | $-299.88 | $35.85 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.71 | $336.90 | $324.50 | 59.3 | 1.26% | $348.11 | 2.07 | -3 |
| NVDA | $222.46 | $228.76 | $223.25 | 47.3 | -3.52% | $243.34 | -1.21 | +2 |
| AMD | $583.51 | $611.38 | $534.84 | 34.1 | -6.01% | $658.45 | -1.08 | +1 |
| MSFT | $536.89 | $516.47 | $503.96 | 74.1 | 2.71% | $551.08 | 1.32 | -2 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
