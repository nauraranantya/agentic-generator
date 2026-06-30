"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Human Agents:
  - user_human ()
Capabilities:
  - Compose Email: Generate a draft email (subject, body, to) from conversation history.
  - Rewrite Email: Rewrite email content given user's response/instructions; should only change requested fields.
  - Send Email: Finalize and send the composed email (in this implementation it yields a confirmation message indicating successful send).
  - Handle Human Interrupt: Present the email to a human for review and accept/edit/ignore/response and handle the resulting input accordingly.
Resources:
  - Conversation History: Sequence of messages between user and agent used as input to generate the email. In implementation substituted into the prompt via {CONVERSATION}.
  - Draft Email: Structured email artifact with fields:
- subject: string
- body: string
- to: string

This is the primary data produced by the writing and rewriting tasks. The implementation expects these exact fields.
  - Sent Email Record: A record/artifact representing that the email was sent. In implementation returned as an AI message: 'Successfully sent email.' (represented as an artifact here).
  - Human Response (interrupt result): Represents the human-interaction result from the interrupt UI. Possible response types recorded in implementation: 'ignore', 'response', 'accept', or 'edit' (with args carrying edited email fields). This ontology stores allowed values in the interrupt config and records that user participated in interrupt interactions.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: write_email_tool — unknown tool class "writeemailtoolschemabound"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("writeemailtoolschemabound")
def write_email_tool(*args, **kwargs) -> str:
    """Tool binding used by the LLM to produce structured email objects. Description: "Write an email based"""
    return "write_email_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def email_assistant_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_assistant_agent'],
            tools=[write_email_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def write_email_generate_draft(self) -> Task:
        return Task(
            config=self.tasks_config['write_email_generate_draft'],
            agent=self.email_assistant_agent(),
        )

    @task
    def rewrite_email_apply_user_s_requested_changes(self) -> Task:
        return Task(
            config=self.tasks_config['rewrite_email_apply_user_s_requested_changes'],
            agent=self.email_assistant_agent(),
        )

    @task
    def ignore(self) -> Task:
        return Task(
            config=self.tasks_config['ignore'],
            context=[self.rewrite_email_apply_user_s_requested_changes()],
            human_input=True,
        )

    @task
    def send_email_finalize_send(self) -> Task:
        return Task(
            config=self.tasks_config['send_email_finalize_send'],
            agent=self.email_assistant_agent(),
            context=[self.rewrite_email_apply_user_s_requested_changes()],
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
