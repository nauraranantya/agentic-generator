
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
# Environment Configuration
# ==================================================
# Environment:  (local-development)
# Configuration indicates use of localhost postgres and local services (from source code constants).

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
Chef

Goal:
Chef

Background:
Agent-level instructions used as the system persona for the Chef Agent.
""",
)


memory_agent = AssistantAgent(
    name="memory_agent",
    model_client=model_client,
    system_message="""
Role:
Memory

Goal:
Memory

Background:
Agent-level instructions used as the system persona for the Memory Agent.
""",
)



