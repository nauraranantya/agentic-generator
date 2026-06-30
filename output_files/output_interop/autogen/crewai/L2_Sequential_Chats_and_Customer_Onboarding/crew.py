"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Human Agents:
  - customer_proxy_agent (customer_proxy)
Resources:
  - : Structured output expected from summary: JSON object of the form {'name': '', 'location': ''}.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def onboarding_personal_information_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['onboarding_personal_information_agent'],
        )

    @agent
    def onboarding_topic_preference_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['onboarding_topic_preference_agent'],
        )

    @agent
    def customer_engagement_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_engagement_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_collect_personal_info(self) -> Task:
        return Task(
            config=self.tasks_config['task_collect_personal_info'],
            human_input=True,
        )

    @task
    def task_collect_topic_preferences(self) -> Task:
        return Task(
            config=self.tasks_config['task_collect_topic_preferences'],
            human_input=True,
        )

    @task
    def task_customer_proxy_to_engagement(self) -> Task:
        return Task(
            config=self.tasks_config['task_customer_proxy_to_engagement'],
            human_input=True,
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
