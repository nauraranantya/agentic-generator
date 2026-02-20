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

senior_engineer_agent = Agent(
    role='Senior Software Engineer',
    goal='Create software as needed',
    backstory="""You are a Senior Software Engineer at a leading tech think tank.
Your expertise in programming in python. and do your best to produce perfect code""",
    verbose=True
)

qa_engineer_agent = Agent(
    role='Software Quality Control Engineer',
    goal='Create Perfect code, by analyzing the code that is given for errors',
    backstory="""You are a software engineer that specializes in checking code
for errors. You have an eye for detail and a knack for finding
hidden bugs.
You check for missing imports, variable declarations, mismatched
brackets and syntax errors.
You also check for security vulnerabilities, and logic errors""",
    verbose=True
)

chief_qa_engineer_agent = Agent(
    role='Chief Software Quality Control Engineer',
    goal='Ensure that the code fulfills the functional requirements of the game description and is complete.',
    backstory="""You feel that programmers always do only half the job, so you are
super dedicate to make high quality code.""",
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

code_task = Task(
    description="""You will create a game using python, these are the instructions:

Instructions
------------
{game}""",
    expected_output='Your Final answer must be the full python code, only the python code and nothing else.',
    agent=senior_engineer_agent
)

review_task = Task(
    description="""You will create a game using python, these are the instructions:

Instructions
------------
{game}

Using the code you got, check for errors. Check for logic errors,
syntax errors, missing imports, variable declarations, mismatched brackets,
and security vulnerabilities.""",
    expected_output='Your Final answer must be the full python code, only the python code and nothing else.',
    agent=qa_engineer_agent
)

evaluate_task = Task(
    description="""You are helping create a game using python, these are the instructions:

Instructions
------------
{game}

You will look over the code to insure that it is complete and
does the job that it is supposed to do.""",
    expected_output='Your Final answer must be the full python code, only the python code and nothing else.',
    agent=chief_qa_engineer_agent
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[senior_engineer_agent, qa_engineer_agent, chief_qa_engineer_agent],
        tasks=[code_task, review_task, evaluate_task],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
