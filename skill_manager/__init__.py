"""skill_manager – a lightweight framework for building agents with skills."""

from .agent import Agent
from .skill import Skill
from .skills import CalculatorSkill, EchoSkill, TimeSkill

__all__ = [
    "Agent",
    "Skill",
    "CalculatorSkill",
    "EchoSkill",
    "TimeSkill",
]
