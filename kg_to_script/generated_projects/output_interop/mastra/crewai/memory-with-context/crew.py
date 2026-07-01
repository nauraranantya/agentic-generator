"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Resources:
  - : Represents the external user resource identifier passed as resourceId to the agent.stream calls in the code (literal in source: 'SOME_USER_ID').
  - : A textual stream produced by the agent.stream operation; in implementation this is masked/filtered for 'think' and 'working_memory' tags and presented to the console.
Constraints:
  - : Behavioral rule: The program calls memory.getThreadById({ threadId }) and sets isFirstChat to true when no thread exists (Boolean(...) === false). This affects which system prompt template is used (prompt_system_firstChat vs prompt_system_returningChat).
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
    def memory_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['memory_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_initial_system_message(self) -> Task:
        return Task(
            config=self.tasks_config['task_initial_system_message'],
            agent=self.memory_agent(),
        )

    @task
    def task_receive_user_input(self) -> Task:
        return Task(
            config=self.tasks_config['task_receive_user_input'],
            agent=self.memory_agent(),
        )

    @task
    def task_agent_stream_response(self) -> Task:
        return Task(
            config=self.tasks_config['task_agent_stream_response'],
            agent=self.memory_agent(),
        )

    @task
    def task_interactive_chat(self) -> Task:
        return Task(
            config=self.tasks_config['task_interactive_chat'],
            agent=self.memory_agent(),
        )

    @task
    def task_agent_instantiation(self) -> Task:
        return Task(
            config=self.tasks_config['task_agent_instantiation'],
            agent=self.memory_agent(),
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
