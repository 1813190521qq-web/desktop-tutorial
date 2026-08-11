"""Agent execution primitives."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .memory import InMemoryStore
from .models import Message, Model


@dataclass(slots=True)
class AgentContext:
    session_id: str = "default"
    metadata: dict[str, Any] = field(default_factory=dict)
    memory: InMemoryStore = field(default_factory=InMemoryStore)


class Agent:
    """An agent that turns conversation state into a model completion."""

    def __init__(self, name: str, instructions: str = "") -> None:
        if not name.strip():
            raise ValueError("agent name must not be empty")
        self.name = name
        self.instructions = instructions

    def run(self, messages: list[Message], model: Model, context: AgentContext | None = None) -> Message:
        context = context or AgentContext()
        prompt = list(messages)
        if self.instructions:
            prompt.insert(0, Message.system(self.instructions))
        output = model.complete(prompt)
        context.memory.append(context.session_id, output)
        return Message.assistant(output)

