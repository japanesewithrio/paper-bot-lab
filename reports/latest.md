# Paper Bot Lab — Latest Report

Updated: 2026-10-08T10:09:31.819488-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,021.07 | 0.21% | $8,000.00 | $10,021.07 | $0.00 | $21.07 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,968.96 | -0.31% | $2,498.60 | $10,007.62 | $-8.85 | $-22.20 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,920.99 | -0.79% | $2,500.00 | $10,000.00 | $0.00 | $-79.01 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $337.14 | $335.02 | $322.26 | 51.8 | 1.02% | $345.28 | 0.68 | +2 |
| NVDA | $235.70 | $226.43 | $221.50 | 70.7 | 0.73% | $243.34 | 1.12 | +1 |
| AMD | $637.13 | $594.36 | $526.91 | 73.3 | 0.53% | $658.45 | 0.85 | +3 |
| MSFT | $530.40 | $508.47 | $498.92 | 78.5 | 2.53% | $535.69 | 1.75 | +1 |

## Actions this run

- BOT_C BUY MSFT @ 530.67 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
