"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Resources:
  - : The raw user input string read from stdin and provided to the agent as the `answer` parameter in agent.stream(answer, { threadId, resourceId }). Example content: "What's the meaning of life?".
  - : Text response produced by the agent through agent.stream. The code receives a streaming text iterator (textStream) and applies maskStreamTags(textStream, 'think', ...) to handle 'think' tags and update UI spinner. The final output is printed to stdout. Streaming semantics (chunks, think masks) are modeled as descriptive text.
Constraints:
  - : The source code uses maskStreamTags(textStream, 'think', { onStart, onMask, onEnd }) to treat 'think' annotation tags within the stream, updating a spinner (ora) and coloring (gradient). These are runtime/UI behaviors and are represented as descriptive metadata attached to the TextResponseResource and Task, not as executable components.
  - : The main loop reads stdin via Readline, prompts the user, and sends inputs to agent.stream. The event-loop and readline implementation are presented as descriptive context for the ChatInteractionTask.
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
    def example_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['example_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def chat_interaction_task(self) -> Task:
        return Task(
            config=self.tasks_config['chat_interaction_task'],
            agent=self.example_agent(),
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
