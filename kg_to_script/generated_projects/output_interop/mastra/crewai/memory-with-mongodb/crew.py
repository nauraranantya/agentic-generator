"""
Auto-generated CrewAI Crew: MastraSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Capabilities:
  - Recipe suggestion: Capability: suggest recipes and high-level steps given available ingredients; described by the Chef Agent instructions.
  - Memory recall and conversation continuity: Capability: recall past messages and maintain long-running conversation states.
Resources:
  - SOME_USER_ID: 
  - Recipe suggestion: pasta-based suggestions: 
  - Recipe suggestion: chicken-curry suggestions: 
  - Memory-based recipe recall: 
  - Welcome/restart message: 
  - thread:39873fbf-84d6-425e-8c1b-8afd798d72a4: 
  - thread:randomUUID(): 
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: openai_tool — unknown tool class "OpenAISDKtool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("OpenAISDKtool")
def openai_tool(*args, **kwargs) -> str:
    """Representing the usage of the OpenAI SDK via openai(...) calls in the source code."""
    return "openai_tool result"

# TODO: mongo_db_store — unknown tool class "MongoDBStoretool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("MongoDBStoretool")
def mongo_db_store(*args, **kwargs) -> str:
    """Storage backend used by Memory.storage in code (MongoDBStore). The code uses process.env.MONGODB_URI"""
    return "mongo_db_store result"

# TODO: mongo_db_vector — unknown tool class "MongoDBVectorvectorstoretool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("MongoDBVectorvectorstoretool")
def mongo_db_vector(*args, **kwargs) -> str:
    """Vector store used for semantic recall via MongoDB-backed vectors (MongoDBVector)."""
    return "mongo_db_vector result"




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
            tools=[openai_tool, mongo_db_store],
        )

    @agent
    def memory_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['memory_agent'],
            tools=[openai_tool, mongo_db_store, mongo_db_vector],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def chef_initial_recipe_suggestion_task(self) -> Task:
        return Task(
            config=self.tasks_config['chef_initial_recipe_suggestion_task'],
            agent=self.chef_agent(),
        )

    @task
    def chef_friend_s_ingredients_recipe_suggestion_task(self) -> Task:
        return Task(
            config=self.tasks_config['chef_friend_s_ingredients_recipe_suggestion_task'],
            agent=self.chef_agent(),
        )

    @task
    def chef_memory_query_task_asks_what_was_cooked_earlier(self) -> Task:
        return Task(
            config=self.tasks_config['chef_memory_query_task_asks_what_was_cooked_earlier'],
            agent=self.chef_agent(),
        )

    @task
    def chat_initial_system_message_task(self) -> Task:
        return Task(
            config=self.tasks_config['chat_initial_system_message_task'],
            agent=self.memory_agent(),
        )

    @task
    def chat_interactive_loop_task(self) -> Task:
        return Task(
            config=self.tasks_config['chat_interactive_loop_task'],
            agent=self.memory_agent(),
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
