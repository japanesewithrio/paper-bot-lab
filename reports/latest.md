# Paper Bot Lab — Latest Report

Updated: 2026-10-09T15:40:35.337471-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,865.06 | -1.35% | $4,933.62 | $10,007.62 | $-129.01 | $-5.93 | AAPL, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,775.51 | -2.24% | $4,845.19 | $10,000.00 | $-154.81 | $-69.68 | MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $335.47 | $335.41 | $322.40 | 47.3 | 0.71% | $345.28 | 0.02 | +2 |
| NVDA | $229.58 | $226.75 | $222.09 | 53.4 | -3.93% | $243.34 | 0.36 | +2 |
| AMD | $607.18 | $598.01 | $528.99 | 46.9 | -3.92% | $658.45 | 0.20 | +0 |
| MSFT | $535.92 | $510.09 | $500.45 | 72.4 | 2.08% | $537.17 | 1.99 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
