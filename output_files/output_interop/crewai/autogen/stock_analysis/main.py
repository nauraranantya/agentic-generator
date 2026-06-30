import asyncio

from team import (
    financial_agent,
    financial_analyst_agent,
    research_analyst_agent,
    investment_advisor_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "company_stock":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: research
        # Workflow Edge: research -> filings_analysis
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: research")
        print("=" * 80)

        task_prompt = """Collect and summarize recent news articles, press releases, and market analyses related to the {company_stock} stock and its industry. Pay special attention to any significant events, market sentiments, and analysts' opinions. Also include upcoming events like earnings and others."""
        # Execute via the assigned agent: research_analyst_agent
        result = await research_analyst_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: filings_analysis
        # Workflow Edge: filings_analysis -> financial_analysis
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: filings_analysis")
        print("=" * 80)

        task_prompt = """Analyze the latest 10-Q and 10-K filings from EDGAR for the stock {company_stock} in question. Focus on key sections like Management's Discussion and analysis, financial statements, insider trading activity, and any disclosed risks. Extract relevant data and insights that could influence the stock's future performance."""
        # Execute via the assigned agent: financial_analyst_agent
        result = await financial_analyst_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: financial_analysis
        # Workflow Edge: financial_analysis -> recommend
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: financial_analysis")
        print("=" * 80)

        task_prompt = """Conduct a thorough analysis of {company_stock}'s stock financial health and market performance. This includes examining key financial metrics such as P/E ratio, EPS growth, revenue trends, and debt-to-equity ratio. Also, analyze the stock's performance in comparison to its industry peers and overall market trends."""
        # Execute via the assigned agent: financial_analyst_agent
        result = await financial_analyst_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: recommend
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: recommend")
        print("=" * 80)

        task_prompt = """Review and synthesize the analyses provided by the Financial Analyst and the Research Analyst. Combine these insights to form a comprehensive investment recommendation. MUST consider financial health, market sentiment, and qualitative data from EDGAR filings. Include insider trading activity and upcoming events like earnings."""
        # Execute via the assigned agent: investment_advisor_agent
        result = await investment_advisor_agent.run(task=task_prompt)

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