"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Primary goal: Identify birds and contextual metadata: 
Objectives:
  - Acquire representative image for inspection: 
  - Identify bird presence/species and summarize location: 
Environments:
  - Web runtime environment (Next.js / browser + server (application) environment; uses Unsplash API via server-side call and LLM via configured model.): 
Capabilities:
  - detect bird: Determine whether an image contains a bird (boolean).
  - identify species (scientific name): Identify the bird species, ideally returning scientific name as a string.
  - summarize location: Summarize the location of the photographed scene in one or two simple sentences.
  - fetch random image: Capability to query Unsplash and return a representative image resource.
Resources:
  - Example Unsplash image instance (sample resource produced by fetch task): An image resource object with the fields used by the system: 
  alt_description: string,
  urls: { regular: string, raw: string },
  user: { first_name: string, links: { html: string } }.
  (This instance models the schema and an example image result; real images are produced at runtime.)
  - Example bird metadata instance (example resource produced by analyze task): Structured metadata returned by analysis:
  { "bird": boolean, "species": string, "location": string }.
  Example semantics: bird=true, species='Corvus corax' (scientific name), location='a coastal cliff near (region/city)'. The exact scientific name and summary are derived by the agent from the image.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: get_random_image_tool — unknown tool class "GetarandomimagefromUnsplashtool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("GetarandomimagefromUnsplashtool")
def get_random_image_tool(*args, **kwargs) -> str:
    """Tool that queries Unsplash and returns a single image object selected from search results. Implement"""
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
            tools=[get_random_image_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def fetch_random_image_task(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_random_image_task'],
        )

    @task
    def analyze_image_and_produce_bird_metadata(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_image_and_produce_bird_metadata'],
            agent=self.bird_checker(),
            context=[self.fetch_random_image_task()],
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
