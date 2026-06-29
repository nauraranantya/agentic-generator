"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - : Define agent 1 goal here
  - : Define agent 2 goal here
Capabilities:
  - web search: Capability to run web searches and return search results.
Resources:
  - : Represents the output produced by task_1_name; used as input to task_2_name. Created by Task_1.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: duck_duck_go_tool — unknown tool class "DuckDuckGoTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("DuckDuckGoTool")
def duck_duck_go_tool(*args, **kwargs) -> str:
    """An instance of DuckDuckGoSearchRun created in main.py and intended for web search functionality. (No"""
    return "duck_duck_go_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def agent_1_name(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_1_name'],
            tools=[duck_duck_go_tool],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def agent_2_name(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_2_name'],
            tools=[duck_duck_go_tool],
            allow_delegation=True,
            verbose=True,
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_1(self) -> Task:
        return Task(
            config=self.tasks_config['task_1'],
            agent=self.agent_1_name(),
        )

    @task
    def task_2(self) -> Task:
        return Task(
            config=self.tasks_config['task_2'],
            agent=self.agent_2_name(),
            context=[self.task_1()],
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
