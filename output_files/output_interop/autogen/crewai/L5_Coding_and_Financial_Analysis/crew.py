"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Lesson 5: Coding and Financial Analysis Goal: 
Objectives:
  - Produce stock gain YTD plot objective: 
Resources:
  - ytd_stock_gains.png: PNG image file saved by the code executor containing the YTD stock gain plot for NVDA and TLSA. Filename specified in prompt.
  - chat_result (chat session artifact): Result of initiating chat: chat_result = code_executor_agent.initiate_chat(code_writer_agent, message=message). Represents the chat session/response resource created by the notebook run (content not captured here).
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: local_cmd_executor_tool — unknown tool class "LocalCommandLineCodeExecutor"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("LocalCommandLineCodeExecutor")
def local_cmd_executor_tool(*args, **kwargs) -> str:
    """Local command-line code executor used to run code with timeout and working directory."""
    return "local_cmd_executor_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def code_executor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['code_executor_agent'],
            tools=[local_cmd_executor_tool],
        )

    @agent
    def code_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['code_writer_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def stock_analysis_ytd_stock_gain_plot(self) -> Task:
        return Task(
            config=self.tasks_config['stock_analysis_ytd_stock_gain_plot'],
            agent=self.code_writer_agent(),
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the UnnamedProject"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
