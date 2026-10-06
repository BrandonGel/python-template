"""Command-line interface."""

import argparse
from collections.abc import Sequence

from my_package.core import greet


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="my-package", description="Greet someone.")
    parser.add_argument("name", help="Name to greet")
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
