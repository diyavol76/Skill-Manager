"""Built-in skills: CalculatorSkill, EchoSkill, TimeSkill."""

import datetime
import math
import operator
from typing import Any

from ..skill import Skill

_SAFE_OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow,
}

_SAFE_NAMES: dict = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}


class CalculatorSkill(Skill):
    """Evaluate simple arithmetic expressions safely.

    Supported: ``+``, ``-``, ``*``, ``/``, ``//``, ``%``, ``**``, and all
    :mod:`math` functions/constants (e.g. ``sqrt``, ``pi``).

    Example::

        skill = CalculatorSkill()
        skill.execute("2 ** 10")   # 1024.0
        skill.execute("sqrt(16)")  # 4.0
    """

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "Evaluate an arithmetic expression and return the numeric result."

    def execute(self, expression: str) -> float:
        """Evaluate *expression* and return the result as a float.

        Args:
            expression: A string containing the arithmetic expression.

        Returns:
            The numeric result.

        Raises:
            ValueError: If the expression is invalid or unsafe.
        """
        try:
            result = eval(  # noqa: S307
                expression,
                {"__builtins__": {}},
                _SAFE_NAMES,
            )
        except Exception as exc:
            raise ValueError(f"Invalid expression {expression!r}: {exc}") from exc
        if not isinstance(result, (int, float)):
            raise ValueError(f"Expression did not produce a number: {result!r}")
        return float(result)


class EchoSkill(Skill):
    """Return the input message unchanged.

    Useful for testing the agent pipeline.

    Example::

        skill = EchoSkill()
        skill.execute("hello")  # "hello"
    """

    @property
    def name(self) -> str:
        return "echo"

    @property
    def description(self) -> str:
        return "Echo back the provided message unchanged."

    def execute(self, message: Any) -> Any:
        """Return *message* as-is."""
        return message


class TimeSkill(Skill):
    """Return the current UTC date and time.

    Example::

        skill = TimeSkill()
        skill.execute()  # datetime.datetime(...)
    """

    @property
    def name(self) -> str:
        return "time"

    @property
    def description(self) -> str:
        return "Return the current UTC date and time as a datetime object."

    def execute(self) -> datetime.datetime:
        """Return the current UTC datetime."""
        return datetime.datetime.now(datetime.timezone.utc)
