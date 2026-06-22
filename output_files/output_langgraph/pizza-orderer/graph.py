"""
Auto-generated LangGraph App: MyCrew

Pattern : Tool-Calling (single agent with tools)
Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
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

import os
from typing import Annotated, TypedDict
from pathlib import Path
from dotenv import load_dotenv

_HERE = Path(__file__).parent
load_dotenv(_HERE / ".env", override=True)

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool

LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")


# ===========================================================
# Tool Stubs
# ===========================================================

@tool
def tool_pizza_finder(query: str) -> str:
    """Represents the external lookup mechanism that returns store contact information. In code this is emulated by constructing a ToolMessage with found shop details."""
    # TODO: implement tool_pizza_finder
    return f"Stub result from 'tool_pizza_finder' for query: {query}"

@tool
def tool_pizza_ordering_system(query: str) -> str:
    """Represents the external ordering mechanism that places the pizza order and returns confirmation. In code this is emulated by constructing a ToolMessage 'Pizza order successfully placed.'."""
    # TODO: implement tool_pizza_ordering_system
    return f"Stub result from 'tool_pizza_ordering_system' for query: {query}"

tools_list = [tool_pizza_finder, tool_pizza_ordering_system]


# ===========================================================
# State
# ===========================================================

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


# ===========================================================
# LLM
# ===========================================================

llm = ChatOpenAI(model=LLM_MODEL)
llm_with_tools = llm.bind_tools(tools_list)


# ===========================================================
# Agent Node
# ===========================================================

def pizza_orderer_v1_node(state: AgentState) -> dict:
    """pizza-ordering-assistant — invokes tools as needed and returns a response."""
    sys_msg = SystemMessage(content="""General system role description used by both nodes as the system message.""")
    messages = [sys_msg] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


# ===========================================================
# Graph
# ===========================================================

workflow = StateGraph(AgentState)
workflow.add_node("agent", pizza_orderer_v1_node)
workflow.add_node("tools", ToolNode(tools_list))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile()
