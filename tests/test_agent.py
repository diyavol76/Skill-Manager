"""Tests for the Agent class."""

import pytest

from skill_manager.agent import Agent
from skill_manager.skill import Skill


class DummySkill(Skill):
    @property
    def name(self) -> str:
        return "dummy"

    @property
    def description(self) -> str:
        return "A dummy skill."

    def execute(self, value=42):
        return value


class AnotherSkill(Skill):
    @property
    def name(self) -> str:
        return "another"

    @property
    def description(self) -> str:
        return "Another dummy skill."

    def execute(self):
        return "another_result"


class TestAgentRegister:
    def test_register_skill(self):
        agent = Agent()
        skill = DummySkill()
        agent.register(skill)
        assert "dummy" in agent.skills

    def test_register_non_skill_raises(self):
        agent = Agent()
        with pytest.raises(TypeError, match="Skill instance"):
            agent.register("not a skill")  # type: ignore[arg-type]

    def test_register_duplicate_raises(self):
        agent = Agent()
        agent.register(DummySkill())
        with pytest.raises(ValueError, match="already registered"):
            agent.register(DummySkill())

    def test_skills_property_is_copy(self):
        agent = Agent()
        agent.register(DummySkill())
        skills_copy = agent.skills
        skills_copy["injected"] = DummySkill()
        assert "injected" not in agent.skills


class TestAgentUnregister:
    def test_unregister_skill(self):
        agent = Agent()
        agent.register(DummySkill())
        agent.unregister("dummy")
        assert "dummy" not in agent.skills

    def test_unregister_unknown_raises(self):
        agent = Agent()
        with pytest.raises(KeyError, match="dummy"):
            agent.unregister("dummy")


class TestAgentRun:
    def test_run_known_skill(self):
        agent = Agent()
        agent.register(DummySkill())
        assert agent.run("dummy") == 42

    def test_run_with_argument(self):
        agent = Agent()
        agent.register(DummySkill())
        assert agent.run("dummy", value=99) == 99

    def test_run_unknown_skill_raises(self):
        agent = Agent()
        with pytest.raises(KeyError, match="unknown"):
            agent.run("unknown")

    def test_run_multiple_skills(self):
        agent = Agent()
        agent.register(DummySkill())
        agent.register(AnotherSkill())
        assert agent.run("dummy") == 42
        assert agent.run("another") == "another_result"


class TestAgentGetSkill:
    def test_get_existing_skill(self):
        agent = Agent()
        skill = DummySkill()
        agent.register(skill)
        assert agent.get_skill("dummy") is skill

    def test_get_missing_skill_returns_none(self):
        agent = Agent()
        assert agent.get_skill("missing") is None


class TestAgentRepr:
    def test_repr_contains_name(self):
        agent = Agent(name="TestBot")
        assert "TestBot" in repr(agent)

    def test_repr_contains_skills(self):
        agent = Agent()
        agent.register(DummySkill())
        assert "dummy" in repr(agent)
