"""
Auto-generated CrewAI Crew: MastraSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Capabilities:
  - Fetch current weather capability: Fetches geocoding for a city and retrieves current weather fields. Input: { location: string }. Output: { temperature, feelsLike, humidity, windSpeed, windGust, conditions, location }.
Resources:
  - forecast array: Forecast array produced by fetch-weather:
Array of objects with schema:
[{ date: string, maxTemp: number, minTemp: number, precipitationChance: number, condition: string, location: string }]
  - open-meteo geocoding API: Used to convert city names to lat/lon.
  - open-meteo forecast API: Used to fetch daily or hourly forecast values.
  - current weather (tool output): Object returned by the weather tool with current weather metrics and location as a string.
  - agent input string: A string like: 'Forecast data: { ... }' that will be provided to the weatherReporterAgent.
  - activities text: Activities textual output produced by agent with a structured format per guidelines:
📅 [Day, Month Date, Year]
═══════════════════════════

🌡️ WEATHER SUMMARY
• Conditions: ...
• Temperature: ...
• Precipitation: ...

... (sections for MORNING ACTIVITIES, AFTERNOON ACTIVITIES, INDOOR ALTERNATIVES, SPECIAL CONSIDERATIONS)
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
    """Tool to get current weather for a location. Wraps geocoding and open-meteo APIs and returns a simpli"""
    return "weather_tool result"




@CrewBase
class MastraSystem:
    """MastraSystem crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            tools=[weather_tool],
        )

    @agent
    def weather_explainer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_explainer_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def fetch_weather_task(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_weather_task'],
        )

    @task
    def weather_tool_call_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_tool_call_task'],
        )

    @task
    def map_forecast_to_prompt_task(self) -> Task:
        return Task(
            config=self.tasks_config['map_forecast_to_prompt_task'],
            context=[self.weather_tool_call_task()],
        )

    @task
    def plan_activities(self) -> Task:
        return Task(
            config=self.tasks_config['plan_activities'],
            agent=self.weather_agent(),
            context=[self.fetch_weather_task(), self.map_forecast_to_prompt_task()],
        )

    @task
    def explain_weather_task(self) -> Task:
        return Task(
            config=self.tasks_config['explain_weather_task'],
            context=[self.map_forecast_to_prompt_task()],
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
