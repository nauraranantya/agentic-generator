"""
Auto-generated CrewAI Main: GameBuilderCrew

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
"""

import sys
import yaml
from dotenv import load_dotenv

# Load .env from this directory BEFORE importing crew (which triggers crewai init)
load_dotenv()

from crew import GameBuilderCrew


def run():
    """Run the GameBuilderCrew."""
    print("## Welcome to the Game Crew")
    print("-------------------------------")

    with open('config/gamedesign.yaml', 'r', encoding='utf-8') as file:
        examples = yaml.safe_load(file)

    inputs = {
        'game': examples['example3_snake'],
    }
    result = GameBuilderCrew().crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print("final code for the game:")
    print(result)
    return result


def train():
    """Train the GameBuilderCrew for a given number of iterations."""
    with open('config/gamedesign.yaml', 'r', encoding='utf-8') as file:
        examples = yaml.safe_load(file)

    inputs = {
        'game': examples['example1_pacman'],
    }
    try:
        GameBuilderCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


if __name__ == "__main__":
    result = run()
    print(result)
