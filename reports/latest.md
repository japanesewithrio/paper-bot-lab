# Paper Bot Lab — Latest Report

Updated: 2026-10-27T14:30:01.863631-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,022.70 | 0.23% | $7,996.35 | $10,051.61 | $-4.57 | $27.26 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,888.92 | -1.11% | $7,426.01 | $10,007.62 | $-98.65 | $-12.43 | AAPL |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,804.76 | -1.95% | $4,762.78 | $10,009.55 | $-391.29 | $196.05 | AMD, NVDA |
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
| AAPL | $345.56 | $340.03 | $331.05 | 62.7 | 0.47% | $351.68 | 1.09 | +1 |
| NVDA | $217.54 | $224.45 | $222.17 | 31.6 | -1.96% | $243.34 | -0.78 | +0 |
| AMD | $565.44 | $580.98 | $543.67 | 33.8 | 2.33% | $658.45 | -0.35 | +1 |
| MSFT | $530.65 | $528.98 | $510.18 | 50.6 | -0.40% | $551.08 | 0.20 | +1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
