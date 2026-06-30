"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - Get stock information and perform trades: Goal: Provide stock price information to the user, show portfolio details on request, and facilitate buy orders when requested by user.
Environments:
  - Trading Environment (virtual): Operational environment context for the Stockbroker agent (uses external financial datasets API).
Capabilities:
  - Get stock prices: Capability to query historical and recent market prices for a given ticker.
  - Get portfolio: Capability to retrieve the user's portfolio details.
  - Buy stock: Capability to initiate a purchase action for a given stock and quantity.
Resources:
  - FINANCIAL_DATASETS_API_KEY (env var): Environment variable required by the agent to access the financial datasets API (FINANCIAL_DATASETS_API_KEY).
  - LLM message: The assistant message returned by the LLM invocation. May include content, and tool_calls array with each tool call having an id, name, and args object. This resource is pushed to the UI along with UI items representing tool outputs.
  - UI items: A list of UI items produced by the agent to present results (e.g., chart for prices, portfolio view, buy confirmation). Modeled here as a resource produced by the CallToolsTask.
  - oneDayPrices: Array of Price entries for a single day. Retrieved from https://api.financialdatasets.ai/prices with interval=minute and interval_multiplier=5, start_date=end_date=today, limit=5000.
  - thirtyDayPrices: Array of Price entries covering up to 30 days. Retrieved from https://api.financialdatasets.ai/prices with interval=minute and interval_multiplier=30; may require pagination following next_page_url to collect additional pages.
  - snapshot: Snapshot object returned by https://api.financialdatasets.ai/prices/snapshot for a requested ticker. Used by the buy-stock UI item to present price at purchase time.
  - portfolio UI: UI representation of the user's portfolio produced when the portfolio tool is invoked.
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
# Environment Configuration
# ==================================================
# Environment: Trading Environment (virtual)
# Operational environment context for the Stockbroker agent (uses external financial datasets API).

# ==================================================
# Generated Tool Stubs
# ==================================================


def tool_stock_price_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    stockprice

    Description:
    A tool to get the stock price of a company. Invoked with argument { ticker: string }. When called, the agent fetches one-day and thirty-day price collections from https://api.financialdatasets.ai/prices with specified query parameters (interval, interval_multiplier, start_date, end_date, limit). The thirty-day retrieval may follow next_page_url to aggregate pages.
    """
    return (
        "Tool 'tool_stock_price' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_stock_price = FunctionTool(
    tool_stock_price_impl,
    description="""A tool to get the stock price of a company. Invoked with argument { ticker: string }. When called, the agent fetches one-day and thirty-day price collections from https://api.financialdatasets.ai/prices with specified query parameters (interval, interval_multiplier, start_date, end_date, limit). The thirty-day retrieval may follow next_page_url to aggregate pages."""
)


def tool_portfolio_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    portfolio

    Description:
    A tool to get the user's portfolio details. Only called when the user explicitly requests portfolio details. Invoked with argument { get_portfolio: true }.
    """
    return (
        "Tool 'tool_portfolio' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_portfolio = FunctionTool(
    tool_portfolio_impl,
    description="""A tool to get the user's portfolio details. Only called when the user explicitly requests portfolio details. Invoked with argument { get_portfolio: true }."""
)


def tool_buy_stock_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    buystock

    Description:
    A tool to buy a stock. Invoked with arguments { ticker: string, quantity: number }. When called, the agent requests a price snapshot from https://api.financialdatasets.ai/prices/snapshot and includes the snapshot and quantity in the UI output.
    """
    return (
        "Tool 'tool_buy_stock' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_buy_stock = FunctionTool(
    tool_buy_stock_impl,
    description="""A tool to buy a stock. Invoked with arguments { ticker: string, quantity: number }. When called, the agent requests a price snapshot from https://api.financialdatasets.ai/prices/snapshot and includes the snapshot and quantity in the UI output."""
)


# ==================================================
# Agents
# ==================================================


stockbroker_01 = AssistantAgent(
    name="stockbroker_01",
    model_client=model_client,
    system_message="""
Role:
stockbroker

Goal:
Goal: Provide stock price information to the user, show portfolio details on request, and facilitate buy orders when requested by user.

Background:
System-level instruction provided to the LLM on each invocation. Used with the conversation messages array state.messages.
""",
)



