
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


memory_agent = AssistantAgent(
    name="memory_agent",
    model_client=model_client,
    system_message="""
Role:
assistant

Goal:
assistant

Background:
This prompt is supplied as the 'instructions' argument when creating the Agent instance in source code.
""",
)



