# Paper Bot Lab

A simulation-only strategy lab for **AAPL, NVDA, AMD, and MSFT**. Four independent virtual bots compete with separate $10,000 ledgers.

- **BOT_A** — Trend / Breakout
- **BOT_B** — Dip / Mean Reversion
- **BOT_C** — News + Momentum
- **BOT_D** — Conservative Confirmation

## Safety

This project **does not submit Alpaca brokerage orders**. Alpaca is used only for market clock, market data, and news. The GitHub Actions workflow has a safety guard that fails if common broker-order submission code appears in `bot_runner.py`.

This is an experimental simulation, not financial advice. Simulated fills include a small slippage assumption but still do not reproduce all real-world liquidity, latency, fees, market impact, halts, or execution behavior.

## Backtest

`backtest.py` (workflow **Paper Bot Lab backtest**, run by hand) replays the same rules on daily bars since 2016,
for the 4-stock watchlist and for the 28 largest US companies of early 2016. Results: `reports/backtest.md`.
It showed that stopping a bot forever after a drawdown hurt every strategy, so the live rule is now a
28-day cooldown followed by a restart.

## Required repository secrets

Add these under **Settings → Secrets and variables → Actions**:

- `ALPACA_API_KEY`
- `ALPACA_SECRET_KEY`

Use a fresh Alpaca paper/data key pair. Never commit keys to this repository.

## Automation

GitHub's scheduler drops most scheduled runs (some days none at all), so the workflow keeps itself alive as a relay: each run trades every 30 minutes while the market is open, or waits for the next open, for up to ~5h40m, then starts the next run itself. The schedule only restarts the relay if it ever breaks. `market_clock.py` only reads Alpaca's market clock, which handles weekends, holidays, and DST changes.

State is persisted in `bot_state.json`; the human-readable latest status is in `reports/latest.md`.
