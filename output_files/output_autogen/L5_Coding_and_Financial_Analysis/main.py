import asyncio

from team import (
    code_executor_agent,
    code_writer_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "today":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: stock_analysis_ytd_stock_gain_plot
        # Workflow Edge: stock_analysis_ytd_stock_gain_plot -> stock_analysis_ytd_stock_gain_plot
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: stock_analysis_ytd_stock_gain_plot")
        print("=" * 80)

        task_prompt = """Today is {today}. Create a plot showing stock gain YTD for NVDA and TLSA. Make sure the code is in markdown code block and save the figure to a file ytd_stock_gains.png. """
        # Execute via the assigned agent: code_writer_agent
        result = await code_writer_agent.run(task=task_prompt)

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