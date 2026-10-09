# Paper Bot Lab — Latest Report

Updated: 2026-10-09T10:45:01.033639-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,895.92 | -1.04% | $7,525.80 | $10,007.62 | $25.80 | $-129.89 | AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,797.30 | -2.03% | $2,500.00 | $10,000.00 | $0.00 | $-202.70 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $333.47 | $335.25 | $322.34 | 44.0 | 0.11% | $345.28 | -0.54 | +0 |
| NVDA | $230.69 | $226.81 | $222.11 | 55.3 | -3.47% | $243.34 | 0.49 | +1 |
| AMD | $615.68 | $598.37 | $529.13 | 49.3 | -2.58% | $658.45 | 0.37 | +0 |
| MSFT | $532.81 | $509.91 | $500.37 | 71.0 | 1.49% | $535.69 | 1.81 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
