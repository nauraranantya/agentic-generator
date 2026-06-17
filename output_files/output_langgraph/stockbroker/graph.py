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

LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")


# ===========================================================
# Tool Stubs
# ===========================================================

@tool
def tool_stock_price(query: str) -> str:
    """A tool to get the stock price of a company. Invoked with argument { ticker: string }. When called, the agent fetches one-day and thirty-day price collections from https://api.financialdatasets.ai/prices with specified query parameters (interval, interval_multiplier, start_date, end_date, limit). The thirty-day retrieval may follow next_page_url to aggregate pages."""
    # TODO: implement tool_stock_price
    return f"Stub result from 'tool_stock_price' for query: {query}"

@tool
def tool_portfolio(query: str) -> str:
    """A tool to get the user's portfolio details. Only called when the user explicitly requests portfolio details. Invoked with argument { get_portfolio: true }."""
    # TODO: implement tool_portfolio
    return f"Stub result from 'tool_portfolio' for query: {query}"

@tool
def tool_buy_stock(query: str) -> str:
    """A tool to buy a stock. Invoked with arguments { ticker: string, quantity: number }. When called, the agent requests a price snapshot from https://api.financialdatasets.ai/prices/snapshot and includes the snapshot and quantity in the UI output."""
    # TODO: implement tool_buy_stock
    return f"Stub result from 'tool_buy_stock' for query: {query}"

tools_list = [tool_stock_price, tool_portfolio, tool_buy_stock]


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

def stockbroker_01_node(state: AgentState) -> dict:
    """stockbroker — invokes tools as needed and returns a response."""
    sys_msg = SystemMessage(content="""System-level instruction provided to the LLM on each invocation. Used with the conversation messages array state.messages.""")
    messages = [sys_msg] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


# ===========================================================
# Graph
# ===========================================================

workflow = StateGraph(AgentState)
workflow.add_node("agent", stockbroker_01_node)
workflow.add_node("tools", ToolNode(tools_list))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile()
