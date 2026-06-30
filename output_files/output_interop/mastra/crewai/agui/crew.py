"""
Auto-generated CrewAI Crew: MastraSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Resources:
  - : Top-level Mastra storage created in src/mastra/index.ts. Uses LibSQLStore with id 'agui-storage' and url ':memory:' by default.
  - : LibSQLStore used by the Weather Agent's Memory. Path in code: 'file:../mastra.db' (relative to .mastra/output directory).
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task




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
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def network_supervisor_task(self) -> Task:
        return Task(
            config=self.tasks_config['network_supervisor_task'],
            agent=self.weather_agent(),
        )

    @task
    def copilotkit(self) -> Task:
        return Task(
            config=self.tasks_config['copilotkit'],
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
