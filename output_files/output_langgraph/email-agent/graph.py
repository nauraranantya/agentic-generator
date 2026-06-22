"""
Auto-generated LangGraph App: MyCrew

Pattern : Tool-Calling (single agent with tools)
Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Human Agents:
  - user_human ()
Capabilities:
  - Compose Email: Generate a draft email (subject, body, to) from conversation history.
  - Rewrite Email: Rewrite email content given user's response/instructions; should only change requested fields.
  - Send Email: Finalize and send the composed email (in this implementation it yields a confirmation message indicating successful send).
  - Handle Human Interrupt: Present the email to a human for review and accept/edit/ignore/response and handle the resulting input accordingly.
Resources:
  - Conversation History: Sequence of messages between user and agent used as input to generate the email. In implementation substituted into the prompt via {CONVERSATION}.
  - Draft Email: Structured email artifact with fields:
- subject: string
- body: string
- to: string

This is the primary data produced by the writing and rewriting tasks. The implementation expects these exact fields.
  - Sent Email Record: A record/artifact representing that the email was sent. In implementation returned as an AI message: 'Successfully sent email.' (represented as an artifact here).
  - Human Response (interrupt result): Represents the human-interaction result from the interrupt UI. Possible response types recorded in implementation: 'ignore', 'response', 'accept', or 'edit' (with args carrying edited email fields). This ontology stores allowed values in the interrupt config and records that user participated in interrupt interactions.
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
def write_email_tool(query: str) -> str:
    """Tool binding used by the LLM to produce structured email objects. Description: "Write an email based on the conversation history"."""
    # TODO: implement write_email_tool
    return f"Stub result from 'write_email_tool' for query: {query}"

tools_list = [write_email_tool]


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

def email_assistant_agent_node(state: AgentState) -> dict:
    """email_assistant — invokes tools as needed and returns a response."""
    sys_msg = SystemMessage(content="""You are a email_assistant.""")
    messages = [sys_msg] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


# ===========================================================
# Graph
# ===========================================================

workflow = StateGraph(AgentState)
workflow.add_node("agent", email_assistant_agent_node)
workflow.add_node("tools", ToolNode(tools_list))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile(
    interrupt_before=[""]
)
