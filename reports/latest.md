# Paper Bot Lab — Latest Report

Updated: 2026-10-07T12:43:37.497561-04:00

> Simulation only. No Alpaca brokerage orders are submitted.

## Leaderboard

| Rank | Bot | Status | Strategy | Equity | Return | Cash | Peak | Realized P/L | Unrealized P/L | Open positions |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | BOT_D | ACTIVE | Conservative Confirmation | $10,013.55 | 0.14% | $8,000.00 | $10,013.55 | $0.00 | $13.55 | AAPL |
| 2 | BOT_B | ACTIVE | Dip / Mean Reversion | $10,000.00 | 0.00% | $10,000.00 | $10,000.00 | $0.00 | $0.00 | — |
| 3 | BOT_C | ACTIVE | News + Momentum | $9,972.57 | -0.27% | $2,496.50 | $10,000.00 | $-17.65 | $-9.78 | AAPL, AMD, MSFT |
| 4 | BOT_A | ACTIVE | Trend / Breakout | $9,939.39 | -0.61% | $2,500.00 | $10,000.00 | $0.00 | $-60.61 | AMD, MSFT, NVDA |

## Portfolio risk rules

- Permanent stop at 80% of starting equity (20% total loss).
- Permanent stop after a 15% drawdown from the bot's peak equity.
- Pause new entries for the rest of the trading day after a 5% daily equity loss.
- No profit ceiling: active bots may continue compounding.
- New position sizes are a percentage of current equity: A/B/C 25%, D 20%.

## Current signals

| Symbol | Price | SMA20 | SMA50 | RSI14 | 5D % | Prior 20D High | Z20 | News |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $335.89 | $334.46 | $322.27 | 48.3 | 1.65% | $345.28 | 0.40 | +3 |
| NVDA | $236.93 | $225.55 | $220.58 | 76.0 | 2.55% | $243.34 | 1.40 | +3 |
| AMD | $641.75 | $587.49 | $522.67 | 77.5 | 4.22% | $658.45 | 1.03 | +2 |
| MSFT | $527.83 | $506.48 | $496.09 | 71.4 | 2.95% | $535.69 | 1.82 | +3 |

## Actions this run

- No virtual trades this run.

## Notes

- Prices use IEX market data when available.
- Entries include 5 bps simulated slippage; exits also include 5 bps.
- Completed daily bars are used for rolling indicators; current market price is used for live comparisons and P/L.
- Portfolio stops are virtual risk controls only; this program does not submit broker orders.
