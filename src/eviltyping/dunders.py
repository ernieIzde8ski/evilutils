"""Miscellaneous double-underscore protocols."""

from typing import Protocol

__all__ = ["Callable", "Newable"]


class Callable[**P, RT](Protocol):
    """Like typing.Protocol but it doesn't scream at me for being wrong."""

    def __call__(self, *args: P.args, **kwds: P.kwargs) -> RT: ...


class Newable[**P, RT](Protocol):
    def __new__(cls, *args: P.args, **kwargs: P.kwargs) -> RT: ...
