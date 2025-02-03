"""All the types I don't want to write twice."""

__all__ = ["Getter", "HasName", "name", "StrPath", "Callable", "Newable", "strong_cast"]

from os import PathLike
from typing import TYPE_CHECKING, Any, Protocol, TypeVar

from .dunder import Getter, HasName, name

type StrPath = str | PathLike[str]
"""Like StrPath from typeshed."""


class Callable[**P, RT](Protocol):
    """Like typing.Protocol but it doesn't scream at me for being wrong."""

    def __call__(self, *args: P.args, **kwds: P.kwargs) -> RT: ...


class Newable[**P, RT](Protocol):
    def __new__(cls, *args: P.args, **kwargs: P.kwargs) -> RT: ...


if TYPE_CHECKING:

    def strong_cast[T](
        _type: type[T] | TypeVar,
        _value: Any,  # pyright: ignore[reportAny, reportExplicitAny]
        /,
    ) -> T: ...

else:

    def strong_cast[T](_type, _value):
        return _value
