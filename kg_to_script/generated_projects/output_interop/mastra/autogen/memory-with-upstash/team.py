"""
Auto-generated AutoGen Team: Mastrasystemagentorchestrator
Goals:
  - Improve user's cooking experience: 
Objectives:
  - Help user cook with available ingredients: Collective objective assigned to the Mastra system's agents to assist users in cooking with available ingredients.
Capabilities:
  - Key-value storage capability: Capability representing storing/retrieving messages or data in a key-value store.
  - Vector DB capability: Capability representing vector embedding storage and semantic recall operations.
  - Language model access capability: Capability to invoke and stream responses from a language model.
Resources:
  - User provided ingredients (initial): pasta, canned tomatoes, garlic, olive oil, dried herbs (basil and oregano)
  - Recipe suggestions (initial): Output resource containing brief high-level steps for recipes the Chef Agent suggests given the initial ingredients.
  - User provided ingredients (friend's house): chicken thighs, coconut milk, sweet potatoes, curry powder
  - Recipe suggestions (friend's house): Output resource containing brief high-level steps for recipes suggested for friend's ingredients.
  - Recipe recall output: Memory-influenced response listing what was cooked previously in the same thread/session.
  - src/index.ts (example run description): Describes the example orchestrated run: constructs threadId via randomUUID(); calls agent.stream with user messages; logs streaming chunks to stdout; final call includes memoryOptions { lastMessages: 3 }.
  - src/bubble.ts (message bubble utility - UI/formatting only): A local formatting utility for console output (borders, wrapping). Not modeled as tool used by agents for decision making; included for completeness as a resource artifact.
  - Upstash HTTP store (resource): Represents the Upstash storage resource reachable at http://localhost:8089 with token 'test_token' as in source.
  - PgVector Postgres instance (resource): Represents the Postgres instance used by PgVector (connection string postgresql://postgres:postgres@localhost:5433).
  - thread session resource: Session/thread metadata for a run. threadId is generated using randomUUID() at runtime (source). resourceId used in calls is 'SOME_USER_ID'.
  - Example run (index.ts main()): Sequence executed by src/index.ts: (1) call chefAgent.stream with initial ingredients; (2) call chefAgent.stream with friend's ingredients; (3) call chefAgent.stream to ask what was cooked before with memoryOptions override; then process.exit(0). Each call uses threadId and resourceId parameters; threadId is randomUUID() per run; resourceId set to 'SOME_USER_ID' in source.
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


def memory_storage_upstash_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    UpstashStoreKVstoreadapter

    Description:
    Represents the Upstash HTTP-backed storage used by the memory implementation.
    """
    return (
        "Tool 'memory_storage_upstash_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


memory_storage_upstash_tool = FunctionTool(
    memory_storage_upstash_tool_impl,
    description="""Represents the Upstash HTTP-backed storage used by the memory implementation."""
)


def memory_vector_pg_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    PgVectorPostgresvectorstoreadapter

    Description:
    
    """
    return (
        "Tool 'memory_vector_pg_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


memory_vector_pg_tool = FunctionTool(
    memory_vector_pg_tool_impl,
    description=""""""
)


def open_ai_sdk_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    OpenAISDKclientconceptualtool

    Description:
    Conceptual representation of the OpenAI client used to call gpt-4o. SDK details are not modeled; configuration captured as literals.
    """
    return (
        "Tool 'open_ai_sdk_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


open_ai_sdk_tool = FunctionTool(
    open_ai_sdk_tool_impl,
    description="""Conceptual representation of the OpenAI client used to call gpt-4o. SDK details are not modeled; configuration captured as literals."""
)


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
Agent-level instructions for Chef Agent; used as persistent agent prompt.
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
Agent-level instructions for Memory Agent; used as persistent agent prompt.
""",
)



