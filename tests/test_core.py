import pytest

from my_package import greet
from my_package.cli import main


def test_greet() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_strips_whitespace() -> None:
    assert greet("  Ada  ") == "Hello, Ada!"


@pytest.mark.parametrize("bad", ["", "   "])
def test_greet_rejects_empty(bad: str) -> None:
    with pytest.raises(ValueError):
        greet(bad)


def test_cli(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"
