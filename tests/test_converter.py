from . import _ensure as _  # noqa: F401

# isort: split

import pytest

from evilconverters import ConversionError, IntFlag, IntFlagMeta, auto


def test_intflagmeta_loads():
    class FooBar(IntFlag, metaclass=IntFlagMeta):
        foo = auto()
        bar = auto()

    assert FooBar.loads("foo") == FooBar.foo

    assert FooBar.loads("foo | bar") == FooBar.foo | FooBar.bar

    with pytest.raises(ConversionError):
        _ = FooBar.loads("")

    with pytest.raises(ConversionError):
        _ = FooBar.loads("foo | ")

    with pytest.raises(ConversionError):
        _ = FooBar.loads(" | foo")

    with pytest.raises(ConversionError):
        _ = FooBar.loads("baz")
