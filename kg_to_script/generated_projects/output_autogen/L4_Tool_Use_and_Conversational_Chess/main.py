import asyncio

from team import (
    player_white,
    player_black,
    board_proxy,
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
        # Workflow Step: task_initiate_chat
        # Workflow Edge: task_initiate_chat -> task_board_proxy_summary_to_white
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_initiate_chat")
        print("=" * 80)

        task_prompt = """player_black initiates the game chat to start a move sequence. """
        # Execute via the assigned agent: player_black
        result = await player_black.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_board_proxy_summary_to_white
        # Workflow Edge: task_board_proxy_summary_to_white -> task_get_legal_moves
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_board_proxy_summary_to_white")
        print("=" * 80)

        task_prompt = """Board proxy provides last message summary to the white player before the player's turn. """
        # Execute via the assigned agent: board_proxy
        result = await board_proxy.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_get_legal_moves
        # Workflow Edge: task_get_legal_moves -> task_make_move
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_get_legal_moves")
        print("=" * 80)

        task_prompt = """Player requests the list of legal moves for selection. """
        # Execute via the assigned agent: player_white
        result = await player_white.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_make_move
        # Workflow Edge: task_make_move -> task_check_made_move
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_make_move")
        print("=" * 80)

        task_prompt = """Player makes a selected move by calling make_move(move). """
        # Execute via the assigned agent: player_white
        result = await player_white.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_check_made_move
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_check_made_move")
        print("=" * 80)

        task_prompt = """Board proxy evaluates the made_move flag to determine if the nested chat should terminate. """
        # Execute via the assigned agent: board_proxy
        result = await board_proxy.run(task=task_prompt)

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