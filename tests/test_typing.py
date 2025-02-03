from . import _ensure as _  # noqa: F401

# isort: split

import pytest

from eviltyping import name


def test_classes_have_names():
    assert isinstance(name(str), str)


def test_instances_dont():
    with pytest.raises(AttributeError):
        assert isinstance(name(object()), str)  # pyright: ignore[reportArgumentType]
