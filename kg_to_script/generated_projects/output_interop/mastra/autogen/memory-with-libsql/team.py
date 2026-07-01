
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


chef_agent = AssistantAgent(
    name="chef_agent",
    model_client=model_client,
    system_message="""
Role:
chef

Goal:
chef

Background:
This prompt is set as the chefAgent's instruction/role definition (provided as 'instructions' when the agent is created).
""",
)


memory_agent = AssistantAgent(
    name="memory_agent",
    model_client=model_client,
    system_message="""
Role:
memory

Goal:
memory

Background:
This prompt is set as the memoryAgent's instruction/role definition (provided as 'instructions' when the agent is created).
""",
)



