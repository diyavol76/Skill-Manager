"""Base class for all skills."""

from abc import ABC, abstractmethod
from typing import Any


class Skill(ABC):
    """Abstract base class that every skill must implement."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique name used to look up this skill."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable description of what this skill does."""

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        """Run the skill and return its result."""

    def __repr__(self) -> str:
        return f"<Skill name={self.name!r}>"
