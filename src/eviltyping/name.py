from typing import Protocol, Self

from .descriptors import Getter

__all__ = ["HasName", "name"]


class HasName(Protocol):
    __name__: str | Getter[str, "Self"]


def name(obj: HasName, /) -> str:
    """Returns the name of an object.

    For the name of an object's *type*, consider `type(name(obj))`."""
    return obj.__name__
