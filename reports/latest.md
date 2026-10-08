# Paper Bot Lab — Latest Report

Updated: 2026-10-08T10:43:39.980872-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,025.39 | 0.25% | $8,000.00 | $10,025.39 | $0.00 | $25.39 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,981.55 | -0.18% | $2,498.60 | $10,007.62 | $-8.85 | $-9.60 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,939.38 | -0.61% | $2,500.00 | $10,000.00 | $0.00 | $-60.62 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $337.87 | $335.05 | $322.28 | 52.6 | 1.23% | $345.28 | 0.89 | +2 |
| NVDA | $236.77 | $226.50 | $221.53 | 73.7 | 1.19% | $243.34 | 1.23 | +0 |
| AMD | $638.48 | $594.34 | $526.90 | 73.1 | 0.75% | $658.45 | 0.88 | +3 |
| MSFT | $530.84 | $508.50 | $498.93 | 78.7 | 2.61% | $535.69 | 1.78 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
