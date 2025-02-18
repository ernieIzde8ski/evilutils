"""All the types I don't want to write twice."""

__all__ = [
    "StrPath",
    "Destructor",
    "Getter",
    "Setter",
    "Callable",
    "Newable",
    "strong_cast",
    "HasName",
    "name",
]

from .aliases import StrPath
from .descriptors import Destructor, Getter, Setter
from .dunders import Callable, Newable
from .guards import strong_cast
from .name import HasName, name
