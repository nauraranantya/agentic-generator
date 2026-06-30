"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - : Define agent 1 goal here
  - : Define agent 2 goal here
Capabilities:
  - web search: Capability to run web searches and return search results.
Resources:
  - : Represents the output produced by task_1_name; used as input to task_2_name. Created by Task_1.
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


def duck_duck_go_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    duck_duck_go_tool

    Description:
    An instance of DuckDuckGoSearchRun created in main.py and intended for web search functionality. (Note: installed via 'duckduckgo-search' if used.)
    """
    return (
        "Tool 'duck_duck_go_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


duck_duck_go_tool = FunctionTool(
    duck_duck_go_tool_impl,
    description="""An instance of DuckDuckGoSearchRun created in main.py and intended for web search functionality. (Note: installed via 'duckduckgo-search' if used.)"""
)


# ==================================================
# Agents
# ==================================================


agent_1_name = AssistantAgent(
    name="agent_1_name",
    model_client=model_client,
    system_message="""
Role:
Define agent 1 role here

Goal:
Define agent 1 goal here

Background:
agent settings: allow_delegation=False; verbose=True; llm=ChatOpenAI(gpt-3.5-turbo)
""",
)


agent_2_name = AssistantAgent(
    name="agent_2_name",
    model_client=model_client,
    system_message="""
Role:
Define agent 2 role here

Goal:
Define agent 2 goal here

Background:
agent settings: allow_delegation=False; verbose=True; llm=ChatOpenAI(gpt-3.5-turbo)
""",
)



