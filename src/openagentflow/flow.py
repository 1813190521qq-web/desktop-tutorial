"""Sequential workflow orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .agent import Agent, AgentContext
from .models import Message, Model


@dataclass(frozen=True, slots=True)
class FlowResult:
    output: str
    messages: tuple[Message, ...]
    steps: int


class Flow:
    """Run agents in order, passing each completion to the next step."""

    def __init__(self, agents: list[Agent], model: Model, max_steps: int = 20) -> None:
        if not agents:
            raise ValueError("a flow needs at least one agent")
        if max_steps < 1:
            raise ValueError("max_steps must be positive")
        self.agents = agents
        self.model = model
        self.max_steps = max_steps

    def run(self, messages: list[Message], context: AgentContext | None = None, on_step: Callable[[int, Agent, Message], None] | None = None) -> FlowResult:
        state = list(messages)
        context = context or AgentContext()
        for index, agent in enumerate(self.agents[: self.max_steps]):
            response = agent.run(state, self.model, context)
            state.append(response)
            if on_step:
                on_step(index, agent, response)
        return FlowResult(output=state[-1].content if state else "", messages=tuple(state), steps=min(len(self.agents), self.max_steps))

