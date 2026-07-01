/**
 * Agent: The Best Financial Analyst
 * ID: financial_agent
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
import { toolCalculatorTool, toolScrapeWebsiteTool, toolWebsiteSearchTool, toolSec10KToolAmzn, toolSec10QToolAmzn } from '../tools'

/**
 * The Best Financial Analyst
 * 
 * Instructions:
 * You are The Best Financial Analyst.
 */
export const financialAgent = new Agent({
  id: `financial_agent`,
  name: `The Best Financial Analyst`,
  instructions: `You are The Best Financial Analyst.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolCalculatorTool,
    toolScrapeWebsiteTool,
    toolWebsiteSearchTool,
    toolSec10KToolAmzn,
    toolSec10QToolAmzn,
  },
})
