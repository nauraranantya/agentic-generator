/**
 * Agent: Senior Photographer
 * ID: senior_photographer_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Extract and summarize HTML content from websites.
 *   - : Query web search API and return ranked result snippets.
 *   - : Search Instagram content via web search for post examples and snippets.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolScrapeWebsite, toolSearchInternet, toolSearchInstagram } from '../tools'

/**
 * Senior Photographer
 * 
 * Instructions:
 * Generate three photographic concepts that best represent the campaign and product without showing the actual product.
 */
export const seniorPhotographerAgent = new Agent({
  id: `senior_photographer_agent`,
  name: `Senior Photographer`,
  instructions: `Generate three photographic concepts that best represent the campaign and product without showing the actual product.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolScrapeWebsite,
    toolSearchInternet,
    toolSearchInstagram,
  },
})
