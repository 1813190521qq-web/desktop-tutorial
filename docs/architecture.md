# Architecture

OpenAgentFlow has four deliberately small layers:

1. Models expose one complete(messages) method, making providers replaceable.
2. Agents add instructions and write outputs to session memory.
3. Flows sequence agents with a bounded step budget and optional callbacks.
4. Skills and workflows hold reusable domain instructions outside runtime code.

The v0.1.0 runtime is synchronous to keep the mental model clear. Streaming, durable checkpoints, retries, and human approval gates are planned extensions. Integrations should remain optional so the core stays easy to install and test.

