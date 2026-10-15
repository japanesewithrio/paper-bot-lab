# Paper Bot Lab — Latest Report

Updated: 2026-10-15T14:19:16.839662-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,003.79 | 0.04% | $7,996.35 | $10,046.82 | $-4.57 | $8.35 | AAPL |
| 2 | BOT_C | ACTIVE | News + Momentum | $9,940.27 | -0.60% | $9,940.27 | $10,007.62 | $-59.73 | $0.00 | — |
| 3 | BOT_B | ACTIVE | Dip / Mean Reversion | $9,821.26 | -1.79% | $9,821.26 | $10,009.55 | $-178.74 | $0.00 | — |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,751.41 | -2.49% | $7,200.12 | $10,000.00 | $-299.88 | $51.29 | MSFT |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $342.34 | $337.09 | $325.10 | 51.6 | 1.74% | $348.11 | 1.37 | +0 |
| NVDA | $217.20 | $228.59 | $223.19 | 40.9 | -5.30% | $243.34 | -2.06 | +0 |
| AMD | $555.05 | $611.40 | $536.11 | 29.0 | -8.69% | $658.45 | -2.22 | +2 |
| MSFT | $540.16 | $518.41 | $504.94 | 66.3 | 0.93% | $551.08 | 1.41 | -1 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
