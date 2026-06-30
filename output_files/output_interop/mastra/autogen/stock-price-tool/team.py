
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


def stock_prices_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    GetStockPricestockPrices

    Description:
    Fetches the last day's closing stock price for a given symbol. Source tool implementation uses an HTTP fetch to https://mastra-stock-data.vercel.app/api/stock-data?symbol={symbol} and returns { symbol, currentPrice } with currentPrice mapped from data.prices['4. close'].
    """
    return (
        "Tool 'stock_prices_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


stock_prices_tool = FunctionTool(
    stock_prices_tool_impl,
    description="""Fetches the last day's closing stock price for a given symbol. Source tool implementation uses an HTTP fetch to https://mastra-stock-data.vercel.app/api/stock-data?symbol={symbol} and returns { symbol, currentPrice } with currentPrice mapped from data.prices['4. close']."""
)


# ==================================================
# Agents
# ==================================================


stock_agent = AssistantAgent(
    name="stock_agent",
    model_client=model_client,
    system_message="""
Role:
price_provider

Goal:
price_provider

Background:
Agent-level instruction used as the LLM system prompt / persona.
""",
)



