
from autogen_agentchat.agents import AssistantAgent

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import (

    MaxMessageTermination

)

from autogen_core.tools import FunctionTool

from autogen_ext.models.openai import (
    OpenAIChatCompletionClient
)

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini"
)


# ==================================================
# Generated Tool Stubs
# ==================================================


# ==================================================
# Agents
# ==================================================


chat_agent_1 = AssistantAgent(
    name="chat_agent_1",
    model_client=model_client,
    system_message="""
Role:
conversational assistant

Goal:
conversational assistant

Background:
This system role message is prepended to every model invocation in the chat node.
""",
)



