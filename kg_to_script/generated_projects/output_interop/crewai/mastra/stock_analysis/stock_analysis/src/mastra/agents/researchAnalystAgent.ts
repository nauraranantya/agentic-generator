/**
 * Agent: Staff Research Analyst
 * ID: research_analyst_agent
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
import { toolScrapeWebsiteTool, toolSec10KToolAmzn, toolSec10QToolAmzn } from '../tools'

/**
 * Staff Research Analyst
 * 
 * Instructions:
 * You are Staff Research Analyst.
 */
export const researchAnalystAgent = new Agent({
  id: `research_analyst_agent`,
  name: `Staff Research Analyst`,
  instructions: `You are Staff Research Analyst.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolScrapeWebsiteTool,
    toolSec10KToolAmzn,
    toolSec10QToolAmzn,
  },
})
