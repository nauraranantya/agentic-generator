"""
Auto-generated LangGraph App: MyCrew

Pattern : Tool-Calling (single agent with tools)
Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
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

LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o")


# ===========================================================
# Tool Stubs
# ===========================================================

@tool
def tool_extract(query: str) -> str:
    """Tool name: "extract"
Purpose: Extract TripDetails from conversation history. Bound to the agent's LLM.
Schema (Zod, represented informally):
{
  location: string (describe: The location to plan the trip for. Can be a city, state, or country.),
  startDate: string (optional, describe: The start date of the trip. YYYY-MM-DD),
  endDate: string (optional, describe: The end date of the trip. YYYY-MM-DD),
  numberOfGuests: number (describe: The number of guests. Defaults to 2 if unspecified.)
}
Behavior: the tool returns only fields specified by the user; do not make up values. If location is missing, a clarification message should be generated requesting the location."""
    # TODO: implement tool_extract
    return f"Stub result from 'tool_extract' for query: {query}"

@tool
def tool_classify(query: str) -> str:
    """Tool name: "classify"
Purpose: Classify whether trip details remain relevant to the user's most recent request.
Schema:
{
  isRelevant: boolean (describe: Whether the trip details are still relevant to the user's request.)
}
Notes: When invoked, tool_choice is set to "classify" in the implementation."""
    # TODO: implement tool_classify
    return f"Stub result from 'tool_classify' for query: {query}"

@tool
def tool_list_accommodations(query: str) -> str:
    """Tool name: "list-accommodations"
Purpose: A tool to list accommodations for the user. Implementation populates an accommodations list (id, name, price, rating, city, image) using a data generator.
Schema: {} (no input schema fields required in the implementation).
Produces: An accommodations list resource used to populate UI."""
    # TODO: implement tool_list_accommodations
    return f"Stub result from 'tool_list_accommodations' for query: {query}"

@tool
def tool_list_restaurants(query: str) -> str:
    """Tool name: "list-restaurants"
Purpose: A tool to list restaurants for the user. Implementation uses trip details to produce a restaurants list.
Schema: {}.
Produces: A restaurants list resource used to populate UI."""
    # TODO: implement tool_list_restaurants
    return f"Stub result from 'tool_list_restaurants' for query: {query}"

tools_list = [tool_extract, tool_classify, tool_list_accommodations, tool_list_restaurants]


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

def trip_planner_agent_node(state: AgentState) -> dict:
    """assistant / trip-planner — invokes tools as needed and returns a response."""
    sys_msg = SystemMessage(content="""You are a assistant / trip-planner.""")
    messages = [sys_msg] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


# ===========================================================
# Graph
# ===========================================================

workflow = StateGraph(AgentState)
workflow.add_node("agent", trip_planner_agent_node)
workflow.add_node("tools", ToolNode(tools_list))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile()
