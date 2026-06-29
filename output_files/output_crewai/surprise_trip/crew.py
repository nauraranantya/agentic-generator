"""
Auto-generated CrewAI Crew: SurpriseTravelCrew

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Goal: personalized activity planner: Research and find cool things to do at the destination, including activities and events that match the traveler's interests and age group
  - Goal: restaurant scout: Find highly-rated restaurants and dining experiences at the destination, and recommend scenic locations and fun activities
  - Goal: itinerary compiler: Compile all researched information into a comprehensive day-by-day itinerary, ensuring the integration of flights and hotel information
Objectives:
  - : Produce a per-day list of recommended activities and events including details and suitability rationale.
  - : Produce recommended restaurants and scenic locations with ratings and descriptions for each relevant day.
  - : Produce a single integrated itinerary document that schedules flights, hotel, day plans, activities and restaurants.
Resources:
  - Itinerary_Instance: Pydantic output schema named Itinerary:
- name: string (funny name for itinerary)
- day_plans: List[DayPlan], each DayPlan:
    - date: string
    - activities: List[Activity], each Activity:
        - name: string
        - location: string
        - description: string
        - date: string
        - cousine: string
        - why_its_suitable: string
        - reviews: Optional[List[str]]
        - rating: Optional[float]
    - restaurants: List[str]
    - flight: Optional[str]
- hotel: string
This resource is the output_json schema referenced by itinerary_compilation_task.
  - ExampleRunInputs: Example runtime inputs used in main.run and train():
    {
      'origin': 'São Paulo, GRU',
      'destination': 'New York, JFK',
      'age': 31,
      'hotel_location': 'Brooklyn',
      'flight_information': 'GOL 1234, leaving at June 30th, 2024, 10:00',
      'trip_duration': '14 days'
    }
    This is a sample input bundle used for kickoff/train in the repository.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool

from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# ===========================================================
# Tool Instances
# ===========================================================
serper_dev_tool = SerperDevTool()
scrape_website_tool = ScrapeWebsiteTool()
# TODO: my_custom_tool — unknown tool class "MyCustomTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("MyCustomTool")
def my_custom_tool(*args, **kwargs) -> str:
    """Example custom tool present in source (tools/custom_tool.py). This example tool is included in the r"""
    return "my_custom_tool result"




@CrewBase
class SurpriseTravelCrew:
    """SurpriseTravelCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def personalized_activity_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['personalized_activity_planner'],
            tools=[serper_dev_tool, scrape_website_tool],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def restaurant_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['restaurant_scout'],
            tools=[serper_dev_tool, scrape_website_tool],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def itinerary_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_compiler'],
            tools=[serper_dev_tool],
            allow_delegation=False,
            verbose=True,
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def personalized_activity_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['personalized_activity_planning_task'],
            agent=self.personalized_activity_planner(),
        )

    @task
    def restaurant_scenic_location_scout_task(self) -> Task:
        return Task(
            config=self.tasks_config['restaurant_scenic_location_scout_task'],
            agent=self.restaurant_scout(),
        )

    @task
    def itinerary_compilation_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_compilation_task'],
            agent=self.itinerary_compiler(),
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the SurpriseTravelCrew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
