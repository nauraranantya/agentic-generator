"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Capabilities:
  - : Ability to answer questions about cat species, their behavior, biology and taxonomy.
Resources:
  - : Output produced by the agent for the generateMostPopularSpecies task. Expected shape: { "species": string } (the source's Zod schema). Example: { "species": "Maine Coon" }
  - : Representation of the console runtime used as a resource during task execution.
  - : Output of logCatName task. Example: 'Hello Fluffy'. Output schema in source: z.object({ rawText: z.string() }).
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: console_tool — unknown tool class "consoleTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("consoleTool")
def console_tool(*args, **kwargs) -> str:
    """Represents the runtime logging facility used by the step (the source prints to console via console.l"""
    return "console_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def cat_one(self) -> Agent:
        return Agent(
            config=self.agents_config['cat_one'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_log_cat_name(self) -> Task:
        return Task(
            config=self.tasks_config['task_log_cat_name'],
        )

    @task
    def task_generate_most_popular_species(self) -> Task:
        return Task(
            config=self.tasks_config['task_generate_most_popular_species'],
            agent=self.cat_one(),
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
