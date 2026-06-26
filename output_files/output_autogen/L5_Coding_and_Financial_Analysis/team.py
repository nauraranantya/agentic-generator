"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - Lesson 5: Coding and Financial Analysis Goal: 
Objectives:
  - Produce stock gain YTD plot objective: 
Resources:
  - ytd_stock_gains.png: PNG image file saved by the code executor containing the YTD stock gain plot for NVDA and TLSA. Filename specified in prompt.
  - chat_result (chat session artifact): Result of initiating chat: chat_result = code_executor_agent.initiate_chat(code_writer_agent, message=message). Represents the chat session/response resource created by the notebook run (content not captured here).
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


def local_cmd_executor_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    LocalCommandLineCodeExecutor

    Description:
    Local command-line code executor used to run code with timeout and working directory.
    """
    return (
        "Tool 'local_cmd_executor_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


local_cmd_executor_tool = FunctionTool(
    local_cmd_executor_tool_impl,
    description="Local command-line code executor used to run code with timeout and working directory."
)


# ==================================================
# Agents
# ==================================================


code_executor_agent = AssistantAgent(
    name="code_executor_agent",
    model_client=model_client,
    system_message="""
Role:
conversable code executor

Goal:
conversable code executor

Background:
You are a conversable code executor.
""",
)


code_writer_agent = AssistantAgent(
    name="code_writer_agent",
    model_client=model_client,
    system_message="""
Role:
assistant code writer

Goal:
assistant code writer

Background:
The source obtains code_writer_agent.system_message and prints it; exact content is not available in the provided artifact.
""",
)



team = RoundRobinGroupChat(
    participants=[
        code_executor_agent,
        code_writer_agent,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """

Task:
Today is {today}. Create a plot showing stock gain YTD for NVDA and TLSA. Make sure the code is in markdown code block and save the figure to a file ytd_stock_gains.png.

Expected Output:
A markdown code block containing runnable code and a saved image file ytd_stock_gains.png

"""