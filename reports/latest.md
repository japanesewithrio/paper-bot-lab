# Paper Bot Lab — Latest Report

Updated: 2026-10-08T11:07:58.452100-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,025.63 | 0.26% | $8,000.00 | $10,025.63 | $0.00 | $25.63 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,968.67 | -0.31% | $2,498.60 | $10,007.62 | $-8.85 | $-22.49 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,918.58 | -0.81% | $2,500.00 | $10,000.00 | $0.00 | $-81.42 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $337.90 | $335.05 | $322.27 | 52.4 | 1.24% | $345.28 | 0.91 | +2 |
| NVDA | $236.05 | $226.46 | $221.51 | 71.9 | 0.87% | $243.34 | 1.16 | +0 |
| AMD | $634.47 | $594.21 | $526.85 | 72.0 | 0.11% | $658.45 | 0.80 | +3 |
| MSFT | $531.32 | $508.51 | $498.93 | 78.7 | 2.71% | $535.69 | 1.81 | +0 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
