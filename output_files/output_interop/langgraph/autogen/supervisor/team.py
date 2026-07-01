
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
    tool_stockbroker

    Description:
    can fetch the price of a ticker, purchase/sell a ticker, or get the user's portfolio
    """
    return (
        "Tool 'tool_stockbroker' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_stockbroker = FunctionTool(
    tool_stockbroker_impl,
    description="""can fetch the price of a ticker, purchase/sell a ticker, or get the user's portfolio """
)


def tool_trip_planner_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_trip_planner

    Description:
    helps the user plan their trip; can suggest restaurants and places to stay in any given location.
    """
    return (
        "Tool 'tool_trip_planner' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_trip_planner = FunctionTool(
    tool_trip_planner_impl,
    description="""helps the user plan their trip; can suggest restaurants and places to stay in any given location. """
)


def tool_open_code_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_open_code

    Description:
    can write a React TODO app for the user. Only call this tool if they request a TODO app.
    """
    return (
        "Tool 'tool_open_code' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_open_code = FunctionTool(
    tool_open_code_impl,
    description="""can write a React TODO app for the user. Only call this tool if they request a TODO app. """
)


def tool_order_pizza_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_order_pizza

    Description:
    can order a pizza for the user
    """
    return (
        "Tool 'tool_order_pizza' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_order_pizza = FunctionTool(
    tool_order_pizza_impl,
    description="""can order a pizza for the user """
)


def tool_writer_agent_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_writer_agent

    Description:
    can write a text document for the user. Only call this tool if they request a text document.
    """
    return (
        "Tool 'tool_writer_agent' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_writer_agent = FunctionTool(
    tool_writer_agent_impl,
    description="""can write a text document for the user. Only call this tool if they request a text document. """
)


def tool_router_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_router

    Description:
    A tool to route the user's query to the appropriate tool. (Used as a tool schema bound to the routing model)
    """
    return (
        "Tool 'tool_router' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_router = FunctionTool(
    tool_router_impl,
    description="""A tool to route the user's query to the appropriate tool. (Used as a tool schema bound to the routing model) """
)


# ==================================================
# Agents
# ==================================================


supervisor = AssistantAgent(
    name="supervisor",
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


router = AssistantAgent(
    name="router",
    model_client=model_client,
    system_message="""
Role:
router

Goal:
router

Background:
You are a router.
""",
)


general_input = AssistantAgent(
    name="general_input",
    model_client=model_client,
    system_message="""
Role:
general_input_handler

Goal:
general_input_handler

Background:
You are a general_input_handler.
""",
)


stockbroker = AssistantAgent(
    name="stockbroker",
    model_client=model_client,
    system_message="""
Role:
stockbroker_tool_agent

Goal:
stockbroker_tool_agent

Background:
You are a stockbroker_tool_agent.
""",
)


trip_planner = AssistantAgent(
    name="trip_planner",
    model_client=model_client,
    system_message="""
Role:
trip_planner_tool_agent

Goal:
trip_planner_tool_agent

Background:
You are a trip_planner_tool_agent.
""",
)


open_code = AssistantAgent(
    name="open_code",
    model_client=model_client,
    system_message="""
Role:
open_code_tool_agent

Goal:
open_code_tool_agent

Background:
You are a open_code_tool_agent.
""",
)


order_pizza = AssistantAgent(
    name="order_pizza",
    model_client=model_client,
    system_message="""
Role:
order_pizza_tool_agent

Goal:
order_pizza_tool_agent

Background:
You are a order_pizza_tool_agent.
""",
)


writer_agent = AssistantAgent(
    name="writer_agent",
    model_client=model_client,
    system_message="""
Role:
writer_agent_tool

Goal:
writer_agent_tool

Background:
You are a writer_agent_tool.
""",
)



