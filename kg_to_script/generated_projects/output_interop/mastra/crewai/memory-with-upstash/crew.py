"""
Auto-generated CrewAI Crew: Mastrasystemagentorchestrator

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Improve user's cooking experience: 
Objectives:
  - Help user cook with available ingredients: Collective objective assigned to the Mastra system's agents to assist users in cooking with available ingredients.
Capabilities:
  - Key-value storage capability: Capability representing storing/retrieving messages or data in a key-value store.
  - Vector DB capability: Capability representing vector embedding storage and semantic recall operations.
  - Language model access capability: Capability to invoke and stream responses from a language model.
Resources:
  - User provided ingredients (initial): pasta, canned tomatoes, garlic, olive oil, dried herbs (basil and oregano)
  - Recipe suggestions (initial): Output resource containing brief high-level steps for recipes the Chef Agent suggests given the initial ingredients.
  - User provided ingredients (friend's house): chicken thighs, coconut milk, sweet potatoes, curry powder
  - Recipe suggestions (friend's house): Output resource containing brief high-level steps for recipes suggested for friend's ingredients.
  - Recipe recall output: Memory-influenced response listing what was cooked previously in the same thread/session.
  - src/index.ts (example run description): Describes the example orchestrated run: constructs threadId via randomUUID(); calls agent.stream with user messages; logs streaming chunks to stdout; final call includes memoryOptions { lastMessages: 3 }.
  - src/bubble.ts (message bubble utility - UI/formatting only): A local formatting utility for console output (borders, wrapping). Not modeled as tool used by agents for decision making; included for completeness as a resource artifact.
  - Upstash HTTP store (resource): Represents the Upstash storage resource reachable at http://localhost:8089 with token 'test_token' as in source.
  - PgVector Postgres instance (resource): Represents the Postgres instance used by PgVector (connection string postgresql://postgres:postgres@localhost:5433).
  - thread session resource: Session/thread metadata for a run. threadId is generated using randomUUID() at runtime (source). resourceId used in calls is 'SOME_USER_ID'.
  - Example run (index.ts main()): Sequence executed by src/index.ts: (1) call chefAgent.stream with initial ingredients; (2) call chefAgent.stream with friend's ingredients; (3) call chefAgent.stream to ask what was cooked before with memoryOptions override; then process.exit(0). Each call uses threadId and resourceId parameters; threadId is randomUUID() per run; resourceId set to 'SOME_USER_ID' in source.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: memory_storage_upstash_tool — unknown tool class "UpstashStoreKVstoreadapter"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("UpstashStoreKVstoreadapter")
def memory_storage_upstash_tool(*args, **kwargs) -> str:
    """Represents the Upstash HTTP-backed storage used by the memory implementation."""
    return "memory_storage_upstash_tool result"

# TODO: memory_vector_pg_tool — unknown tool class "PgVectorPostgresvectorstoreadapter"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("PgVectorPostgresvectorstoreadapter")
def memory_vector_pg_tool(*args, **kwargs) -> str:
    """Description for memory_vector_pg_tool"""
    return "memory_vector_pg_tool result"

# TODO: open_ai_sdk_tool — unknown tool class "OpenAISDKclientconceptualtool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("OpenAISDKclientconceptualtool")
def open_ai_sdk_tool(*args, **kwargs) -> str:
    """Conceptual representation of the OpenAI client used to call gpt-4o. SDK details are not modeled; con"""
    return "open_ai_sdk_tool result"




@CrewBase
class Mastrasystemagentorchestrator:
    """Mastrasystemagentorchestrator crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def chef_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chef_agent'],
            tools=[memory_storage_upstash_tool, memory_vector_pg_tool],
        )

    @agent
    def memory_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['memory_agent'],
            tools=[memory_storage_upstash_tool, memory_vector_pg_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def set_up_session_and_thread(self) -> Task:
        return Task(
            config=self.tasks_config['set_up_session_and_thread'],
            agent=self.memory_agent(),
        )

    @task
    def suggest_recipes_from_user_s_listed_ingredients(self) -> Task:
        return Task(
            config=self.tasks_config['suggest_recipes_from_user_s_listed_ingredients'],
            agent=self.chef_agent(),
        )

    @task
    def suggest_recipes_from_friend_s_ingredients(self) -> Task:
        return Task(
            config=self.tasks_config['suggest_recipes_from_friend_s_ingredients'],
            agent=self.chef_agent(),
        )

    @task
    def recall_what_was_cooked_previously(self) -> Task:
        return Task(
            config=self.tasks_config['recall_what_was_cooked_previously'],
            agent=self.chef_agent(),
            context=[self.set_up_session_and_thread()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the Mastrasystemagentorchestrator"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
