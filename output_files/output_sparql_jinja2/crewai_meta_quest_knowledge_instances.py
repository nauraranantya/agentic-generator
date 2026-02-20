"""
Auto-generated CrewAI Script
Source : AgentO Knowledge Graph
Pipeline: SPARQL extraction + Jinja2 template rendering
"""

from crewai import Agent, Task, Crew
import os

# ===========================================================
# Agents
# ===========================================================

meta_quest_expert = Agent(
    role='Meta Quest Expert',
    goal='Goal expressed in agents configuration to provide best answers to questions about Meta Quest.',
    backstory="""An LLM-based agent configured to answer questions about Meta Quest using provided knowledge sources and a task-driven prompt. Created from agents configuration 'config/agents.yaml'.""",
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

answer_question_task = Task(
    description="""Answer the user question with the most relevant information from the context and available knowledge sources. Question: {question}

Do not answer questions that are not related to the context or knowledge sources.""",
    expected_output='Best answer to the user question',
    agent=meta_quest_expert
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[meta_quest_expert],
        tasks=[answer_question_task],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
