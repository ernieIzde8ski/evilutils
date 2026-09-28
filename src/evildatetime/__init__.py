__all__ = ["Date", "DateTime", "Duration", "Seconds", "Time", "TimeZone", "TzInfo"]

from datetime import date as Date
from datetime import datetime as DateTime
from datetime import time as Time
from datetime import timedelta
from datetime import timezone as TimeZone
from datetime import tzinfo as TzInfo
from typing import Self
from typing import overload
from typing import override

from typing_extensions import deprecated


class Duration(timedelta):
    @classmethod
    def from_seconds(cls, seconds: float) -> Self:
        return cls(seconds=seconds)

    @classmethod
    def from_milliseconds(cls, milliseconds: float) -> Self:
        return cls(milliseconds=milliseconds)


class Seconds(Duration):
    @overload
    def __new__(cls, inst: Duration, /) -> Self: ...

    @overload
    def __new__(cls, seconds: float = 0) -> Self: ...

    @override
    def __new__(cls, seconds: Duration | float = 0) -> Self:
        if isinstance(seconds, Duration):
            seconds = seconds.total_seconds()
        return super().__new__(cls, seconds=seconds)

    @override
    def __str__(self):
        return f"{self.total_seconds():.2f}s"


@deprecated("Deprecated in favor of `Duration`.")
class TimeDelta(timedelta):
    pass
