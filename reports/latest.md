# Paper Bot Lab — Latest Report

Updated: 2026-10-16T10:21:14.696833-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,019.71 | 0.20% | $7,996.35 | $10,046.82 | $-4.57 | $24.27 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,939.03 | -0.61% | $7,455.20 | $10,007.62 | $-59.73 | $-1.24 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,818.80 | -1.81% | $4,910.94 | $10,009.55 | $-178.74 | $-2.45 | AMD, NVDA |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,735.73 | -2.64% | $7,200.12 | $10,000.00 | $-299.88 | $35.61 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $345.06 | $337.53 | $325.75 | 58.0 | 1.18% | $348.11 | 1.81 | +3 |
| NVDA | $216.82 | $228.34 | $223.15 | 34.9 | -4.26% | $243.34 | -1.95 | +2 |
| AMD | $558.25 | $611.20 | $537.44 | 31.7 | -6.07% | $658.45 | -2.04 | +2 |
| MSFT | $536.84 | $520.65 | $505.70 | 71.5 | -0.78% | $551.08 | 1.09 | +2 |

## Actions this run

- BOT_B BUY NVDA @ 216.93 — Dip / Mean Reversion entry rule satisfied
- BOT_B BUY AMD @ 558.52 — Dip / Mean Reversion entry rule satisfied
- BOT_C BUY AAPL @ 345.23 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
