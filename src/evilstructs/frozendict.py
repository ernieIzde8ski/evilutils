__all__ = ["frozendict"]


from collections.abc import Hashable, Iterable, Iterator, Mapping
from typing import TYPE_CHECKING, override

from eviltyping import name

if TYPE_CHECKING:
    from _typeshed import SupportsKeysAndGetItem


class ToDo(NotImplementedError):
    pass


class frozendict[KT, VT](Mapping[KT, VT]):
    """An immutable implementation of Mapping."""

    # TODO: support Pydantic, pprint
    __store: dict[KT, VT]
    __as_str: str | None = None
    __as_repr: str | None = None
    __as_hash: int | None = None

    def __init__(
        self,
        obj: "SupportsKeysAndGetItem[KT, VT] | Iterable[tuple[KT, VT]] | None" = None,
        /,
    ) -> None:
        if obj is None:
            self.__store = {}
        else:
            self.__store = dict(obj)

    @override
    def __iter__(self) -> Iterator[KT]:
        yield from self.__store

    @override
    def __len__(self) -> int:
        return len(self.__store)

    @override
    def __getitem__(self, key: KT, /) -> VT:
        return self.__store[key]

    @override
    def __str__(self) -> str:
        if self.__as_str is None:
            self.__as_str = str(self.__store)
        return self.__as_str

    @override
    def __repr__(self) -> str:
        if self.__as_repr is None:
            self.__as_repr = name(type(self)) + " " + repr(self.__store)
        return self.__as_repr

    @override
    def __hash__(self: "frozendict[Hashable, Hashable]") -> int:
        if self.__as_hash is None:
            self.__as_hash = hash(tuple(self.items()))
        return self.__as_hash

    @override
    def __contains__(self, key: object) -> bool:
        return key in self.__store
