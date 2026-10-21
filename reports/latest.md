# Paper Bot Lab — Latest Report

Updated: 2026-10-21T11:29:02.384777-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,015.22 | 0.15% | $7,996.35 | $10,046.82 | $-4.57 | $19.79 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,908.25 | -0.92% | $9,908.25 | $10,007.62 | $-91.75 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,805.58 | -1.94% | $4,910.94 | $10,009.55 | $-178.74 | $-15.67 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,708.60 | -2.91% | $7,200.12 | $10,000.00 | $-299.88 | $8.48 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.29 | $338.02 | $327.73 | 71.4 | 0.70% | $348.11 | 1.41 | +1 |
| NVDA | $219.69 | $226.80 | $222.99 | 37.8 | 1.08% | $243.34 | -0.98 | +3 |
| AMD | $547.86 | $598.60 | $540.95 | 32.9 | -2.54% | $658.45 | -1.36 | +2 |
| MSFT | $531.10 | $525.03 | $507.26 | 61.9 | -1.53% | $551.08 | 0.50 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
