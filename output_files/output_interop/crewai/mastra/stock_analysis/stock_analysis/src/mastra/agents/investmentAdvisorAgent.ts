/**
 * Agent: Private Investment Advisor
 * ID: investment_advisor_agent
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
import { toolCalculator, toolScrapeWebsite, toolWebsiteSearch } from '../tools'

/**
 * Private Investment Advisor
 * 
 * Instructions:
 * System prompt for the investment advisor agent.
 */
export const investmentAdvisorAgent = new Agent({
  id: `investment_advisor_agent`,
  name: `Private Investment Advisor`,
  instructions: `System prompt for the investment advisor agent.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolCalculator,
    toolScrapeWebsite,
    toolWebsiteSearch,
  },
})
