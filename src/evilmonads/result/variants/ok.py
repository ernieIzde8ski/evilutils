from dataclasses import dataclass
from typing import Never, final, override

from ..error import UnwrapError
from ..result import Result


@dataclass(frozen=True)
class _Ok[T](Result[T, Never]):
    val: T

    @override
    def unwrap(self, expected: object = None) -> T:
        return self.val

    @override
    def unwrap_err(self, expected: object = None) -> Never:
        raise UnwrapError(self, expected)


@final
class Ok[T](_Ok[T]):
    val: T


@final
class Some[T](_Ok[T]):
    val: T
