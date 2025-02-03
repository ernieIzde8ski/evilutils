from . import _ensure as _  # noqa: F401

# isort: split

from datetime import datetime

import pytest

from evilpath import Path


@pytest.fixture
def this():
    return Path(__file__)


def test_can_get_default_float_times(this: Path) -> None:
    """
    The no-parameter behavior of [amc]time should be
    """
    assert isinstance(this.atime(), float)
    assert isinstance(this.mtime(), float)
    assert isinstance(this.ctime(), float)


def test_can_get_float_times(this: Path) -> None:
    assert isinstance(this.atime(form="float"), float)
    assert isinstance(this.mtime(form="float"), float)
    assert isinstance(this.ctime(form="float"), float)


def test_can_get_datetimes(this: Path) -> None:
    assert isinstance(this.atime(form="datetime"), datetime)
    assert isinstance(this.mtime(form="datetime"), datetime)
    assert isinstance(this.ctime(form="datetime"), datetime)
