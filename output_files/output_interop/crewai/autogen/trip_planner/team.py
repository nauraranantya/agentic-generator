"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - : Select the best city based on weather patterns, seasonal events, and travel costs
  - : Provide in-depth local guide content, hidden gems, and practical tips.
  - : Create a 7-day travel itinerary with detailed daily plans, budgets, packing suggestions, and logistics.
Capabilities:
  - : Analyze and compare cities by weather conditions, events, and travel costs; deliver a detailed city selection report.
  - : Collect and synthesize local cultural, tourism and attraction information into a comprehensive guide.
  - : Generate optimized daily travel itineraries with logistics, budget calculations, and packing recommendations.
  - : Search the internet for relevant results and return structured snippets with title, link, and snippet text.
  - : Scrape raw HTML of a website, partition and summarize content with an internal summarization agent; returns concise summaries for each chunk.
  - : Perform safe arithmetic evaluation of mathematical expressions (supports + - * / % ** and parentheses). Returns numeric result or error message.
Resources:
  - : Used by SearchTools.search_internet to obtain organic search results.
  - : Used by BrowserTools.scrape_and_summarize_website to fetch HTML content.
  - : API key used by the language model client OpenAI (langchain_openai.OpenAI).
  - : The final produced travel plan (7-day itinerary), including hotels, restaurants, per-day schedule, weather forecast, packing suggestions, and budget breakdown.
  - : Comprehensive city guide including hidden gems, cultural hotspots and practical tips.
  - : Detailed report on chosen city including flight costs, weather forecast, and attractions.
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


def search_tools_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    search_tools

    Description:
    Toolset providing search_internet(query) which posts to Serper API and returns top organic results. Top results are returned in a formatted text with Title/Link/Snippet.
    """
    return (
        "Tool 'search_tools' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_tools = FunctionTool(
    search_tools_impl,
    description="""Toolset providing search_internet(query) which posts to Serper API and returns top organic results. Top results are returned in a formatted text with Title/Link/Snippet."""
)


def browser_tools_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    browser_tools

    Description:
    Scrape website content using Browserless content API; partitions HTML and produces chunk summaries by running an internal summarization agent.
    """
    return (
        "Tool 'browser_tools' "
        "is a generated stub and "
        "has not been implemented yet."
    )


browser_tools = FunctionTool(
    browser_tools_impl,
    description="""Scrape website content using Browserless content API; partitions HTML and produces chunk summaries by running an internal summarization agent."""
)


def calculator_tools_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    calculator_tools

    Description:
    Make a calculation(operation) evaluates basic arithmetic expressions safely using AST validation and a whitelist of allowed tokens.
    """
    return (
        "Tool 'calculator_tools' "
        "is a generated stub and "
        "has not been implemented yet."
    )


calculator_tools = FunctionTool(
    calculator_tools_impl,
    description="""Make a calculation(operation) evaluates basic arithmetic expressions safely using AST validation and a whitelist of allowed tokens."""
)


# ==================================================
# Agents
# ==================================================


city_selection_agent = AssistantAgent(
    name="city_selection_agent",
    model_client=model_client,
    system_message="""
Role:
City Selection Expert

Goal:
Select the best city based on weather patterns, seasonal events, and travel costs

Background:
Role: City Selection Expert; purpose: select the best city based on weather, season, and prices.
""",
)


local_expert_agent = AssistantAgent(
    name="local_expert_agent",
    model_client=model_client,
    system_message="""
Role:
Local Expert at this city

Goal:
Provide in-depth local guide content, hidden gems, and practical tips.

Background:
Role: Local Expert; purpose: compile an in-depth city guide with hidden gems and local insights.
""",
)


travel_concierge_agent = AssistantAgent(
    name="travel_concierge_agent",
    model_client=model_client,
    system_message="""
Role:
Amazing Travel Concierge

Goal:
Create a 7-day travel itinerary with detailed daily plans, budgets, packing suggestions, and logistics.

Background:
Role: Travel Concierge; purpose: produce a full 7-day itinerary, budget breakdown and packing suggestions.
""",
)



