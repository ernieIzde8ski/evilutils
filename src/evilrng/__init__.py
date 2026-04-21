from collections.abc import Callable, Sequence
from functools import partial
from random import Random
from typing import TYPE_CHECKING, final, overload

if TYPE_CHECKING:
    from _typeshed import SupportsLenAndGetItem

__all__ = ["RNG"]


@final
class RNG:
    """An alternative API to `random.Random`.

    For now, this class cannot be subclassed. Pass a subclass of `Random` as
    the first parameter instead.
    """

    @overload
    def __init__(self, wrapped: Random, /) -> None: ...

    @overload
    def __init__(
        self, seed: int | float | str | bytes | bytearray | None = None
    ) -> None: ...

    def __init__(
        self, seed: Random | int | float | str | bytes | bytearray | None = None
    ) -> None:
        self.__inst = seed if isinstance(seed, Random) else Random(seed)

    @property
    def unit(self) -> Callable[[], float]:
        return self.__inst.random

    @overload
    def choice[T](
        self,
        population: "SupportsLenAndGetItem[T]",
        /,
        k: None = None,
        weights: Sequence[float] | None = None,
        cumulative: bool = False,
    ) -> T: ...

    @overload
    def choice[T](
        self,
        population: "SupportsLenAndGetItem[T]",
        /,
        k: int,
        weights: Sequence[float] | None = None,
        cumulative: bool = False,
    ) -> Sequence[T]: ...

    def choice[T](
        self,
        population: "SupportsLenAndGetItem[T]",
        /,
        k: int | None = None,
        weights: Sequence[float] | None = None,
        cumulative: bool = False,
    ) -> T | Sequence[T]:
        if weights is None and k is None:
            return self.__inst.choice(population)
        choices = self.__inst.choices
        with_weights = (
            partial(choices, cum_weights=weights)
            if cumulative
            else partial(choices, weights=weights)
        )

        result = with_weights(population, k=1 if k is None else k)
        return result[0] if k is None else result


_inst = RNG()
