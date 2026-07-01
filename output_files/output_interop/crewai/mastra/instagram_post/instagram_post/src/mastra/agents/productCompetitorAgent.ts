/**
 * Agent: Lead Market Analyst
 * ID: product_competitor_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Extract and summarize HTML content from websites.
 *   - : Query web search API and return ranked result snippets.
 *   - : Search Instagram content via web search for post examples and snippets.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolScrapeWebsite, toolSearchInternet } from '../tools'

/**
 * Lead Market Analyst
 * 
 * Instructions:
 * Produce thorough product and competitor analysis to inform marketing strategy.
 */
export const productCompetitorAgent = new Agent({
  id: `product_competitor_agent`,
  name: `Lead Market Analyst`,
  instructions: `Produce thorough product and competitor analysis to inform marketing strategy.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolScrapeWebsite,
    toolSearchInternet,
  },
})
