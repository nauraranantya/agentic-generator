"""
Auto-generated AutoGen Team: Mastraagenticsystem
Goals:
  - Play Heads-Up Game: Top-level goal for the workflow/system: enable a complete game session and determine if the player guesses the famous person correctly.
Objectives:
  - Heads-Up game objective: Objective: run an interactive Heads-Up guessing game to let the user identify a famous person via yes/no questions and guesses.
Resources:
  - heads-up-game: Persistent memory/resource ID used by FamousPersonAgent and by the workflow memory thread 'famous-person-generator'.
  - famousPerson (resource): String resource holding the generated famous person's name produced by the start-step task.
  - guessCount (resource): Integer resource tracking the number of guesses made by the user; produced & updated by the workflow.
  - agentResponse (resource): String resource containing the textual response from the Game Agent on a user question or guess.
  - gameWon (resource): Boolean-like resource indicating whether the game has been won (true) or not (false). The runtime must treat this as a boolean flag produced by the Game Agent's structured output.
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


def lib_sql_store_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    LibSQLStorestorage

    Description:
    Persistent storage provider used by the Mastra system to store observability and memory state (file:../mastra.db).
    """
    return (
        "Tool 'lib_sql_store_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


lib_sql_store_tool = FunctionTool(
    lib_sql_store_tool_impl,
    description="""Persistent storage provider used by the Mastra system to store observability and memory state (file:../mastra.db)."""
)


def lib_sql_vector_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    LibSQLVectorvectorDBadapter

    Description:
    Vector store adapter used by agent Memory to store/retrieve embeddings.
    """
    return (
        "Tool 'lib_sql_vector_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


lib_sql_vector_tool = FunctionTool(
    lib_sql_vector_tool_impl,
    description="""Vector store adapter used by agent Memory to store/retrieve embeddings."""
)


# ==================================================
# Agents
# ==================================================


famous_person_generator = AssistantAgent(
    name="famous_person_generator",
    model_client=model_client,
    system_message="""
Role:
generator

Goal:
generator

Background:
Agent instructions and constraints for generating a single famous person's name.
""",
)


game_agent = AssistantAgent(
    name="game_agent",
    model_client=model_client,
    system_message="""
Role:
game-assistant

Goal:
game-assistant

Background:
Agent instructions and required structured JSON output (response, gameWon).
""",
)


guess_verifier_agent = AssistantAgent(
    name="guess_verifier_agent",
    model_client=model_client,
    system_message="""
Role:
verifier

Goal:
verifier

Background:
You are a verifier.
""",
)



