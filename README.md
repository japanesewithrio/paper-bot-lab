# Paper Bot Lab

A simulation-only strategy lab for **AAPL, NVDA, AMD, and MSFT**. Four independent virtual bots compete with separate $10,000 ledgers.

- **BOT_A** — Trend / Breakout
- **BOT_B** — Dip / Mean Reversion
- **BOT_C** — News + Momentum
- **BOT_D** — Conservative Confirmation

## Safety

This project **does not submit Alpaca brokerage orders**. Alpaca is used only for market clock, market data, and news. The GitHub Actions workflow has a safety guard that fails if common broker-order submission code appears in `bot_runner.py`.

This is an experimental simulation, not financial advice. Simulated fills include a small slippage assumption but still do not reproduce all real-world liquidity, latency, fees, market impact, halts, or execution behavior.

## Required repository secrets

Add these under **Settings → Secrets and variables → Actions**:

- `ALPACA_API_KEY`
- `ALPACA_SECRET_KEY`

Use a fresh Alpaca paper/data key pair. Never commit keys to this repository.

## Automation

GitHub Actions runs every 30 minutes on weekdays across a broad UTC window. `bot_runner.py` checks Alpaca's market clock and exits without changing state when the regular U.S. market is closed, which handles weekends, holidays, and DST changes.

State is persisted in `bot_state.json`; the human-readable latest status is in `reports/latest.md`.
