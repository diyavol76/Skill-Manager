"""Tests for the Skill base class."""

import pytest

from skill_manager.skill import Skill


class ConcreteSkill(Skill):
    @property
    def name(self) -> str:
        return "concrete"

    @property
    def description(self) -> str:
        return "A concrete skill for testing."

    def execute(self, *args, **kwargs):
        return "executed"


class TestSkillABC:
    def test_cannot_instantiate_directly(self):
        with pytest.raises(TypeError):
            Skill()  # type: ignore[abstract]

    def test_concrete_instantiation(self):
        skill = ConcreteSkill()
        assert skill.name == "concrete"
        assert skill.description == "A concrete skill for testing."

    def test_execute(self):
        skill = ConcreteSkill()
        assert skill.execute() == "executed"

    def test_repr(self):
        skill = ConcreteSkill()
        assert "concrete" in repr(skill)
