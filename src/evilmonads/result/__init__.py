"""All the monads I don't want to write twice."""

__all__ = ["UnwrapError", "Err", "Null", "Ok", "Result", "Option", "catch_unwind"]


from dataclasses import dataclass
from functools import wraps
from typing import Callable

from .error import UnwrapError
from .variants import Err, Null, Ok, Some

type Result[T, E: Exception] = Ok[T] | Err[E]
type Option[T] = Some[T] | Null


@dataclass
class catch_unwind[**P, T, E: Exception]:
    """Wraps a function and prevents it from raising the given exception(s)."""

    exc: type[E]

    def __call__(self, func: Callable[P, T]) -> Callable[P, Result[T, E]]:
        @wraps(func)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> Result[T, E]:
            try:
                res = func(*args, **kwargs)
                return Ok(res)
            except self.exc as exc:
                return Err(exc)

        return wrapped
