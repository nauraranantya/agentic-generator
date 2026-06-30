
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


recruiter_agent = AssistantAgent(
    name="recruiter_agent",
    model_client=model_client,
    system_message="""
Role:
Recruiter Agent

Goal:
Recruiter Agent

Background:
Agent-level static instruction used as the recruiter's persona/instruction set for generation.
""",
)



