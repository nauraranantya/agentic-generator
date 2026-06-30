"""
Auto-generated CrewAI Crew: TravelAISystemMastraexampleapp

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Plan Trip: 
  - Format Output: 
Objectives:
  - Assemble trip components: 
Capabilities:
  - Find Flights: Capability to search and select flight options.
  - Find Hotels: Capability to search and select hotels.
  - Find Attractions: Capability to search and select attractions.
  - Search Airbnb: Capability to search airbnb locations and listings.
  - Analyze Travel Results: Capability to analyze raw agent search outputs and reformat into application schema.
Resources:
  - outboundFlight (Flight object): Domain Flight object produced by searchFlights: includes airline, flightNumber, departure/arrival airports/cities/times, duration, price, legs.
  - returnFlight (Flight object): Return flight object (same structure as outbound).
  - accommodation (Hotel or Airbnb listing): Hotel or Airbnb domain object with fields: name, rating, pricePerNight or price, images, location, address, description, amenities.
  - attractions (list of Attraction): Array of Attraction items recommended for trip.
  - Formatted travel plan (travelSchema): Final application JSON matching travelSchema with flights.outbound, flights.return, accommodation, attractions.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: search_flights_tool — unknown tool class "GetFlightInfosearchFlights"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("GetFlightInfosearchFlights")
def search_flights_tool(*args, **kwargs) -> str:
    """Fetches flight information for a given date range, origin and destination. Origin and Destination ar"""
    return "search_flights_tool result"

# TODO: search_hotels_tool — unknown tool class "SearchHotelssearchHotels"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SearchHotelssearchHotels")
def search_hotels_tool(*args, **kwargs) -> str:
    """Searches for hotels in a specified location. Destination is a cityId like 20015732 for 20015733"""
    return "search_hotels_tool result"

# TODO: search_attractions_tool — unknown tool class "SearchAttractionssearchAttractions"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SearchAttractionssearchAttractions")
def search_attractions_tool(*args, **kwargs) -> str:
    """Searches for attractions in a specified location. Destination is a cityId like 20015732 for 20015733"""
    return "search_attractions_tool result"

# TODO: search_airbnb_location_tool — unknown tool class "SearchAirbnbLocationsearchAirbnbLocation"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SearchAirbnbLocationsearchAirbnbLocation")
def search_airbnb_location_tool(*args, **kwargs) -> str:
    """Searches for Airbnb places in a specified location. Place is a city name like New York, NY"""
    return "search_airbnb_location_tool result"

# TODO: search_airbnb_tool — unknown tool class "SearchAirbnbsearchAirbnb"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SearchAirbnbsearchAirbnb")
def search_airbnb_tool(*args, **kwargs) -> str:
    """Searches for Airbnb in a specified location. Place is a cityId like 20015732 for 20015733"""
    return "search_airbnb_tool result"




@CrewBase
class TravelAISystemMastraexampleapp:
    """TravelAISystemMastraexampleapp crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def travel_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_agent'],
            tools=[search_flights_tool, search_hotels_tool, search_attractions_tool, search_airbnb_location_tool, search_airbnb_tool],
        )

    @agent
    def travel_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_analyzer'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def sync_csv_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['sync_csv_data_task'],
        )

    @task
    def find_outbound_flight(self) -> Task:
        return Task(
            config=self.tasks_config['find_outbound_flight'],
            agent=self.travel_agent(),
            context=[self.sync_csv_data_task()],
        )

    @task
    def find_return_flight(self) -> Task:
        return Task(
            config=self.tasks_config['find_return_flight'],
            context=[self.sync_csv_data_task()],
        )

    @task
    def find_accommodation_hotel_or_airbnb(self) -> Task:
        return Task(
            config=self.tasks_config['find_accommodation_hotel_or_airbnb'],
        )

    @task
    def find_attractions(self) -> Task:
        return Task(
            config=self.tasks_config['find_attractions'],
        )

    @task
    def analyze_and_format_results(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_and_format_results'],
            agent=self.travel_analyzer(),
        )

    @task
    def travel_agent_participates_in_planning_tasks(self) -> Task:
        return Task(
            config=self.tasks_config['travel_agent_participates_in_planning_tasks'],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the TravelAISystemMastraexampleapp"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
