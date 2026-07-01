"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - : 
Objectives:
  - : 
Capabilities:
  - conversational: Capability to hold a multi-turn conversation and respond to user inputs.
  - memory_update: Capability to update and persist working memory based on conversation content; expects <working_memory> tags to be used in outputs.
  - greet_returning_user: Capability to detect returning users and greet them referencing remembered information.
Resources:
  - : LibSQLStore persistent storage used for Memory. Source code: new LibSQLStore({ id: 'memory-demo-storage', url: 'file:./memory-demo.db' }). File path: file:./memory-demo.db
  - : Simulated resource ID for Alice (source: USERS.alice = 'user-alice-123').
  - : Simulated resource ID for Bob (source: USERS.bob = 'user-bob-456').
  - : Simulated demo user resource ID (source: USERS.demo = 'demo-user-789').
  - : At runtime, a random UUID is used to generate a resource ID (example: user-<uuid>). Represented here as a template; actual UUIDs are generated at runtime.
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


personal_assistant = AssistantAgent(
    name="personal_assistant",
    model_client=model_client,
    system_message="""
Role:
Personal Assistant

Goal:
Personal Assistant

Background:
Agent instructions configured at creation time (Agent.instructions in source code).
""",
)



