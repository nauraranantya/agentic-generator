
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


def search_crypto_coins_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    Searchcryptocoinstool

    Description:
    Tool to search all available crypto coins by a keyword. Implements logic: fetch coin list from CoinGecko, try exact match by name (case-insensitive), if not found return first coin whose name contains the keyword.
    """
    return (
        "Tool 'search_crypto_coins_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_crypto_coins_tool = FunctionTool(
    search_crypto_coins_tool_impl,
    description="""Tool to search all available crypto coins by a keyword. Implements logic: fetch coin list from CoinGecko, try exact match by name (case-insensitive), if not found return first coin whose name contains the keyword."""
)


def get_crypto_price_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    Getcryptopricetool

    Description:
    Tool to get crypto price by coin id. Fetches market data for a given id from CoinGecko markets endpoint.
    """
    return (
        "Tool 'get_crypto_price_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


get_crypto_price_tool = FunctionTool(
    get_crypto_price_tool_impl,
    description="""Tool to get crypto price by coin id. Fetches market data for a given id from CoinGecko markets endpoint."""
)


def get_historical_crypto_prices_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    Gethistoricalcryptopricestool

    Description:
    Tool to retrieve historical price data for a coin. Returns an array of {timestamp,price}. Calls CoinGecko market_chart endpoint.
    """
    return (
        "Tool 'get_historical_crypto_prices_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


get_historical_crypto_prices_tool = FunctionTool(
    get_historical_crypto_prices_tool_impl,
    description="""Tool to retrieve historical price data for a coin. Returns an array of {timestamp,price}. Calls CoinGecko market_chart endpoint."""
)


# ==================================================
# Agents
# ==================================================


crypto_agent = AssistantAgent(
    name="crypto_agent",
    model_client=model_client,
    system_message="""
Role:
crypto-agent

Goal:
crypto-agent

Background:
You are a crypto-agent.
""",
)



