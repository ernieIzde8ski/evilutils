import re
from collections.abc import Generator, Iterable
from enum import IntFlag, auto
from functools import reduce

__all__ = ["auto", "IntFlag", "IntFlagMeta"]

try:
    from .error import ConversionError
except ImportError:
    if __name__ == "__main__":
        ConversionError = RuntimeError
    else:
        raise

_split_word_boundaries = re.compile(r"\b").split


def split_word_boundaries(__s: str):
    for word in _split_word_boundaries(__s):
        word = word.strip()
        if word:
            yield word


# todo: native Pydantic support when Pydantic is available
class IntFlagMeta(type(IntFlag)):
    def loads(self, __s: str, /):
        def iter_flags(args: Iterable[str]) -> Generator[IntFlagMeta]:
            i = 0
            last_yield = None

            for i, arg in enumerate(args):
                match (i % 2 == 0, arg):
                    case (True, "|"):
                        raise ConversionError(
                            f"Expected a flag, got a pipe at element #{i}"
                        )
                    case (False, "|"):
                        pass
                    case (True, flag):
                        last_yield = self[arg]
                        yield last_yield
                    case (False, flag):
                        raise ConversionError(
                            f"Expected a pipe, got a flag at element #{i} ({flag = })"
                        )

            if last_yield is not None and i % 2 == 1:
                raise ConversionError(
                    f"Expected word after pipe at element #{i} (after flag: {last_yield!r})"
                )

        try:
            args = split_word_boundaries(__s)
            flags = iter_flags(args)
            flag = reduce(lambda f, g: f | g, flags)
            return flag
        except Exception as exc:
            if isinstance(exc, ConversionError):
                raise
            else:
                raise ConversionError("An internal exception occurred.") from exc
