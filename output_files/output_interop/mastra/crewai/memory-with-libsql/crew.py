"""
Auto-generated CrewAI Crew: MastraSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Resources:
  - : Placeholder resource identifier used in the source code to represent a user-specific memory resource (resource = 'SOME_USER_ID').
  - : Represents the streaming text output produced by agent.stream in the implementation (modeled as a Resource instance).
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
    def chef_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chef_agent'],
        )

    @agent
    def memory_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['memory_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_initial_ingredients_query(self) -> Task:
        return Task(
            config=self.tasks_config['task_initial_ingredients_query'],
            agent=self.chef_agent(),
        )

    @task
    def task_ingredients_at_friend_s_house(self) -> Task:
        return Task(
            config=self.tasks_config['task_ingredients_at_friend_s_house'],
            agent=self.chef_agent(),
        )

    @task
    def task_ask_what_we_cooked_before(self) -> Task:
        return Task(
            config=self.tasks_config['task_ask_what_we_cooked_before'],
            agent=self.chef_agent(),
        )

    @task
    def task_memory_agent_recall_operation(self) -> Task:
        return Task(
            config=self.tasks_config['task_memory_agent_recall_operation'],
            agent=self.memory_agent(),
        )

    @task
    def exit(self) -> Task:
        return Task(
            config=self.tasks_config['exit'],
            agent=self.chef_agent(),
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
