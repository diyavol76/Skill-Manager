"""Agent class that orchestrates skill execution."""

from typing import Any, Dict, Optional

from .skill import Skill


class Agent:
    """An agent that can register and invoke skills by name.

    Usage::

        agent = Agent(name="MyAgent")
        agent.register(CalculatorSkill())
        result = agent.run("calculator", expression="2 + 2")
    """

    def __init__(self, name: str = "Agent") -> None:
        self.name = name
        self._skills: Dict[str, Skill] = {}

    def register(self, skill: Skill) -> None:
        """Register a skill with the agent.

        Args:
            skill: A :class:`Skill` instance to register.

        Raises:
            TypeError: If *skill* is not a :class:`Skill` instance.
            ValueError: If a skill with the same name is already registered.
        """
        if not isinstance(skill, Skill):
            raise TypeError(f"Expected a Skill instance, got {type(skill).__name__}")
        if skill.name in self._skills:
            raise ValueError(f"A skill named {skill.name!r} is already registered.")
        self._skills[skill.name] = skill

    def unregister(self, skill_name: str) -> None:
        """Remove a previously registered skill.

        Args:
            skill_name: The name of the skill to remove.

        Raises:
            KeyError: If no skill with *skill_name* is registered.
        """
        if skill_name not in self._skills:
            raise KeyError(f"No skill named {skill_name!r} is registered.")
        del self._skills[skill_name]

    def run(self, skill_name: str, *args: Any, **kwargs: Any) -> Any:
        """Invoke a registered skill by name.

        Args:
            skill_name: The name of the skill to invoke.
            *args: Positional arguments forwarded to the skill.
            **kwargs: Keyword arguments forwarded to the skill.

        Returns:
            Whatever the skill's ``execute`` method returns.

        Raises:
            KeyError: If no skill with *skill_name* is registered.
        """
        if skill_name not in self._skills:
            raise KeyError(
                f"Skill {skill_name!r} not found. "
                f"Available skills: {list(self._skills)}"
            )
        return self._skills[skill_name].execute(*args, **kwargs)

    def get_skill(self, skill_name: str) -> Optional[Skill]:
        """Return the skill registered under *skill_name*, or ``None``."""
        return self._skills.get(skill_name)

    @property
    def skills(self) -> Dict[str, Skill]:
        """Read-only view of the registered skills keyed by name."""
        return dict(self._skills)

    def __repr__(self) -> str:
        skill_names = list(self._skills)
        return f"<Agent name={self.name!r} skills={skill_names}>"
