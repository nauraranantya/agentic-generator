"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Objectives:
  - : Objective representing the evaluation goal to measure the relevancy of ycAgent answers using an automatic scorer.
  - : Objective requiring the agent to answer questions about companies in the YC 2024 directory using only the dataset fields: name, longDescription, tags, industries, batch.
Capabilities:
  - : A scorer created by createAnswerRelevancyScorer used in tests: model 'openai/gpt-4o' with options scale:1 and uncertaintyWeight:0.3.
Resources:
  - : The Y Combinator Directory data used by the yc-directory tool (set in src/mastra/data/2024.ts). This dataset is an array of company objects; each object contains name, longDescription, tags, industries, batch fields. The original array is located in the project at src/mastra/data/2024.ts and contains many company entries for F24, S24, W24 batches and others. For fidelity, the dataset reference path is preserved here rather than embedding the entire array into the ontology file. Use the referenced file to obtain the full literal data when reconstructing the system.
  - : Single evaluation input used in tests: { input: 'Can you tell me what recent YC companies are working on AI Frameworks?' }
  - : Results produced by the evaluation runner when scoring the agent's output for the input question using the AnswerRelevancyScorer.
  - : References the key source files used to construct this ontology population: src/mastra/index.ts, src/mastra/agents/index.ts, src/mastra/tools/index.ts, src/mastra/data/2024.ts, src/mastra/tests/index.ts.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: yc_directory_tool — unknown tool class "ycdirectorytool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("ycdirectorytool")
def yc_directory_tool(*args, **kwargs) -> str:
    """Tool that returns the Y Combinator 2024 directory data. Created in src/mastra/tools/index.ts. Expose"""
    return "yc_directory_tool result"

# TODO: mastra_evals_runner — unknown tool class "mastraevalsrunner"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("mastraevalsrunner")
def mastra_evals_runner(*args, **kwargs) -> str:
    """Represents the runEvals invocation in src/mastra/tests/index.ts. Executes an evaluation run on a tar"""
    return "mastra_evals_runner result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def yc_directory_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['yc_directory_agent'],
            tools=[yc_directory_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def run_evals_task(self) -> Task:
        return Task(
            config=self.tasks_config['run_evals_task'],
        )

    @task
    def fetch_yc_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_yc_data_task'],
        )

    @task
    def answer_yc_directory_query(self) -> Task:
        return Task(
            config=self.tasks_config['answer_yc_directory_query'],
            agent=self.yc_directory_agent(),
            context=[self.fetch_yc_data_task()],
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
