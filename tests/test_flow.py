from openagentflow import Agent, Flow, Message, RuleBasedModel


def test_flow_runs_agents_in_order():
    flow = Flow([Agent("one"), Agent("two")], model=RuleBasedModel({"hello": "first"}))
    result = flow.run([Message.user("hello")])
    assert result.output == "first"
    assert result.steps == 2
    assert len(result.messages) == 3


def test_empty_flow_rejected():
    try:
        Flow([], model=RuleBasedModel({}))
    except ValueError as exc:
        assert "at least one" in str(exc)
    else:
        raise AssertionError("expected ValueError")

