# Contributing to OpenAgentFlow

Thanks for helping make reliable agent workflows easier to build.

## Development setup

Create a virtual environment, then install development dependencies:

    python -m venv .venv
    .venv/bin/python -m pip install -e ".[dev]"

On Windows, use .venv\\Scripts\\python. Before opening a pull request, run:

    ruff check .
    pytest

## Guidelines

- Keep changes focused and add tests for behavior changes.
- Use type annotations and concise docstrings for public APIs.
- Keep provider SDKs optional; the core has no runtime dependencies.
- Never commit API keys, tokens, or private customer data.
- Update docs and examples when a public API changes.

Contributions are licensed under the MIT License. Be respectful, constructive, and inclusive.

