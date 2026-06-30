import asyncio

from team import (
    todo_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "timestamp":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: init_return_chat_task
        # Workflow Edge: init_return_chat_task -> present_list_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: init_return_chat_task")
        print("=" * 80)

        task_prompt = """Chat with user started now {timestamp}. Don't mention this message. This means some time has passed between this message and the one before. The user left and came back again. Say something to start the conversation up again."""
        # Execute via the assigned agent: todo_agent
        result = await todo_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: present_list_task
        # Workflow Edge: present_list_task -> update_list_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: present_list_task")
        print("=" * 80)

        task_prompt = """You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later."""
        # Execute via the assigned agent: todo_agent
        result = await todo_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: update_list_task
        # Workflow Edge: update_list_task -> timebox_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: update_list_task")
        print("=" * 80)

        task_prompt = """You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later."""
        # Execute via the assigned agent: todo_agent
        result = await todo_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: timebox_task
        # Workflow Edge: timebox_task -> save_working_memory_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: timebox_task")
        print("=" * 80)

        task_prompt = """You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later."""
        # Execute via the assigned agent: todo_agent
        result = await todo_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: save_working_memory_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: save_working_memory_task")
        print("=" * 80)

        task_prompt = """You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later."""
        # Execute via the assigned agent: todo_agent
        result = await todo_agent.run(task=task_prompt)

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