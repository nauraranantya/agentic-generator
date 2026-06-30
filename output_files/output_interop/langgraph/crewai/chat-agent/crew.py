"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Resources:
  - : The output messages (array/object) returned by the Language Model invocation for the chat task. In the source this is the 'response' object assigned to { messages: response } and returned by the node.
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
    def chat_agent_1(self) -> Agent:
        return Agent(
            config=self.agents_config['chat_agent_1'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def chat_task(self) -> Task:
        return Task(
            config=self.tasks_config['chat_task'],
            agent=self.chat_agent_1(),
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
