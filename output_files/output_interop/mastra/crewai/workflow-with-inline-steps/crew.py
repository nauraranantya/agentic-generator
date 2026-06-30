"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Resources:
  - : Workflow trigger input resource: inputValue (number) provided when the workflow is triggered.
  - : Numeric output produced by stepOne: doubledValue = trigger.inputValue * 2 (number).
  - : Numeric output produced by stepTwo: incrementedValue = inputData.valueToIncrement + 1 (number).
  - : Prompt resource produced when stepThree suspends the workflow: message 'Do you accept?'. This is not a Prompt class instance because the code uses a suspend() runtime action; the text is preserved for reconstruction.
  - : Final message produced if resumeData.confirm === 'true': 'Thank you for accepting'.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: mastra_engine_tool — unknown tool class "mastraEngineTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("mastraEngineTool")
def mastra_engine_tool(*args, **kwargs) -> str:
    """Represents the Mastra runtime/engine that executes workflow steps and tasks (mapped to :Tool for lac"""
    return "mastra_engine_tool result"




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
