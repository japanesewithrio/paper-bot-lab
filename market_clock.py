"""Market clock helper for the session loop (read-only: only asks Alpaca for the clock).
Prints one of: OPEN / WAIT <seconds-until-next-open>"""
import os
from datetime import datetime, timezone

from alpaca.trading.client import TradingClient

c = TradingClient(os.environ["ALPACA_API_KEY"].strip(), os.environ["ALPACA_SECRET_KEY"].strip(), paper=True).get_clock()
if c.is_open:
    print("OPEN")
else:
    wait = (c.next_open - datetime.now(timezone.utc)).total_seconds()
    print("WAIT %d" % max(wait, 60))
