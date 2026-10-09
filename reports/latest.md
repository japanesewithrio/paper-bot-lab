# Paper Bot Lab — Latest Report

Updated: 2026-10-09T14:44:33.023475-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,877.27 | -1.23% | $4,933.62 | $10,007.62 | $-129.01 | $6.28 | AAPL, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,776.20 | -2.24% | $4,845.19 | $10,000.00 | $-154.81 | $-68.99 | MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $336.85 | $335.41 | $322.40 | 47.4 | 1.12% | $345.28 | 0.44 | +2 |
| NVDA | $229.44 | $226.74 | $222.09 | 53.1 | -3.99% | $243.34 | 0.34 | +2 |
| AMD | $612.11 | $598.25 | $529.09 | 48.5 | -3.14% | $658.45 | 0.30 | +0 |
| MSFT | $536.38 | $510.13 | $500.46 | 72.6 | 2.16% | $536.60 | 2.01 | +1 |

## Actions this run

- BOT_C BUY AAPL @ 337.01 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
