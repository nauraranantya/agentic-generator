"""
Auto-generated LangGraph App: MyCrew

Pattern : Linear (single agent, no tools)
Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
"""

import os
from typing import Annotated, TypedDict
from pathlib import Path
from dotenv import load_dotenv
import yaml

_HERE = Path(__file__).parent
load_dotenv(_HERE / ".env", override=True)

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")


# ===========================================================
# State
# ===========================================================

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


# ===========================================================
# LLM
# ===========================================================

llm = ChatOpenAI(model=LLM_MODEL)


# ===========================================================
# Agent Node
# ===========================================================

def chat_step_node(state: AgentState) -> dict:
    """conversational assistant — processes messages and returns a response."""
    sys_msg = SystemMessage(content="""This system role message is prepended to every model invocation in the chat node.""")
    messages = [sys_msg] + state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}


# ===========================================================
# Graph
# ===========================================================

workflow = StateGraph(AgentState)
workflow.add_node("chat_step", chat_step_node)

workflow.add_edge(START, "chat_step")
workflow.add_edge("chat_step", END)

app = workflow.compile()
