# Paper Bot Lab — Latest Report

Updated: 2026-10-09T13:40:33.679776-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 2 | BOT_D | ACTIVE | Conservative Confirmation | $9,995.43 | -0.05% | $9,995.43 | $10,046.82 | $-4.57 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,869.76 | -1.30% | $7,403.25 | $10,007.62 | $-129.01 | $-1.23 | MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,768.08 | -2.32% | $4,845.19 | $10,000.00 | $-154.81 | $-77.11 | MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $335.11 | $335.33 | $322.37 | 45.7 | 0.60% | $345.28 | -0.07 | +2 |
| NVDA | $229.52 | $226.75 | $222.09 | 53.4 | -3.96% | $243.34 | 0.35 | +2 |
| AMD | $612.54 | $598.24 | $529.08 | 48.4 | -3.07% | $658.45 | 0.31 | +0 |
| MSFT | $534.48 | $510.00 | $500.41 | 71.7 | 1.80% | $535.69 | 1.91 | +1 |

## Actions this run

- BOT_C BUY MSFT @ 534.75 — News + Momentum entry rule satisfied

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
