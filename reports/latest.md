# Paper Bot Lab — Latest Report

Updated: 2026-10-28T14:35:49.153455-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,019.74 | 0.20% | $7,996.35 | $10,051.61 | $-4.57 | $24.30 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,884.10 | -1.16% | $9,884.10 | $10,007.62 | $-115.90 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,804.24 | -1.96% | $7,350.95 | $10,009.55 | $-193.74 | $-2.02 | NVDA |
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
| AAPL | $345.06 | $340.68 | $331.77 | 56.0 | -0.94% | $351.68 | 0.88 | -1 |
| NVDA | $216.75 | $223.90 | $222.12 | 35.9 | 2.11% | $243.34 | -0.80 | -1 |
| AMD | $567.57 | $579.07 | $545.45 | 40.6 | 11.70% | $658.45 | -0.26 | +1 |
| MSFT | $529.10 | $529.81 | $511.13 | 53.8 | 1.44% | $551.08 | -0.10 | -1 |

## Actions this run

- BOT_B SELL AMD @ 567.29 — take +8%
- BOT_C SELL AAPL @ 344.89 — negative news

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
