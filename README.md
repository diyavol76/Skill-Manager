# Skill-Manager

A lightweight Python framework for building **agents** with pluggable **skills**.

---

## Overview

```
skill_manager/
├── agent.py          # Agent class – registers and runs skills
├── skill.py          # Abstract Skill base class
└── skills/
    └── builtins.py   # Built-in skills: calculator, echo, time
```

---

## Installation

```bash
pip install -e .
```

---

## Quick Start

```python
from skill_manager import Agent, CalculatorSkill, EchoSkill, TimeSkill

# Create an agent
agent = Agent(name="MyAgent")

# Register skills
agent.register(CalculatorSkill())
agent.register(EchoSkill())
agent.register(TimeSkill())

# Run skills
print(agent.run("calculator", expression="sqrt(144)"))  # 12.0
print(agent.run("echo", message="Hello, world!"))       # Hello, world!
print(agent.run("time"))                                # 2026-05-04 ...
```

---

## Creating a Custom Skill

Subclass `Skill` and implement three members:

```python
from skill_manager import Agent, Skill

class GreetSkill(Skill):
    @property
    def name(self) -> str:
        return "greet"

    @property
    def description(self) -> str:
        return "Greet a person by name."

    def execute(self, person: str) -> str:
        return f"Hello, {person}!"

agent = Agent()
agent.register(GreetSkill())
print(agent.run("greet", person="Alice"))  # Hello, Alice!
```

---

## Built-in Skills

| Name         | Description                                  |
|--------------|----------------------------------------------|
| `calculator` | Evaluate arithmetic expressions (uses `math` module). |
| `echo`       | Return the input message unchanged.          |
| `time`       | Return the current UTC datetime.             |

---

## Running Tests

```bash
pip install pytest
pytest
```
