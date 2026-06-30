
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


def weaviate_vector_search_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    WeaviateVectorSearchTool

    Description:
    Vector search tool configured to query a Weaviate collection (WeaviateBlogChunk).
    """
    return (
        "Tool 'weaviate_vector_search_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


weaviate_vector_search_tool = FunctionTool(
    weaviate_vector_search_tool_impl,
    description="""Vector search tool configured to query a Weaviate collection (WeaviateBlogChunk)."""
)


def serper_dev_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SerperDevWebSearchTool

    Description:
    Web search tool (SerperDev) used to retrieve web search results for background research.
    """
    return (
        "Tool 'serper_dev_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


serper_dev_tool = FunctionTool(
    serper_dev_tool_impl,
    description="""Web search tool (SerperDev) used to retrieve web search results for background research."""
)


# ==================================================
# Agents
# ==================================================


biomed_agent_1 = AssistantAgent(
    name="biomed_agent_1",
    model_client=model_client,
    system_message="""
Role:
Industry researcher focused on biomedical trends and their applications in AI

Goal:
Industry researcher focused on biomedical trends and their applications in AI

Background:
You are a Industry researcher focused on biomedical trends and their applications in AI.
""",
)


healthcare_agent_1 = AssistantAgent(
    name="healthcare_agent_1",
    model_client=model_client,
    system_message="""
Role:
AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.

Goal:
AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.

Background:
You are a AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement..
""",
)


financial_agent_1 = AssistantAgent(
    name="financial_agent_1",
    model_client=model_client,
    system_message="""
Role:
Insight analyst exploring innovations in finance, wealth tech, and regulatory tech

Goal:
Insight analyst exploring innovations in finance, wealth tech, and regulatory tech

Background:
You are a Insight analyst exploring innovations in finance, wealth tech, and regulatory tech.
""",
)



