"""Type guards and such."""

__all__ = ["strong_cast"]

from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:

    def strong_cast[T](
        _type: type[T] | TypeVar,
        _value: Any,  # pyright: ignore[reportAny, reportExplicitAny]
        /,
    ) -> T: ...

else:

    def strong_cast[T](_type, _value):
        return _value
