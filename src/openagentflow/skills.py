"""Reusable skill definitions."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Skill:
    name: str
    description: str
    instructions: str = ""

    def render(self) -> str:
        return ("## " + self.name + "\n" + self.description + "\n" + self.instructions).strip()

