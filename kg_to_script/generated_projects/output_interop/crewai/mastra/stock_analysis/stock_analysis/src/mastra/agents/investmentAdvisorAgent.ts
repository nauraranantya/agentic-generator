/**
 * Agent: Private Investment Advisor
 * ID: investment_advisor_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Performs arithmetic and mathematical calculations.
 *   - : Scrapes and summarizes web page content.
 *   - : Performs web searches and retrieves relevant results.
 *   - : Searches textual sources or indexes.
 *   - : Semantic search within a company's 10-K filing content.
 *   - : Semantic search within a company's 10-Q filing content.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolCalculatorTool, toolScrapeWebsiteTool, toolWebsiteSearchTool } from '../tools'

/**
 * Private Investment Advisor
 * 
 * Instructions:
 * You are Private Investment Advisor.
 */
export const investmentAdvisorAgent = new Agent({
  id: `investment_advisor_agent`,
  name: `Private Investment Advisor`,
  instructions: `You are Private Investment Advisor.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolCalculatorTool,
    toolScrapeWebsiteTool,
    toolWebsiteSearchTool,
  },
})
