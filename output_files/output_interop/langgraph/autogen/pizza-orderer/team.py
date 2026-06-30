"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - Order Pizza Goal: Top-level intent: find a pizza shop and place a pizza order for a user.
Capabilities:
  - find_store: Capability to find a pizza shop given a location and optional company name.
  - place_order: Capability to place a pizza order given store contact and order details.
Resources:
  - User Location (input): User-provided location string (e.g., 'San Francisco' or 'New York'). Required input for the findStore task.
  - Pizza Company Name (optional input): Optional user-provided pizza company name (e.g., 'Dominos' or 'Papa John's').
  - Store Information (found store): Example produced content (from code's toolResponse): "I've found a pizza shop at 1119 19th St, San Francisco, CA 94107. The phone number for the shop is 415-555-1234.". Also includes link to the tool_call_id produced by the model call in runtime (tool_call_id captured in code), represented here as descriptive metadata.
  - Order Details (input for placing order): Structured fields expected from place_pizza_order output: address (address of store), phone_number (store phone), order (full pizza order for the user).
  - Order Confirmation (produced resource): Example produced content (from code's toolResponse): "Pizza order successfully placed.". In runtime the tool_call_id linking the confirmation to the model/tool invocation is present; represented in this resource description.
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


def tool_pizza_finder_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    PizzaFinderTool

    Description:
    Represents the external lookup mechanism that returns store contact information. In code this is emulated by constructing a ToolMessage with found shop details.
    """
    return (
        "Tool 'tool_pizza_finder' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_pizza_finder = FunctionTool(
    tool_pizza_finder_impl,
    description="""Represents the external lookup mechanism that returns store contact information. In code this is emulated by constructing a ToolMessage with found shop details."""
)


def tool_pizza_ordering_system_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    PizzaOrderingSystem

    Description:
    Represents the external ordering mechanism that places the pizza order and returns confirmation. In code this is emulated by constructing a ToolMessage 'Pizza order successfully placed.'.
    """
    return (
        "Tool 'tool_pizza_ordering_system' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_pizza_ordering_system = FunctionTool(
    tool_pizza_ordering_system_impl,
    description="""Represents the external ordering mechanism that places the pizza order and returns confirmation. In code this is emulated by constructing a ToolMessage 'Pizza order successfully placed.'."""
)


# ==================================================
# Agents
# ==================================================


pizza_orderer_v1 = AssistantAgent(
    name="pizza_orderer_v1",
    model_client=model_client,
    system_message="""
Role:
pizza-ordering-assistant

Goal:
Top-level intent: find a pizza shop and place a pizza order for a user.

Background:
General system role description used by both nodes as the system message.
""",
)



