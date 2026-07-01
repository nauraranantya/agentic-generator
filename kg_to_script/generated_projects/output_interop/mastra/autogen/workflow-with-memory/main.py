import asyncio

from team import (
    cat_one,
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
        # Workflow Step: task_step_one
        # Workflow Edge: task_step_one -> task_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_one")
        print("=" * 80)

        task_prompt = """Doubles the input value """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_two
        # Workflow Edge: task_step_two -> task_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_two")
        print("=" * 80)

        task_prompt = """Adds 1 to the input value """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_three
        # Workflow Edge: task_step_three -> task_step_four
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_three")
        print("=" * 80)

        task_prompt = """Squares the input value """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_four
        # Workflow Edge: task_step_four -> task_step_five
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_four")
        print("=" * 80)

        task_prompt = """Gives the square root of the input value """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_five
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_five")
        print("=" * 80)

        task_prompt = """Triples the input value """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_par_step_one
        # Workflow Edge: task_par_step_one -> task_par_step_six
        # Workflow Edge: task_par_step_one -> task_par_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_par_step_one")
        print("=" * 80)

        task_prompt = """Doubles the input value (parallel workflow start) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_par_step_six
        # Workflow Edge: task_par_step_six -> task_par_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_par_step_six")
        print("=" * 80)

        task_prompt = """Logs the input value and returns rawText """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_par_step_two
        # Workflow Edge: task_par_step_two -> task_par_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_par_step_two")
        print("=" * 80)

        task_prompt = """Adds 1 to the input value (parallel branch) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_par_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_par_step_three")
        print("=" * 80)

        task_prompt = """Squares the input value (parallel branch end) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_br_step_one
        # Workflow Edge: task_br_step_one -> task_br_step_two
        # Workflow Edge: task_br_step_one -> task_br_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_br_step_one")
        print("=" * 80)

        task_prompt = """Doubles the input value (branched workflow start) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_br_step_two
        # Workflow Edge: task_br_step_two -> task_br_step_four
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_br_step_two")
        print("=" * 80)

        task_prompt = """Adds 1 to the input value """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_br_step_four
        # Workflow Edge: task_br_step_four -> task_br_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_br_step_four")
        print("=" * 80)

        task_prompt = """Gives the square root of the input value """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_br_step_three
        # Workflow Edge: task_br_step_three -> task_br_step_five
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_br_step_three")
        print("=" * 80)

        task_prompt = """Squares the input value (parallel branch) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_br_step_five
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_br_step_five")
        print("=" * 80)

        task_prompt = """Triples the input value (branch join) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_cyc_step_one
        # Workflow Edge: task_cyc_step_one -> task_cyc_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_cyc_step_one")
        print("=" * 80)

        task_prompt = """Doubles the input value (cyclical workflow start) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_cyc_step_two
        # Workflow Edge: task_cyc_step_two -> task_cyc_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_cyc_step_two")
        print("=" * 80)

        task_prompt = """Adds 1 to the input value (cyclical workflow) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_cyc_step_three
        # Workflow Edge: task_cyc_step_three -> task_cyc_step_one_loop
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_cyc_step_three")
        print("=" * 80)

        task_prompt = """Squares the input value when condition met (doubledValue == 10) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_cyc_step_one_loop
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_cyc_step_one_loop")
        print("=" * 80)

        task_prompt = """Re-invocation of stepOne under condition (doubledValue == 12) """
        # Execute via the assigned agent: cat_one
        result = await cat_one.run(task=task_prompt)

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