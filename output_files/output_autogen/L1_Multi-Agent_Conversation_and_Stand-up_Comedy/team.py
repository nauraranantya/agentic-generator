
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


cathy = AssistantAgent(
    name="cathy",
    model_client=model_client,
    system_message="""
Role:
stand-up comedian

Goal:
stand-up comedian

Background:
System message as provided at ConversableAgent creation in the notebook.
""",
)


joe = AssistantAgent(
    name="joe",
    model_client=model_client,
    system_message="""
Role:
stand-up comedian

Goal:
stand-up comedian

Background:
System message as provided at ConversableAgent creation in the notebook.
""",
)



team = RoundRobinGroupChat(
    participants=[
        cathy,
        joe,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """
"""
