"""
Auto-generated CrewAI Crew: MastraApplicationSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Human Agents:
  - developer_fajar_ekaputra ()
  - developer_kabul_kurniawan ()
Capabilities:
  - get weather capability: Capability to obtain current weather information for a given location (geocoding + weather API calls, returns normalized weather fields).
Resources:
  - city: Trigger input parameter: the city string provided to the workflow (e.g., 'Seattle').
  - weather-forecast: Array of daily forecast objects with the following structure:
[
  {
    date: string,
    maxTemp: number,
    minTemp: number,
    precipitationChance: number,
    condition: string,
    location: string
  },
  ...
]
This resource is the output of the fetch-weather task and the input to the plan-activities task.
  - activities-text: Textual output produced by the planning agent. Format: exact template as specified in planningAgent instructions (per-day headers, WEATHER SUMMARY, MORNING/AFTERNOON/INDOOR sections, SPECIAL CONSIDERATIONS). Typically a single concatenated string assembled from streamed LLM output.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: get_weather_tool — unknown tool class "getweather"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("getweather")
def get_weather_tool(*args, **kwargs) -> str:
    """Get current weather for a location. Tool accepts an input { location: string } and returns an object"""
    return "get_weather_tool result"




@CrewBase
class MastraApplicationSystem:
    """MastraApplicationSystem crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            tools=[get_weather_tool],
        )

    @agent
    def planning_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['planning_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def fetch_weather(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_weather'],
        )

    @task
    def plan_activities(self) -> Task:
        return Task(
            config=self.tasks_config['plan_activities'],
            agent=self.planning_agent(),
            context=[self.fetch_weather()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the MastraApplicationSystem"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
