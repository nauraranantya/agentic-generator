import asyncio

from team import (
    famous_person_generator,
    game_agent,
    guess_verifier_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: start_task_generate_famous_person
        # Workflow Edge: start_task_generate_famous_person -> a_and_guess_handling
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: start_task_generate_famous_person")
        print("=" * 80)

        task_prompt = """Task logic (semantic description, original source behavior preserved):
- Input: { start: boolean }
- Action: Use the Famous Person Generator agent to 'Generate a famous person's name' with model parameters { temperature: 1.2, topP: 0.9 } and memory context:
  memory.resource = 'heads-up-game', memory.thread = 'famous-person-generator'
- Output: { famousPerson: string, guessCount: 0 }
- Performed by the Famous Person Generator agent.
Notes: The agent must return only the person's name as a plain string. The runtime must strip whitespace and set guessCount to 0."""
        # Execute via the assigned agent: famous_person_generator
        result = await famous_person_generator.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: a_and_guess_handling
        # Workflow Edge: a_and_guess_handling -> win_task_finalization
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: a_and_guess_handling")
        print("=" * 80)

        task_prompt = """Task logic (semantic description, original source preserved):
- Input: { famousPerson: string, guessCount: number }
- Resume Schema: { userMessage: string }
- Suspend Schema: { suspendResponse: string }
- If no resumeData.userMessage: suspend with message "I'm thinking of a famous person. Ask me yes/no questions to figure out who it is!"
- Otherwise, call the Game Agent with an instruction template which provides the famousPerson and the user's message and requests a structured JSON output:
  output: { response: string, gameWon: boolean }
- The structured response's 'gameWon' indicates whether the user guessed correctly.
- Increment guessCount each time the agent is called (for each resume with a userMessage).
- Returns: { famousPerson, gameWon, agentResponse, guessCount }.
- Performed by the Game Agent (the agent must never reveal the famous person's name).
- The runtime must enforce the JSON structure in the agent response and extract 'response' and 'gameWon' fields."""
        # Execute via the assigned agent: game_agent
        result = await game_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: win_task_finalization
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: win_task_finalization")
        print("=" * 80)

        task_prompt = """Finalization task:
- Input: { famousPerson: string, gameWon: boolean, agentResponse: string, guessCount: number }
- Action: Log/return the final values (famousPerson, gameWon, guessCount) and complete the workflow.
- In the original source, this step writes console.log messages for the famousPerson, gameWon and guessCount.
- Output: { famousPerson, gameWon, guessCount }.
Notes: No agent call required for this step in the provided implementation."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        print("\n" + "=" * 80)
        print("DONE")
        print("=" * 80)

    except Exception as e:
        print("\n" + "=" * 80)
        print("ERROR")
        print("=" * 80)
        print(type(e).__name__)
        print(str(e))



if __name__ == "__main__":
    asyncio.run(main())