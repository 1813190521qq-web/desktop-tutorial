from openagentflow import Agent, Flow, Message, RuleBasedModel

model = RuleBasedModel({"hello": "Hi! What would you like to build with OpenAgentFlow?"})
flow = Flow(
    [Agent("intake", "Understand the request."), Agent("next-step", "Offer one practical next step.")],
    model=model,
)
print(flow.run([Message.user("hello")]).output)

