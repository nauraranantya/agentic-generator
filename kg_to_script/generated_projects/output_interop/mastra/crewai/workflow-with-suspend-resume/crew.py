"""
Auto-generated CrewAI Crew: MastraSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Resources:
  - doubledValue (resource): {"name": "doubledValue", "type": "number", "exampleValue": 60}
  - incrementedValue (resource): {"name": "incrementedValue", "type": "number", "exampleOnResume": 66, "exampleWhenSuspended": 0}
  - tripledValue (resource): {"name": "tripledValue", "type": "number", "exampleValue": 198}
  - isEven (resource): {"name": "isEven", "type": "boolean", "exampleValue": true }
  - example run result (suspended): {
  "status": "suspended",
  "suspendedSteps": ["stepTwo"],
  "observedOutputs": {
    "doubledValue": 60,
    "incrementedValue": 0
  },
  "input": { "inputValue": 30 },
  "note": "During stepTwo execution resumeData.extraNumber is absent; the step called suspend({}) and returned incrementedValue:0 as transient output."
}
  - example run result (resumed / completed): {
  "status": "completed",
  "finalOutputs": {
    "doubledValue": 60,
    "incrementedValue": 66,
    "tripledValue": 198,
    "isEven": true
  },
  "resumeData": { "extraNumber": 5 },
  "note": "Resumed stepTwo with extraNumber 5, subsequent steps executed to completion."
}
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: mastra_runtime — unknown tool class "MastraRuntimecoreexecutor"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("MastraRuntimecoreexecutor")
def mastra_runtime(*args, **kwargs) -> str:
    """Logical runtime tool that executes workflow steps and coordinates suspend/resume behavior."""
    return "mastra_runtime result"

# TODO: libsql_store — unknown tool class "LibSQLStore"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("LibSQLStore")
def libsql_store(*args, **kwargs) -> str:
    """Storage plugin used by Mastra for workflow snapshots."""
    return "libsql_store result"




@CrewBase
class MastraSystem:
    """MastraSystem crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    # ── Tasks ───────────────────────────────────────────

    @task
    def invoke_nested_data_processing_workflow(self) -> Task:
        return Task(
            config=self.tasks_config['invoke_nested_data_processing_workflow'],
        )

    @task
    def step_one_task_double_input(self) -> Task:
        return Task(
            config=self.tasks_config['step_one_task_double_input'],
        )

    @task
    def resume_increment(self) -> Task:
        return Task(
            config=self.tasks_config['resume_increment'],
        )

    @task
    def step_three_task_triple_incremented_value(self) -> Task:
        return Task(
            config=self.tasks_config['step_three_task_triple_incremented_value'],
            context=[self.resume_increment()],
        )

    @task
    def step_four_task_is_even_check(self) -> Task:
        return Task(
            config=self.tasks_config['step_four_task_is_even_check'],
            context=[self.step_three_task_triple_incremented_value()],
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
