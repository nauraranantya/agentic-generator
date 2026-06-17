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
def tool_plan(query: str) -> str:
    """Represents the logical tool 'plan' that is invoked by the planner node to expose executed/rejected/remaining plan lists as tool_call args."""
    # TODO: implement tool_plan
    return f"Stub result from 'tool_plan' for query: {query}"

@tool
def tool_update_file(query: str) -> str:
    """A tool"""
    # TODO: implement tool_update_file
    return f"Stub result from 'tool_update_file' for query: {query}"

tools_list = [tool_plan, tool_update_file]


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

def open_code_agent_001_node(state: AgentState) -> dict:
    """planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts) — invokes tools as needed and returns a response."""
    sys_msg = SystemMessage(content="""You are a planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts).""")
    messages = [sys_msg] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


# ===========================================================
# Graph
# ===========================================================

workflow = StateGraph(AgentState)
workflow.add_node("agent", open_code_agent_001_node)
workflow.add_node("tools", ToolNode(tools_list))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile()
