"""Useful type aliases."""

__all__ = ["StrPath"]

from os import PathLike

type StrPath = str | PathLike[str]
"""Like StrPath from typeshed."""
