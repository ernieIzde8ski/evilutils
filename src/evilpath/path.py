import pathlib
from datetime import datetime
from typing import Literal, overload

__all__ = ["Path"]


class Path(pathlib.Path):
    """Evil extensions to `pathlib`'s `Path` class."""

    @overload
    def atime(self, *, form: Literal["datetime"]) -> datetime: ...
    @overload
    def atime(self, *, form: Literal["float"] = "float") -> float: ...
    def atime(self, *, form: Literal["float", "datetime"] = "float"):
        """Time of last access."""
        res = self.stat().st_atime
        return res if form == "float" else datetime.fromtimestamp(res)

    @overload
    def mtime(self, *, form: Literal["datetime"]) -> datetime: ...
    @overload
    def mtime(self, *, form: Literal["float"] = "float") -> float: ...
    def mtime(self, *, form: Literal["float", "datetime"] = "float"):
        """Time of last modification."""
        res = self.stat().st_mtime
        return res if form == "float" else datetime.fromtimestamp(res)

    @overload
    def ctime(self, *, form: Literal["datetime"]) -> datetime: ...
    @overload
    def ctime(self, *, form: Literal["float"] = "float") -> float: ...
    def ctime(self, *, form: Literal["float", "datetime"] = "float"):
        """Time of last change."""
        res = self.stat().st_ctime
        return res if form == "float" else datetime.fromtimestamp(res)
