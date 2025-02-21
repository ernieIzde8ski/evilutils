from collections.abc import Mapping

from . import _ensure as _  # noqa: F401

# isort: split

from evilstructs import frozendict


def test_frozendict_can_be_used_as_mapping():
    # This is more of a test of Pyright and my types, if anything
    def first_key(obj: Mapping[str, str]) -> str | None:
        keys = obj.keys()
        return next(iter(keys), None)

    obj = {"abc": "def"}
    assert first_key(obj) == "abc"
    assert first_key(frozendict(obj)) == "abc"
