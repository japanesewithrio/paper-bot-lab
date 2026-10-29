# Paper Bot Lab — Latest Report

Updated: 2026-10-29T14:45:17.333563-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,048.71 | 0.49% | $7,996.35 | $10,051.61 | $-4.57 | $53.27 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,884.10 | -1.16% | $9,884.10 | $10,007.62 | $-115.90 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,758.12 | -2.42% | $7,350.95 | $10,009.55 | $-193.74 | $-48.14 | NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,674.23 | -3.26% | $9,674.23 | $10,000.00 | $-325.77 | $0.00 | — |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $350.00 | $341.62 | $332.42 | 67.8 | 0.66% | $351.68 | 1.75 | -1 |
| NVDA | $212.68 | $222.89 | $221.99 | 33.7 | 0.78% | $243.34 | -1.12 | +0 |
| AMD | $566.25 | $576.64 | $547.47 | 41.2 | 9.56% | $658.45 | -0.24 | +0 |
| MSFT | $527.32 | $530.70 | $512.05 | 44.0 | 0.56% | $551.08 | -0.53 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
