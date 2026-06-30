"""
Auto-generated CrewAI Crew: ClientApplicationViteReactTeam

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Interactive browser UI driven by agent: Goal for the client app: enable an interactive UI where the language model/agent can instruct the browser to perform UI changes and stream text responses.
  - Provide interactive user experience: Higher-level goal: deliver a streaming conversational experience with dynamic UI updates triggered by model-invoked tool calls.
Objectives:
  - Enable user-agent interactive messaging: Objective to allow a human user to send free-text messages to the agent and receive streaming responses.
  - Handle streaming responses and events: Objective to properly process streaming data, including tool call events, tool results, deltas, and text parts.
  - Apply UI updates requested via tool calls: Objective to apply client-side state changes (color, logo size, posts) as requested by tool calls from the agent.
Human Agents:
  - human_user ()
Capabilities:
  - Change background color: Capability to change the UI color state (expects a single string property 'color').
  - Change logo size: Capability to change the UI logo size. Expects 'height' and 'width' string properties.
  - Add a new post: Capability to append a new post entry containing 'color' and 'name' to the posts collection in the client.
Resources:
  - background color state: Abstract representation of the application background color state (corresponds to React state 'color' in src/App.tsx).
  - logo size state: Abstract representation of the logo size state (corresponds to React state 'logoSize' with keys 'height' and 'width').
  - posts list state: Abstract representation of the posts array in client state (React state 'posts'). Items are objects with properties 'name' and 'color'.
  - response text stream: Cumulative response text displayed in the UI (state 'responseText' appended by streaming onTextPart handler).
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: tool_change_color — unknown tool class "changeColor"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("changeColor")
def tool_change_color(*args, **kwargs) -> str:
    """Client-side tool that changes the application background color. Declared in clientSideToolCallsMap i"""
    return "tool_change_color result"

# TODO: tool_change_logo_size — unknown tool class "changeLogoSize"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("changeLogoSize")
def tool_change_logo_size(*args, **kwargs) -> str:
    """Client-side tool that changes the size of the logo. Declared in clientSideToolCallsMap in src/App.ts"""
    return "tool_change_logo_size result"

# TODO: tool_add_post — unknown tool class "addPost"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("addPost")
def tool_add_post(*args, **kwargs) -> str:
    """Client-side tool that adds a new post to the 'posts' state array. Declared in clientSideToolCallsMap"""
    return "tool_add_post result"




@CrewBase
class ClientApplicationViteReactTeam:
    """ClientApplicationViteReactTeam crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def agent(self) -> Agent:
        return Agent(
            config=self.agents_config['agent'],
            tools=[tool_change_color, tool_change_logo_size, tool_add_post],
        )

    @agent
    def test_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['test_agent'],
            tools=[tool_change_color, tool_change_logo_size, tool_add_post],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def append_text_parts_to_the_response_text_state(self) -> Task:
        return Task(
            config=self.tasks_config['append_text_parts_to_the_response_text_state'],
            agent=self.agent(),
        )

    @task
    def user_submits_message(self) -> Task:
        return Task(
            config=self.tasks_config['user_submits_message'],
            agent=self.agent(),
            context=[self.append_text_parts_to_the_response_text_state()],
        )

    @task
    def stream_message_to_agent(self) -> Task:
        return Task(
            config=self.tasks_config['stream_message_to_agent'],
            agent=self.agent(),
            context=[self.append_text_parts_to_the_response_text_state()],
        )

    @task
    def process_streamed_events_tool_calls_tool_results_deltas_text_parts(self) -> Task:
        return Task(
            config=self.tasks_config['process_streamed_events_tool_calls_tool_results_deltas_text_parts'],
            agent=self.agent(),
        )

    @task
    def execute_change_color_tool(self) -> Task:
        return Task(
            config=self.tasks_config['execute_change_color_tool'],
            agent=self.agent(),
        )

    @task
    def execute_change_logo_size_tool(self) -> Task:
        return Task(
            config=self.tasks_config['execute_change_logo_size_tool'],
            agent=self.agent(),
        )

    @task
    def execute_add_post_tool(self) -> Task:
        return Task(
            config=self.tasks_config['execute_add_post_tool'],
            agent=self.agent(),
        )

    @task
    def stream_it_function_logic_description(self) -> Task:
        return Task(
            config=self.tasks_config['stream_it_function_logic_description'],
            agent=self.agent(),
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the ClientApplicationViteReactTeam"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
