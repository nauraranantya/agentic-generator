"""
Auto-generated CrewAI Crew: MastraSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Environments:
  -  (): 
Capabilities:
  - fetch cat fact: Capability of the tool: retrieve a cat fact string from a remote API.
  - double numeric value: 
  - increment numeric value by 1: 
  - square numeric value: 
  - square root numeric value: 
  - triple numeric value: 
  - log numeric value and return raw text: 
Resources:
  - Cat Fact Resource: 
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: cat_fact_tool — unknown tool class "catFactTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("catFactTool")
def cat_fact_tool(*args, **kwargs) -> str:
    """Description for cat_fact_tool"""
    return "cat_fact_tool result"




@CrewBase
class MastraSystem:
    """MastraSystem crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def cat_one(self) -> Agent:
        return Agent(
            config=self.agents_config['cat_one'],
            tools=[cat_fact_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def step_six_task(self) -> Task:
        return Task(
            config=self.tasks_config['step_six_task'],
        )

    @task
    def step_two_task(self) -> Task:
        return Task(
            config=self.tasks_config['step_two_task'],
        )

    @task
    def step_one_task(self) -> Task:
        return Task(
            config=self.tasks_config['step_one_task'],
        )

    @task
    def step_three_task(self) -> Task:
        return Task(
            config=self.tasks_config['step_three_task'],
        )

    @task
    def step_four_task(self) -> Task:
        return Task(
            config=self.tasks_config['step_four_task'],
        )

    @task
    def step_five_task(self) -> Task:
        return Task(
            config=self.tasks_config['step_five_task'],
        )

    @task
    def fetch_cat_fact_task(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_cat_fact_task'],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the MastraSystem"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
