from openagentflow import InMemoryStore


def test_memory_is_session_scoped():
    memory = InMemoryStore()
    memory.append("a", "one")
    memory.append("b", "two")
    assert tuple(memory.history("a")) == ("one",)
    assert tuple(memory.history("b")) == ("two",)

