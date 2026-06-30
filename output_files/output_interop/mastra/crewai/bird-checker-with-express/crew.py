"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Resources:
  - : External API resource used by the get-random-image tool. Requires UNSPLASH_ACCESS_KEY environment variable (UNSPLASH_ACCESS_KEY).
  - : Runtime artifact produced by the image-fetch tool. Fields produced at runtime include:
- imageUrl: raw image URL (string)
- photographerName: first name of photographer (string)
- photographerProfile: link to photographer profile (string)
This instance represents the image resource passed between tasks.
  - : Metadata produced by the image analysis task. Schema (expected):
- bird: boolean
- species: string
- location: string
This reflects the structured output schema provided to the agent in the code (zod object with fields bird, species, location).
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: get_random_image_tool — unknown tool class "getRandomImageTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("getRandomImageTool")
def get_random_image_tool(*args, **kwargs) -> str:
    """Gets a random image from Unsplash based on selected query option. Random page selection and order_by"""
    return "get_random_image_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def bird_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['bird_checker'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_fetch_random_image(self) -> Task:
        return Task(
            config=self.tasks_config['task_fetch_random_image'],
        )

    @task
    def task_analyze_image(self) -> Task:
        return Task(
            config=self.tasks_config['task_analyze_image'],
            agent=self.bird_checker(),
            context=[self.task_fetch_random_image()],
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
