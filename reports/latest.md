# Paper Bot Lab — Latest Report

Updated: 2026-10-09T12:08:18.545935-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,877.13 | -1.23% | $7,525.80 | $10,007.62 | $25.80 | $-148.67 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,780.07 | -2.20% | $2,500.00 | $10,000.00 | $0.00 | $-219.93 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $334.50 | $335.30 | $322.36 | 45.0 | 0.42% | $345.28 | -0.25 | +0 |
| NVDA | $229.70 | $226.76 | $222.09 | 53.7 | -3.88% | $243.34 | 0.37 | +1 |
| AMD | $610.80 | $598.23 | $529.08 | 48.4 | -3.35% | $658.45 | 0.27 | +0 |
| MSFT | $535.32 | $510.06 | $500.44 | 72.1 | 1.96% | $535.69 | 1.95 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
