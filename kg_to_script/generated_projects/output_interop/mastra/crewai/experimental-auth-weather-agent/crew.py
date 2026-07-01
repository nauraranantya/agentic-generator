"""
Auto-generated CrewAI Crew: Mastraserversystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Capabilities:
  - HTTP fetch: Capability to perform HTTP requests to external APIs (used by the weather tool).
  - Text generation (LLM, streaming): Capability to generate natural language text and stream responses from a language model.
  - Get weather data: Capability to retrieve, parse and normalize weather information for a given location.
Resources:
  - open-meteo geocoding API: Geocoding API used to resolve city name to latitude/longitude.
  - open-meteo weather API: Open-Meteo weather endpoint used to fetch current/forecast weather and hourly data.
  - weather forecast: Forecast object produced by fetch-weather step with structure:
{
  date: ISO string,
  maxTemp: number,
  minTemp: number,
  condition: string,
  precipitationChance: number,
  location: string
}
This resource is the normalized forecast that is passed to the activity planning step.
  - planned activities (text): A single string containing activity suggestions (may contain multiple day entries).
Format should follow the activity-planning system prompt (emoji and section headers) and includes: WEATHER SUMMARY, MORNING ACTIVITIES, AFTERNOON ACTIVITIES, INDOOR ALTERNATIVES, SPECIAL CONSIDERATIONS.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: weather_tool — unknown tool class "getweather"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("getweather")
def weather_tool(*args, **kwargs) -> str:
    """Get current weather for a location.  Behavior summary: - Input: { location: string } (city name) - E"""
    return "weather_tool result"




@CrewBase
class Mastraserversystem:
    """Mastraserversystem crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            tools=[weather_tool],
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
            agent=self.weather_agent(),
            context=[self.fetch_weather()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the Mastraserversystem"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
