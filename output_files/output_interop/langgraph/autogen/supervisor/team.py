"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - Provide assistance to user: 
Objectives:
  - Handle user query: 
  - Route selection: 
Capabilities:
  - fetch ticker price: Fetch the price of a stock ticker.
  - trade ticker: Purchase or sell a ticker (trade operation).
  - get portfolio: Retrieve the user's portfolio.
  - suggest restaurants: Suggest restaurants for a given location.
  - suggest accommodations: Suggest places to stay for a trip.
  - write React TODO app: Generate a React TODO application when requested.
  - order pizza: Order a pizza on behalf of the user.
  - write document: Produce a text document for the user.
  - route selection: Analyze conversation and select appropriate tool route.
  - general assistant: Generic assistant capabilities to answer queries, summarize tool results, and follow up.
Resources:
  - Router tool call result: Result of router tool indicating chosen route, e.g., { 'route': 'stockbroker' }.
  - Stockbroker result: Resource representing the output(s) of stockbroker tasks such as price data, trade confirmations, or portfolio summaries.
  - TripPlanner result: Trip planning suggestions (restaurants, accommodations, itinerary).
  - OpenCode result: Generated code artifact: a React TODO app (source files, instructions).
  - OrderPizza result: Confirmation and details of pizza order (order receipt, status).
  - GeneralInput response: Text response from the general assistant (answers, summaries, follow-ups).
  - WriterAgent document: Text document created by writerAgent (full content of the requested document).
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


def tool_stockbroker_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    stockbroker

    Description:
    Can fetch the price of a ticker, purchase/sell a ticker, or get the user's portfolio.
    """
    return (
        "Tool 'tool_stockbroker' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_stockbroker = FunctionTool(
    tool_stockbroker_impl,
    description="""Can fetch the price of a ticker, purchase/sell a ticker, or get the user's portfolio."""
)


def tool_trip_planner_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tripPlanner

    Description:
    Helps the user plan their trip. It can suggest restaurants and places to stay in any given location.
    """
    return (
        "Tool 'tool_trip_planner' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_trip_planner = FunctionTool(
    tool_trip_planner_impl,
    description="""Helps the user plan their trip. It can suggest restaurants and places to stay in any given location."""
)


def tool_open_code_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    openCode

    Description:
    Can write a React TODO app for the user. Only call this tool if the user requests a TODO app.
    """
    return (
        "Tool 'tool_open_code' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_open_code = FunctionTool(
    tool_open_code_impl,
    description="""Can write a React TODO app for the user. Only call this tool if the user requests a TODO app."""
)


def tool_order_pizza_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    orderPizza

    Description:
    Can order a pizza for the user.
    """
    return (
        "Tool 'tool_order_pizza' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_order_pizza = FunctionTool(
    tool_order_pizza_impl,
    description="""Can order a pizza for the user."""
)


def tool_writer_agent_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    writerAgent

    Description:
    Can write a text document for the user. Only call this tool if they request a text document.
    """
    return (
        "Tool 'tool_writer_agent' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_writer_agent = FunctionTool(
    tool_writer_agent_impl,
    description="""Can write a text document for the user. Only call this tool if they request a text document."""
)


def tool_router_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    router

    Description:
    A tool used by the router node to select which tool should handle the user's query (routes: stockbroker, tripPlanner, openCode, orderPizza, generalInput, writerAgent).
    """
    return (
        "Tool 'tool_router' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_router = FunctionTool(
    tool_router_impl,
    description="""A tool used by the router node to select which tool should handle the user's query (routes: stockbroker, tripPlanner, openCode, orderPizza, generalInput, writerAgent)."""
)


def tool_general_input_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    generalInput

    Description:
    Tool/node that responds to general user inputs and summarizes or follows up on tool results.
    """
    return (
        "Tool 'tool_general_input' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_general_input = FunctionTool(
    tool_general_input_impl,
    description="""Tool/node that responds to general user inputs and summarizes or follows up on tool results."""
)


# ==================================================
# Agents
# ==================================================


generative_ui_supervisor = AssistantAgent(
    name="generative_ui_supervisor",
    model_client=model_client,
    system_message="""
Role:
supervisor

Goal:
supervisor

Background:
You are a supervisor.
""",
)



