# Paper Bot Lab — Latest Report

Updated: 2026-10-08T12:09:31.504824-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,028.32 | 0.28% | $8,000.00 | $10,028.32 | $0.00 | $28.32 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,961.76 | -0.38% | $4,991.29 | $10,007.62 | $-8.71 | $-29.54 | AAPL, AMD |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,896.09 | -1.04% | $2,500.00 | $10,000.00 | $0.00 | $-103.91 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $338.36 | $335.08 | $322.29 | 53.2 | 1.38% | $345.28 | 1.03 | +2 |
| NVDA | $235.40 | $226.43 | $221.50 | 70.5 | 0.60% | $243.34 | 1.09 | +2 |
| AMD | $632.55 | $594.07 | $526.79 | 70.8 | -0.19% | $658.45 | 0.77 | +3 |
| MSFT | $529.55 | $508.42 | $498.90 | 77.9 | 2.36% | $535.69 | 1.70 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
