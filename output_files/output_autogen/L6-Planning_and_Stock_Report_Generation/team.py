"""
Auto-generated AutoGen Team: MyCrew
Goals:
  - : 
Objectives:
  - : 
Human Agents:
  - admin ()
Resources:
  - : Historic prices and metadata for Nvidia (NVDA) covering the past month. Intended to be retrieved via Python code. Source and retrieval instructions preserved in CodeArtifact description.
  - : Artifact produced by Engineer: Python scripts to retrieve NVDA historic prices, compute monthly performance metrics, and produce serialized outputs (csv, json, plots). Implementation details intentionally captured as a high-level description (no SDK-specific code insertion in ontology).
  - : Results produced by Executor after running CodeArtifact: computed performance metrics, figures, and any data files used by Writer to compose the blog.
  - : Draft blog post in markdown format produced by Writer based on execution results. Contains title, textual analysis of stock performance, and optionally code-derived figures. Writer instructed to use pseudo ```md``` code block for content.
  - : Blog draft refined by Writer after Admin (user_proxy) provides comments. Final deliverable of workflow.
"""

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.agents import UserProxyAgent

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import (

    MaxMessageTermination

)

from autogen_core.tools import FunctionTool

from autogen_ext.models.openai import (
    OpenAIChatCompletionClient
)

model_client = OpenAIChatCompletionClient(
    model="gpt-4-turbo"
)


# ==================================================
# Generated Tool Stubs
# ==================================================


def coding_environment_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    codingenvironmenttool

    Description:
    Conceptual tool representing the environment used by Executor to run code. Config captured as key/value on Config individual.
    """
    return (
        "Tool 'coding_environment_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


coding_environment_tool = FunctionTool(
    coding_environment_tool_impl,
    description="Conceptual tool representing the environment used by Executor to run code. Config captured as key/value on Config individual."
)


# ==================================================
# Agents
# ==================================================


planner_agent = AssistantAgent(
    name="planner_agent",
    model_client=model_client,
    system_message="""
Role:
Planner

Goal:
Planner

Background:
Planner. Given a task, determine what information is needed to complete the task. After each step is done by others, check the progress and instruct the remaining steps
""",
)


engineer_agent = AssistantAgent(
    name="engineer_agent",
    model_client=model_client,
    system_message="""
Role:
Engineer

Goal:
Engineer

Background:
Engineer: writes code per planner's plan
""",
)


executor_agent = AssistantAgent(
    name="executor_agent",
    model_client=model_client,
    system_message="""
Role:
Executor

Goal:
Executor

Background:
Executor: execute code and return execution results (no human input).
""",
)


writer_agent = AssistantAgent(
    name="writer_agent",
    model_client=model_client,
    system_message="""
Role:
Writer

Goal:
Writer

Background:
Writer: write blogs based on the code execution results and take feedback from the admin to refine the blog.
""",
    tools=[
        coding_environment_tool,
    ],
)


# ==================================================
# Human Agents (UserProxy)
# ==================================================

admin = UserProxyAgent(
    name="admin",
    description="",
)

team = RoundRobinGroupChat(
    participants=[
        planner_agent,
        engineer_agent,
        executor_agent,
        writer_agent,
        admin,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """

Task:
Top-level task given by Admin that initiates the workflow. Text preserved in MainTaskPrompt.

Expected Output:
Completed: main_task


Task:
Planner determines which information (stock prices, date range, sources, computation methods) is needed and specifies steps for retrieving it using Python code.

Expected Output:
Completed: plan_information_task


Task:
Engineer implements Python code to retrieve stock data, compute required metrics, and produce artifacts for the writer. Code artifact contains instructions like 'retrieve historic prices, compute performance over last month, format data for report'.

Expected Output:
Completed: write_code_task


Task:
Executor runs the code produced by the Engineer in a specified working directory and returns execution outputs (e.g., numerical results, csv, figures). Execution config preserved on ExecutorConfig_Execution.

Expected Output:
Completed: execute_code_task


Task:
Writer composes the blog post using execution results; writes in markdown format with relevant titles and places content inside a pseudo ```md``` code block. The writer should accept feedback from Admin and refine the blog.

Expected Output:
Completed: write_report_task


Task:
Admin (user_proxy) reviews the blog draft and provides feedback; the Writer will refine the blog accordingly. Modeled as a Task performed by a HumanAgent.

Expected Output:
Completed: admin_feedback_task

"""