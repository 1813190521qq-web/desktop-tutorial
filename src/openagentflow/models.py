"""Model interfaces and deterministic models for tests and examples."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence


@dataclass(frozen=True, slots=True)
class Message:
    role: str
    content: str

    @classmethod
    def user(cls, content: str) -> "Message":
        return cls("user", content)

    @classmethod
    def assistant(cls, content: str) -> "Message":
        return cls("assistant", content)

    @classmethod
    def system(cls, content: str) -> "Message":
        return cls("system", content)


class Model(Protocol):
    def complete(self, messages: Sequence[Message]) -> str:
        """Return a completion for the supplied conversation."""


class EchoModel:
    """A deterministic model that echoes the latest user message."""

    def complete(self, messages: Sequence[Message]) -> str:
        return next((item.content for item in reversed(messages) if item.role == "user"), "")


class RuleBasedModel:
    """A deterministic model for demos, smoke tests, and local development."""

    def __init__(self, rules: dict[str, str], default: str = "No matching rule.") -> None:
        self.rules = {key.lower(): value for key, value in rules.items()}
        self.default = default

    def complete(self, messages: Sequence[Message]) -> str:
        latest = next((item.content for item in reversed(messages) if item.role == "user"), "")
        for trigger, response in self.rules.items():
            if trigger in latest.lower():
                return response
        return self.default

