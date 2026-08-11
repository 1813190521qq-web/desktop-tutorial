"""Memory abstractions used by agents and flows."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable


class InMemoryStore:
    """Simple session-scoped key/value memory with append-only history."""

    def __init__(self) -> None:
        self._values: dict[str, object] = {}
        self._history: dict[str, list[str]] = defaultdict(list)

    def get(self, key: str, default: object = None) -> object:
        return self._values.get(key, default)

    def set(self, key: str, value: object) -> None:
        self._values[key] = value

    def append(self, session_id: str, item: str) -> None:
        self._history[session_id].append(item)

    def history(self, session_id: str) -> Iterable[str]:
        return tuple(self._history.get(session_id, ()))

