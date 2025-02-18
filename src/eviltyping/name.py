from typing import Protocol, Self

from .descriptors import Getter

__all__ = ["HasName", "name"]


class _HasNameStr(Protocol):
    __name__: str


class _HasNameGetter(Protocol):
    __name__: Getter[str, Self]


type HasName = _HasNameStr | _HasNameGetter
"""An object with a `__name__` string."""


def name(obj: HasName, /) -> str:
    """Returns the name of an object.

    For the name of an object's *type*, consider `type(name(obj))`."""
    return obj.__name__
