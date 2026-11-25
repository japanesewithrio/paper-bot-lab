# Paper Bot Lab — Backtest

Generated: 2026-11-25 00:04 UTC · data: Alpaca daily bars (DataFeed.SIP, split/dividend adjusted) · 2016-03-23 → 2026-11-23

> Simulation only. Past results do not predict future results. Not financial advice.

| Bot / benchmark | Strategy | Total return | CAGR | Max drawdown | Sharpe | Trades | Win rate | Status | Stopped on |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BOT_A | Trend / Breakout | +86.3% | +6.0% | -16.0% | 0.78 | 118 | 53% | STOPPED | 2021-02-25 |
| BOT_B | Dip / Mean Reversion | +13.2% | +1.2% | -15.3% | 0.26 | 48 | 71% | STOPPED | 2018-11-16 |
| BOT_C | News + Momentum | +203.7% | +11.0% | -15.3% | 0.97 | 273 | 42% | STOPPED | 2021-01-29 |
| BOT_D | Conservative Confirmation | +53.8% | +4.1% | -14.6% | 0.70 | 313 | 44% | ACTIVE |  |
| BOT_A (no permanent stop) | Trend / Breakout | +188.5% | +10.4% | -18.1% | 0.97 | 223 | 48% | - |  |
| BOT_B (no permanent stop) | Dip / Mean Reversion | +68.6% | +5.0% | -23.4% | 0.47 | 206 | 67% | - |  |
| BOT_C (no permanent stop) | News + Momentum | +490.9% | +18.1% | -25.8% | 1.08 | 609 | 39% | - |  |
| BOT_D (no permanent stop) | Conservative Confirmation | +53.8% | +4.1% | -14.6% | 0.70 | 313 | 44% | - |  |
| Buy & hold 4 stocks | benchmark | +9661.8% | +53.6% | -60.7% | 1.21 | 0 | - | - |  |
| Buy & hold SPY (S&P 500) | benchmark | +318.6% | +14.4% | -33.8% | 0.86 | 0 | - | - |  |

## Return by year (%, strategies without the permanent stop)

|      |   BOT_A |   BOT_B |   BOT_C |   BOT_D |   Buy & hold 4 stocks |   Buy & hold SPY (S&P 500) |
|-----:|--------:|--------:|--------:|--------:|----------------------:|---------------------------:|
| 2016 |    22.7 |     9.2 |    10.4 |     3.2 |                 140.9 |                       11.8 |
| 2017 |     7   |    15   |    24.8 |     4.8 |                  33   |                       21.7 |
| 2018 |    10.7 |   -10.9 |    14.9 |     0.1 |                  12.2 |                       -5   |
| 2019 |    15.2 |    -0.4 |    41.3 |    11.1 |                 109.8 |                       31.1 |
| 2020 |    17.5 |    19.2 |    44   |    24.5 |                  97.4 |                       18.5 |
| 2021 |     5.6 |    14.2 |    21.9 |    -2   |                  72.4 |                       28.6 |
| 2022 |    -5.3 |   -12.8 |   -18.4 |    -5.3 |                 -49.6 |                      -18.2 |
| 2023 |    23.9 |    18.2 |    37.9 |     7.1 |                 150.2 |                       26.2 |
| 2024 |    20.4 |     9.6 |    24   |     4.4 |                  72.7 |                       24.9 |
| 2025 |     7.8 |    15.4 |     2.9 |     4.9 |                  44.4 |                       17.7 |
| 2026 |    -8.9 |   -14.7 |     4.9 |    -5.7 |                  21   |                        6.8 |

## How this test works

- One decision per trading day at the close, same rules as `bot_runner.py`, 5 bps slippage on every fill.
- BOT_C: the news filter cannot be replayed, so only its price rules are tested (news treated as positive).
- "With live stops" rows apply the live rules (stop forever at -20% or -15% from peak). The "no permanent stop" rows show the strategy itself.
- The 4 stocks were chosen after they became big winners (selection bias), so buy & hold of these 4 looks better than it would have looked in advance.
