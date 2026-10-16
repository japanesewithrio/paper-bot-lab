# Paper Bot Lab — Latest Report

Updated: 2026-10-16T12:57:52.459641-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,017.42 | 0.17% | $7,996.35 | $10,046.82 | $-4.57 | $21.99 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,936.22 | -0.64% | $7,455.20 | $10,007.62 | $-59.73 | $-4.05 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,731.87 | -2.68% | $4,910.94 | $10,009.55 | $-178.74 | $-89.38 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,691.24 | -3.09% | $7,200.12 | $10,000.00 | $-299.88 | $-8.88 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $344.66 | $337.52 | $325.74 | 57.8 | 1.06% | $348.11 | 1.73 | +2 |
| NVDA | $216.13 | $228.32 | $223.14 | 34.4 | -4.56% | $243.34 | -2.04 | -1 |
| AMD | $540.25 | $611.01 | $537.36 | 31.0 | -9.10% | $658.45 | -2.68 | +1 |
| MSFT | $527.42 | $520.14 | $505.49 | 61.9 | -2.53% | $551.08 | 0.51 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
