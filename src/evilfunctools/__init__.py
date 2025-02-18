"""Extensions upon the `functools` library."""

from functools import cache, cached_property, partial, partialmethod, wraps

from .compose import compose
from .decorators import immediate

__all__ = [
    "cache",
    "cached_property",
    "compose",
    "immediate",
    "partial",
    "partialmethod",
    "wraps",
]
