from abc import ABC, abstractmethod
from typing import Never

from .error import UnwrapError

__all__ = ["Result"]


class Result[T, E: Exception | None](ABC):
    """Base class for all `Result` types."""

    def _bad_unwrap(self, expected: object = None) -> Never:
        raise UnwrapError(self, expected)

    @abstractmethod
    def unwrap(self, expected: object = None) -> T: ...

    @abstractmethod
    def unwrap_err(self, expected: object = None) -> E: ...
