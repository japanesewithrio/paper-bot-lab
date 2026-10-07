from bot_runner import Signal, can_open_position, should_enter, should_exit, simulated_fill


def sig(**kw):
    base = dict(price=110.0, sma20=100.0, sma50=90.0, rsi14=55.0, ret5_pct=2.0,
                prior20_high=105.0, zscore20=0.5, news_score=0, news_headlines=())
    base.update(kw)
    return Signal(**base)


def test_entries():
    assert should_enter("BOT_A", sig())
    assert should_enter("BOT_B", sig(rsi14=30, zscore20=-1.5, price=80))
    assert should_enter("BOT_C", sig(news_score=1, ret5_pct=2, price=110, sma20=100))
    assert should_enter("BOT_D", sig(rsi14=60, ret5_pct=3, news_score=0))


def test_exits():
    assert should_exit("BOT_A", sig(price=95, sma20=100), 0)[0]
    assert should_exit("BOT_B", sig(price=101, sma20=100), 0)[0]
    assert should_exit("BOT_C", sig(news_score=-1), 0)[0]
    assert should_exit("BOT_D", sig(rsi14=80), 0)[0]


def test_same_day_reentry_and_max_positions():
    bot = {"positions": {}, "last_exit_date": {"AAPL": "2026-10-07"}}
    assert not can_open_position(bot, "AAPL", "2026-10-07")
    bot = {"positions": {"A": {}, "B": {}, "C": {}}, "last_exit_date": {}}
    assert not can_open_position(bot, "D", "2026-10-07")


def test_slippage_is_adverse():
    assert simulated_fill(100, "BUY") > 100
    assert simulated_fill(100, "SELL") < 100
