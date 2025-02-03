from dataclasses import dataclass
from typing import Never, final, override

from evilmonads.result.error import UnwrapError

from ..result import Result


@final
@dataclass(frozen=True)
class Err[E: Exception](Result[Never, E]):
    exc: E

    @override
    def unwrap(self, expected: object = None) -> Never:
        raise UnwrapError(self, expected)

    @override
    def unwrap_err(self, expected: object = None) -> E:
        return self.exc
