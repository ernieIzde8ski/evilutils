from typing import Protocol

__all__ = ["Getter", "HasName", "name"]


class Getter[T, Owner](Protocol):
    def __get__(self, instance: Owner, owner: type[Owner] | None = None, /) -> T: ...


class _HasName[T](Protocol):
    __name__: T


type HasName = _HasName[str] | _HasName[Getter[str, HasName]]


def name(obj: HasName) -> str:
    return obj.__name__
