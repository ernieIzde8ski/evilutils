from ._ensure import SRC_DIR

# isort: split

from pathlib import Path

from pytest_case import case

MODULES = list(SRC_DIR.glob("*/"))


def is_python_module(path: Path):
    return (path / "__init__.py").is_file()


def is_typed(py_mod: Path):
    return (py_mod / "py.typed").is_file()


@case((module,) for module in MODULES)
def test_modules_are_typed(path: Path) -> None:
    assert not is_python_module(path) or is_typed(path), (
        f"Module {path} should contain `py.typed` file"
    )
