import asyncio

from team import (
    generative_ui_supervisor,
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
        # Workflow Step: router_task
        # Workflow Edge: router_task -> stockbroker_task
        # Workflow Edge: router_task -> trip_planner_task
        # Workflow Edge: router_task -> open_code_task
        # Workflow Edge: router_task -> order_pizza_task
        # Workflow Edge: router_task -> general_input_task
        # Workflow Edge: router_task -> writer_agent_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: router_task")
        print("=" * 80)

        task_prompt = """You're a highly helpful AI assistant, tasked with routing the user's query to the appropriate tool.
You should analyze the user's input, and choose the appropriate tool to use."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: stockbroker_task
        # Workflow Edge: stockbroker_task -> trip_planner_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: stockbroker_task")
        print("=" * 80)

        task_prompt = """Stockbroker Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: trip_planner_task
        # Workflow Edge: trip_planner_task -> open_code_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: trip_planner_task")
        print("=" * 80)

        task_prompt = """Trip Planner Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: open_code_task
        # Workflow Edge: open_code_task -> order_pizza_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: open_code_task")
        print("=" * 80)

        task_prompt = """Open Code Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: order_pizza_task
        # Workflow Edge: order_pizza_task -> general_input_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: order_pizza_task")
        print("=" * 80)

        task_prompt = """Order Pizza Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: general_input_task
        # Workflow Edge: general_input_task -> writer_agent_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: general_input_task")
        print("=" * 80)

        task_prompt = """You are an AI assistant.
If the user asks what you can do, describe these tools.
- stockbroker: can fetch the price of a ticker, purchase/sell a ticker, or get the user's portfolio
- tripPlanner: helps the user plan their trip. it can suggest restaurants, and places to stay in any given location.
- openCode: can write a React TODO app for the user. Only call this tool if they request a TODO app.
- orderPizza: can order a pizza for the user
- writerAgent: can write a text document for the user. Only call this tool if they request a text document.

If the last message is a tool result, describe what the action was, congratulate the user, or send a friendly followup in response to the tool action. Ensure this is a clear and concise message.

Otherwise, just answer as normal."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: writer_agent_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: writer_agent_task")
        print("=" * 80)

        task_prompt = """Writer Agent Task"""
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