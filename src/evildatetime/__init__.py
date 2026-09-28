__all__ = ["Date", "DateTime", "Duration", "Time", "TimeZone", "TzInfo"]

from datetime import date as Date
from datetime import datetime as DateTime
from datetime import time as Time
from datetime import timedelta as Duration
from datetime import timezone as TimeZone
from datetime import tzinfo as TzInfo

from typing_extensions import deprecated


@deprecated("Deprecated in favor of `Duration`.")
class TimeDelta(Duration):
    pass
