# Paper Bot Lab — Latest Report

Updated: 2026-10-09T13:07:12.964589-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,870.99 | -1.29% | $9,870.99 | $10,007.62 | $-129.01 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,769.14 | -2.31% | $4,845.19 | $10,000.00 | $-154.81 | $-76.05 | MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $335.14 | $335.33 | $322.37 | 45.6 | 0.61% | $345.28 | -0.06 | +1 |
| NVDA | $229.35 | $226.74 | $222.09 | 53.1 | -4.03% | $243.34 | 0.33 | +1 |
| AMD | $608.88 | $598.15 | $529.05 | 47.8 | -3.65% | $658.45 | 0.23 | +0 |
| MSFT | $535.09 | $510.05 | $500.43 | 72.0 | 1.92% | $535.69 | 1.94 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
