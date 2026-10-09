# Paper Bot Lab — Latest Report

Updated: 2026-10-09T10:09:04.767435-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,893.49 | -1.07% | $7,525.80 | $10,007.62 | $25.80 | $-132.31 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,793.09 | -2.07% | $2,500.00 | $10,000.00 | $0.00 | $-206.91 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $332.19 | $335.19 | $322.31 | 42.8 | -0.28% | $345.28 | -0.91 | +0 |
| NVDA | $231.33 | $226.84 | $222.13 | 56.1 | -3.20% | $243.34 | 0.57 | +1 |
| AMD | $615.05 | $598.49 | $529.18 | 50.2 | -2.68% | $658.45 | 0.36 | +0 |
| MSFT | $531.00 | $509.77 | $500.32 | 69.8 | 1.14% | $535.69 | 1.71 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
