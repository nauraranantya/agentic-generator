/**
 * Agent: Staff Research Analyst
 * ID: research_analyst_agent
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
import { toolScrapeWebsite, sec10KToolAmzn, sec10QToolAmzn } from '../tools'

/**
 * Staff Research Analyst
 * 
 * Instructions:
 * System prompt for the research analyst agent.
 */
export const researchAnalystAgent = new Agent({
  id: `research_analyst_agent`,
  name: `Staff Research Analyst`,
  instructions: `System prompt for the research analyst agent.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolScrapeWebsite,
    sec10KToolAmzn,
    sec10QToolAmzn,
  },
})
