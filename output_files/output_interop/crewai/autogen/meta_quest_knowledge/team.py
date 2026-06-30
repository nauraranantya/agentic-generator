"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - : Goal expressed in agents configuration to provide best answers to questions about Meta Quest.
Objectives:
  - : Objective assigned to the crew: answer user questions by using available knowledge sources (PDF manual) and agent capabilities.
"""

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


meta_quest_expert = AssistantAgent(
    name="meta_quest_expert",
    model_client=model_client,
    system_message="""
Role:
Meta Quest Expert

Goal:
Goal expressed in agents configuration to provide best answers to questions about Meta Quest.

Background:
Agent-level instruction/backstory used to guide the agent's independent reasoning and responses.
""",
)



