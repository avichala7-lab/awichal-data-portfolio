"""Command-line calculator supporting basic operations.

Usage examples:
    python simple_calculator.py add 5 7
    python simple_calculator.py multiply 3 4 2
    python simple_calculator.py divide 10 2
"""

from __future__ import annotations

import argparse
from functools import reduce
from typing import Callable, Iterable, List


def add(numbers: Iterable[float]) -> float:
    """Return the sum of the provided numbers."""

    return sum(numbers)


def subtract(numbers: Iterable[float]) -> float:
    """Subtract all subsequent numbers from the first number."""

    numbers = list(numbers)
    if not numbers:
        raise ValueError("At least one number is required for subtraction.")
    return numbers[0] - sum(numbers[1:])


def multiply(numbers: Iterable[float]) -> float:
    """Return the product of the provided numbers."""

    return reduce(lambda x, y: x * y, numbers, 1)


def divide(numbers: Iterable[float]) -> float:
    """Divide the first number by each subsequent number."""

    numbers = list(numbers)
    if not numbers:
        raise ValueError("At least one number is required for division.")

    def _safe_divide(x: float, y: float) -> float:
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y

    return reduce(_safe_divide, numbers[1:], numbers[0])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple command-line calculator")
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform",
    )
    parser.add_argument("numbers", nargs="+", type=float, help="Numbers to calculate")
    return parser


def main(argv: List[str] | None = None) -> float:
    parser = build_parser()
    args = parser.parse_args(argv)

    operations: dict[str, Callable[[Iterable[float]], float]] = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    result = operations[args.operation](args.numbers)
    print(result)
    return result


if __name__ == "__main__":
    main()
