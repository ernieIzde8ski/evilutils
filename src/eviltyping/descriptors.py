"""
Descriptor protocol, as a set of Protocols. See:

https://docs.python.org/3/howto/descriptor.html#descriptor-protocol
"""

import sys
from typing import Generic, Protocol, TypeVar, overload

__all__ = ["Getter", "Setter", "Destructor"]

if sys.version_info < (3, 13):
    # TODO: deprecate support for python 3.12 in late 2027
    _Owner = TypeVar("_Owner", contravariant=True)
    _RT_g = TypeVar("_RT_g", covariant=True)
    _IT = TypeVar("_IT", contravariant=True)
    _RT_d = TypeVar("_RT_d", covariant=True)
else:
    _Owner = TypeVar("_Owner", default=object, contravariant=True)
    # pyright: ignore[reportUnreachable]
    _RT_g = TypeVar("_RT_g", covariant=True)
    _IT = TypeVar("_IT", contravariant=True)
    _RT_d = TypeVar("_RT_d", default=None, covariant=True)

### Methods ###


class Getter(Protocol, Generic[_RT_g, _Owner]):
    @overload
    def __get__(self, instance: _Owner, /) -> _RT_g: ...

    @overload
    def __get__(self, instance: _Owner | None, owner: type[_Owner], /) -> _RT_g: ...

    def __get__(
        self, instance: _Owner | None, owner: type[_Owner] | None = None, /
    ) -> _RT_g:
        """
        Implementation of a non-data descriptor. See:

        https://docs.python.org/3/reference/datamodel.html#object.__get
        """
        ...


class Setter(Protocol, Generic[_IT, _RT_d, _Owner]):
    def __set__(self, instance: _Owner, value: _IT, /) -> _RT_d: ...


class Destructor(Protocol, Generic[_RT_d, _Owner]):
    def __delete__(self, instance: _Owner, /) -> _RT_d: ...
