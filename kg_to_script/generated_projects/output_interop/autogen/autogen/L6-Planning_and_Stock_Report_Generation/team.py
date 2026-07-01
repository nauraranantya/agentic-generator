
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


admin = AssistantAgent(
    name="admin",
    model_client=model_client,
    system_message="""
Role:
Admin

Goal:
Admin

Background:
You are a Admin.
""",
)


planner = AssistantAgent(
    name="planner",
    model_client=model_client,
    system_message="""
Role:
Planner

Goal:
Planner

Background:
You are a Planner.
""",
)


engineer = AssistantAgent(
    name="engineer",
    model_client=model_client,
    system_message="""
Role:
Engineer

Goal:
Engineer

Background:
You are a Engineer.
""",
)


executor = AssistantAgent(
    name="executor",
    model_client=model_client,
    system_message="""
Role:
Executor

Goal:
Executor

Background:
You are a Executor.
""",
)


writer = AssistantAgent(
    name="writer",
    model_client=model_client,
    system_message="""
Role:
Writer

Goal:
Writer

Background:
You are a Writer.
""",
)


group_chat_manager = AssistantAgent(
    name="group_chat_manager",
    model_client=model_client,
    system_message="""
Role:
GroupChatManager

Goal:
GroupChatManager

Background:
You are a GroupChatManager.
""",
)



