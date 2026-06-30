/**
 * Agent: The Best Financial Analyst
 * ID: financial_analyst_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - web scraping: Capability to fetch and extract textual content from web pages.
 *   - website search: Capability to search web content and return links or content snippets (site-level search).
 *   - mathematical calculation: Numeric computation capability (safe evaluation of arithmetic expressions).
 *   - SEC 10-K semantic search: Semantic search over the latest 10-K filing content for a specified company ticker.
 *   - SEC 10-Q semantic search: Semantic search over the latest 10-Q filing content for a specified company ticker.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolCalculator, toolScrapeWebsite, toolWebsiteSearch, sec10KToolGeneric, sec10QToolGeneric } from '../tools'

/**
 * The Best Financial Analyst
 * 
 * Instructions:
 * This prompt is produced from the second factory for financial_analyst_agent in the code (duplicate configuration).
 */
export const financialAnalystAgent = new Agent({
  id: `financial_analyst_agent`,
  name: `The Best Financial Analyst`,
  instructions: `This prompt is produced from the second factory for financial_analyst_agent in the code (duplicate configuration).`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolCalculator,
    toolScrapeWebsite,
    toolWebsiteSearch,
    sec10KToolGeneric,
    sec10QToolGeneric,
  },
})
