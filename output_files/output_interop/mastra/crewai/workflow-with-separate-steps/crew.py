"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Capabilities:
  - execute workflow step: Capability to execute a step function, enforce input/output schema constraints, access prior step results (getStepResult), and produce the specified resources.
Resources:
  - workflow inputData (example): 
  - doubledValue: 
  - isOriginalOdd: 
  - incrementedValue: 
  - tripledValue: 
  - isEven: 
  - example-run-1: 
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: mastra_tool — unknown tool class "MastraRuntimeTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("MastraRuntimeTool")
def mastra_tool(*args, **kwargs) -> str:
    """Represents the Mastra runtime that executes workflow steps, performs validation of input/output sche"""
    return "mastra_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_step_one(self) -> Task:
        return Task(
            config=self.tasks_config['task_step_one'],
        )

    @task
    def task_step_two(self) -> Task:
        return Task(
            config=self.tasks_config['task_step_two'],
            context=[self.task_step_one()],
        )

    @task
    def task_step_three(self) -> Task:
        return Task(
            config=self.tasks_config['task_step_three'],
            context=[self.task_step_two()],
        )

    @task
    def task_step_four(self) -> Task:
        return Task(
            config=self.tasks_config['task_step_four'],
            context=[self.task_step_three()],
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
