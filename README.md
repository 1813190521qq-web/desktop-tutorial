# OpenAgentFlow

[![CI](https://github.com/1813190521qq-web/desktop-tutorial/actions/workflows/ci.yml/badge.svg)](https://github.com/1813190521qq-web/desktop-tutorial/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

OpenAgentFlow is an open-source AI workflow and agent skill framework for building reusable AI capabilities through structured Skills, Workflows, and Knowledge Modules.

OpenAgentFlow addresses an emerging AI engineering challenge: moving beyond experimental prompts toward maintainable, reusable AI systems. It provides open-source architecture, practical workflows, and runnable examples that help developers and teams build agents for real-world applications.

## Why OpenAgentFlow?

Agent applications need more than a chat loop: explicit state, repeatable tools, bounded execution, and a clear place to add policy. OpenAgentFlow provides these primitives without forcing a vendor, orchestration service, or deployment model.

- Composable: build a flow from small agents and typed steps.
- Provider-neutral: implement Model for any local or hosted LLM.
- Safe by default: explicit step limits and state.
- Observable: every run returns structured messages.
- Reusable by design: skills, workflows, knowledge modules, examples, docs, and CI live together.

## Quick start

    python -m venv .venv
    .venv/bin/python -m pip install -e ".[dev]"

    from openagentflow import Agent, Flow, Message, RuleBasedModel
    agent = Agent(name="greeter", instructions="Be concise and friendly.")
    flow = Flow([agent], model=RuleBasedModel({"hello": "Hi from OpenAgentFlow!"}))
    print(flow.run([Message.user("hello")]).output)

Read docs/quickstart.md for a fuller walkthrough and run examples/basic_flow.py.

## Repository layout

    src/openagentflow/   Core runtime, agents, models, memory, and skills
    docs/                Architecture and extension guides
    skills/              Reusable skill manifests and prompt assets
    workflows/           Declarative workflow examples
    knowledge/           Reusable knowledge modules for agent builders
    examples/            Runnable Python examples
    tests/               Fast unit tests
    .github/workflows/   CI automation

## Roadmap

- Streaming events and durable checkpoints
- First-party adapters for popular model providers
- Human approval and policy gates
- Tracing exporters and a workflow visualizer
- A registry for community skills

## Contributing and security

Read CONTRIBUTING.md for local development and PR expectations. Report vulnerabilities privately using SECURITY.md.

OpenAgentFlow is MIT licensed. Issues, ideas, and pull requests are welcome.

