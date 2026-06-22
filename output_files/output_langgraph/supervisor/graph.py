"""
Auto-generated LangGraph App: MyCrew

Pattern : Tool-Calling (single agent with tools)
Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
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
def tool_stockbroker(query: str) -> str:
    """Can fetch the price of a ticker, purchase/sell a ticker, or get the user's portfolio."""
    # TODO: implement tool_stockbroker
    return f"Stub result from 'tool_stockbroker' for query: {query}"

@tool
def tool_trip_planner(query: str) -> str:
    """Helps the user plan their trip. It can suggest restaurants and places to stay in any given location."""
    # TODO: implement tool_trip_planner
    return f"Stub result from 'tool_trip_planner' for query: {query}"

@tool
def tool_open_code(query: str) -> str:
    """Can write a React TODO app for the user. Only call this tool if the user requests a TODO app."""
    # TODO: implement tool_open_code
    return f"Stub result from 'tool_open_code' for query: {query}"

@tool
def tool_order_pizza(query: str) -> str:
    """Can order a pizza for the user."""
    # TODO: implement tool_order_pizza
    return f"Stub result from 'tool_order_pizza' for query: {query}"

@tool
def tool_writer_agent(query: str) -> str:
    """Can write a text document for the user. Only call this tool if they request a text document."""
    # TODO: implement tool_writer_agent
    return f"Stub result from 'tool_writer_agent' for query: {query}"

@tool
def tool_router(query: str) -> str:
    """A tool used by the router node to select which tool should handle the user's query (routes: stockbroker, tripPlanner, openCode, orderPizza, generalInput, writerAgent)."""
    # TODO: implement tool_router
    return f"Stub result from 'tool_router' for query: {query}"

@tool
def tool_general_input(query: str) -> str:
    """Tool/node that responds to general user inputs and summarizes or follows up on tool results."""
    # TODO: implement tool_general_input
    return f"Stub result from 'tool_general_input' for query: {query}"

tools_list = [tool_stockbroker, tool_trip_planner, tool_open_code, tool_order_pizza, tool_writer_agent, tool_router, tool_general_input]


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

def generative_ui_supervisor_node(state: AgentState) -> dict:
    """supervisor — invokes tools as needed and returns a response."""
    sys_msg = SystemMessage(content="""You are a supervisor.""")
    messages = [sys_msg] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


# ===========================================================
# Graph
# ===========================================================

workflow = StateGraph(AgentState)
workflow.add_node("agent", generative_ui_supervisor_node)
workflow.add_node("tools", ToolNode(tools_list))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile()
