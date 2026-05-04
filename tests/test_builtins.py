"""Tests for built-in skills."""

import datetime

import pytest

from skill_manager.skills import CalculatorSkill, EchoSkill, TimeSkill


class TestCalculatorSkill:
    def setup_method(self):
        self.skill = CalculatorSkill()

    def test_name(self):
        assert self.skill.name == "calculator"

    def test_addition(self):
        assert self.skill.execute("1 + 1") == 2.0

    def test_subtraction(self):
        assert self.skill.execute("10 - 4") == 6.0

    def test_multiplication(self):
        assert self.skill.execute("3 * 7") == 21.0

    def test_division(self):
        assert self.skill.execute("10 / 4") == 2.5

    def test_floor_division(self):
        assert self.skill.execute("10 // 3") == 3.0

    def test_modulo(self):
        assert self.skill.execute("10 % 3") == 1.0

    def test_exponentiation(self):
        assert self.skill.execute("2 ** 10") == 1024.0

    def test_math_function(self):
        assert self.skill.execute("sqrt(16)") == 4.0

    def test_math_constant(self):
        import math
        result = self.skill.execute("pi")
        assert abs(result - math.pi) < 1e-10

    def test_invalid_expression_raises(self):
        with pytest.raises(ValueError, match="Invalid expression"):
            self.skill.execute("not_a_number()")

    def test_non_numeric_result_raises(self):
        with pytest.raises(ValueError):
            self.skill.execute("'hello'")

    def test_builtin_access_blocked(self):
        with pytest.raises(ValueError):
            self.skill.execute("__import__('os')")


class TestEchoSkill:
    def setup_method(self):
        self.skill = EchoSkill()

    def test_name(self):
        assert self.skill.name == "echo"

    def test_echo_string(self):
        assert self.skill.execute("hello") == "hello"

    def test_echo_number(self):
        assert self.skill.execute(42) == 42

    def test_echo_none(self):
        assert self.skill.execute(None) is None

    def test_echo_list(self):
        data = [1, 2, 3]
        assert self.skill.execute(data) is data


class TestTimeSkill:
    def setup_method(self):
        self.skill = TimeSkill()

    def test_name(self):
        assert self.skill.name == "time"

    def test_returns_datetime(self):
        result = self.skill.execute()
        assert isinstance(result, datetime.datetime)

    def test_returns_utc(self):
        result = self.skill.execute()
        assert result.tzinfo == datetime.timezone.utc
