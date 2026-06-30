"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Order Pizza Goal: Top-level intent: find a pizza shop and place a pizza order for a user.
Capabilities:
  - find_store: Capability to find a pizza shop given a location and optional company name.
  - place_order: Capability to place a pizza order given store contact and order details.
Resources:
  - User Location (input): User-provided location string (e.g., 'San Francisco' or 'New York'). Required input for the findStore task.
  - Pizza Company Name (optional input): Optional user-provided pizza company name (e.g., 'Dominos' or 'Papa John's').
  - Store Information (found store): Example produced content (from code's toolResponse): "I've found a pizza shop at 1119 19th St, San Francisco, CA 94107. The phone number for the shop is 415-555-1234.". Also includes link to the tool_call_id produced by the model call in runtime (tool_call_id captured in code), represented here as descriptive metadata.
  - Order Details (input for placing order): Structured fields expected from place_pizza_order output: address (address of store), phone_number (store phone), order (full pizza order for the user).
  - Order Confirmation (produced resource): Example produced content (from code's toolResponse): "Pizza order successfully placed.". In runtime the tool_call_id linking the confirmation to the model/tool invocation is present; represented in this resource description.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: tool_pizza_finder — unknown tool class "PizzaFinderTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("PizzaFinderTool")
def tool_pizza_finder(*args, **kwargs) -> str:
    """Represents the external lookup mechanism that returns store contact information. In code this is emu"""
    return "tool_pizza_finder result"

# TODO: tool_pizza_ordering_system — unknown tool class "PizzaOrderingSystem"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("PizzaOrderingSystem")
def tool_pizza_ordering_system(*args, **kwargs) -> str:
    """Represents the external ordering mechanism that places the pizza order and returns confirmation. In """
    return "tool_pizza_ordering_system result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def pizza_orderer_v1(self) -> Agent:
        return Agent(
            config=self.agents_config['pizza_orderer_v1'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def find_pizza_shop_task(self) -> Task:
        return Task(
            config=self.tasks_config['find_pizza_shop_task'],
            agent=self.pizza_orderer_v1(),
        )

    @task
    def place_pizza_order_task(self) -> Task:
        return Task(
            config=self.tasks_config['place_pizza_order_task'],
            agent=self.pizza_orderer_v1(),
            context=[self.find_pizza_shop_task()],
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
