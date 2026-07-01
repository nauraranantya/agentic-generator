"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - : 
Objectives:
  - : 
Capabilities:
  - conversational: Capability to hold a multi-turn conversation and respond to user inputs.
  - memory_update: Capability to update and persist working memory based on conversation content; expects <working_memory> tags to be used in outputs.
  - greet_returning_user: Capability to detect returning users and greet them referencing remembered information.
Resources:
  - : LibSQLStore persistent storage used for Memory. Source code: new LibSQLStore({ id: 'memory-demo-storage', url: 'file:./memory-demo.db' }). File path: file:./memory-demo.db
  - : Simulated resource ID for Alice (source: USERS.alice = 'user-alice-123').
  - : Simulated resource ID for Bob (source: USERS.bob = 'user-bob-456').
  - : Simulated demo user resource ID (source: USERS.demo = 'demo-user-789').
  - : At runtime, a random UUID is used to generate a resource ID (example: user-<uuid>). Represented here as a template; actual UUIDs are generated at runtime.
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
    def personal_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['personal_assistant'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_start_conversation(self) -> Task:
        return Task(
            config=self.tasks_config['task_start_conversation'],
            agent=self.personal_assistant(),
        )

    @task
    def task_update_memory(self) -> Task:
        return Task(
            config=self.tasks_config['task_update_memory'],
            agent=self.personal_assistant(),
        )

    @task
    def task_interactive_chat(self) -> Task:
        return Task(
            config=self.tasks_config['task_interactive_chat'],
            agent=self.personal_assistant(),
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
