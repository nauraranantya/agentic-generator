"""
Auto-generated AutoGen Team: GameBuilderCrew
Goals:
  - Create Game (Team Goal): Produce a working python game implementation given a textual game description input. The system assembles agents and tasks to generate, review, and evaluate final python code for a game (examples include Pac-Man and Snake).
  - Create software as needed: Create software as needed
  - Create Perfect code: Create Perfect code, by analyzing the code that is given for errors
  - Ensure the code does the job that it is supposed to do: Ensure that the code fulfills the functional requirements of the game description and is complete.
Resources:
  - initial_game_code: Python code produced by senior_engineer_agent in response to the game description input.
  - reviewed_game_code: Code after QA review by qa_engineer_agent; errors fixed and issues annotated in code response (final output is the corrected python code).
  - final_game_code: Final python code for the requested game after generation, review, and evaluation steps. Example inputs available in src/game_builder_crew/config/gamedesign.yaml (example1_pacman, example2_pacman, example3_snake).
"""

from autogen_agentchat.agents import AssistantAgent

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import (

    MaxMessageTermination

)

from autogen_core.tools import FunctionTool

from autogen_ext.models.openai import (
    OpenAIChatCompletionClient
)

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini"
)


# ==================================================
# Generated Tool Stubs
# ==================================================


# ==================================================
# Agents
# ==================================================


senior_engineer_agent = AssistantAgent(
    name="senior_engineer_agent",
    model_client=model_client,
    system_message="""
Role:
Senior Software Engineer

Goal:
Create software as needed

Background:
Role: Senior Software Engineer
""",
)


qa_engineer_agent = AssistantAgent(
    name="qa_engineer_agent",
    model_client=model_client,
    system_message="""
Role:
Software Quality Control Engineer

Goal:
Create Perfect code, by analyzing the code that is given for errors

Background:
Role: Software Quality Control Engineer
""",
)


chief_qa_engineer_agent = AssistantAgent(
    name="chief_qa_engineer_agent",
    model_client=model_client,
    system_message="""
Role:
Chief Software Quality Control Engineer

Goal:
Ensure that the code fulfills the functional requirements of the game description and is complete.

Background:
Role: Chief Software Quality Control Engineer
""",
)



