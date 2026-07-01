import asyncio

from team import (
    player_white,
    player_black,
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
        # Workflow Step: task_initiate_chat_black_white
        # Workflow Edge: task_initiate_chat_black_white -> task_make_move
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_initiate_chat_black_white")
        print("=" * 80)

        task_prompt = """Let's play chess! Your move. """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_make_move
        # Workflow Edge: task_make_move -> task_make_move
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_make_move")
        print("=" * 80)

        task_prompt = """Call make_move(move) with a single move argument in UCI format when selecting a move to apply. Expect a textual confirmation describing the moved piece and board update. """
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