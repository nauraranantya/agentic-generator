"""
Auto-generated CrewAI Crew: MastraDeploymentBirdChecker

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Identify birds and species from images: Primary goal: determine whether images contain birds, identify species when present, and summarize the location.
Objectives:
  - Accuracy evaluation objective: Objective to measure whether the agent identifies birds and species correctly (used by evaluation).
Environments:
  - Web UI Environment (nextjs + browser UI (visualization of images, interactive tags)): Operational environment of the Bird Checker (user selects tags in UI which trigger image retrieval and agent analysis).
Capabilities:
  - analyze image (detect bird, species, location): Capability assigned to birdAgent: view image, determine if a bird is present, return species scientific name and a short human-readable location summary.
  - fetch random image from Unsplash: Tool capability: call Unsplash search API for a random image matching provided query and return a selected image object.
Resources:
  - Unsplash API (external resource): External API used by GetRandomImageTool: https://api.unsplash.com/search/photos
  - Image resource (unsplash result): A resource that represents an image object returned by Unsplash. Contains URLs and photographer attribution in the runtime system; structurally represented here as a generic resource.
  - BirdResponse (structured agent output): Structured output format expected from the agent: { bird: boolean, species: string, location: string }.
  - IMAGES.isBird image (sample): Sample image expected to be a bird (IMAGES.isBird in src/lib/evals/data.ts).
  - IMAGES.notBird image (sample): Sample image expected to NOT be a bird (IMAGES.notBird in src/lib/evals/data.ts).
  - Evaluation results (bird detection): Contains scoring results for the evaluation (containsScorer: checks bird boolean and that species string contains expected scientific name). Represented as a resource literal in the system.
  - tag:wildlife: Tag option presented in UI: 'wildlife'.
  - tag:feathers: Tag option presented in UI: 'feathers'.
  - tag:flying: Tag option presented in UI: 'flying'.
  - tag:birds: Tag option presented in UI: 'birds'.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: get_random_image_tool — unknown tool class "Getarandomimagefromunsplash"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("Getarandomimagefromunsplash")
def get_random_image_tool(*args, **kwargs) -> str:
    """Gets a random image from Unsplash based on the selected option (query enum). Declared as a tool in s"""
    return "get_random_image_tool result"




@CrewBase
class MastraDeploymentBirdChecker:
    """MastraDeploymentBirdChecker crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def bird_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['bird_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def get_random_image_task(self) -> Task:
        return Task(
            config=self.tasks_config['get_random_image_task'],
        )

    @task
    def analyze_image_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_image_task'],
            agent=self.bird_agent(),
            context=[self.get_random_image_task()],
        )

    @task
    def bird_detection_evaluation_is_a_bird(self) -> Task:
        return Task(
            config=self.tasks_config['bird_detection_evaluation_is_a_bird'],
            agent=self.bird_agent(),
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the MastraDeploymentBirdChecker"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
