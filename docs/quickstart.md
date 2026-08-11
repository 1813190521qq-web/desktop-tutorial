# Quickstart

OpenAgentFlow keeps the core dependency-free so you can prototype before selecting an LLM provider.

## Install

    python -m venv .venv
    .venv/bin/python -m pip install -e ".[dev]"

## Build a flow

An Agent contains role instructions. A Flow executes agents sequentially against a Model implementation.

    from openagentflow import Agent, Flow, Message, RuleBasedModel

    model = RuleBasedModel({"quote": "Share your requirements for a quick quote."})
    flow = Flow([Agent("qualifier", "Extract buyer intent.")], model=model)
    result = flow.run([Message.user("I need a quote for 500 units.")])
    print(result.output)

Implement the Model protocol to connect an API or local model. Keep credentials outside source control and pass request metadata through AgentContext.

