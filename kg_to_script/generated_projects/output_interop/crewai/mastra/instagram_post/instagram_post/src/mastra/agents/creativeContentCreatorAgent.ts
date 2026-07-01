/**
 * Agent: Creative Content Creator
 * ID: creative_content_creator_agent
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
 * Creative Content Creator
 * 
 * Instructions:
 * Produce multiple Instagram ad copy options aligned with campaign strategy.
 */
export const creativeContentCreatorAgent = new Agent({
  id: `creative_content_creator_agent`,
  name: `Creative Content Creator`,
  instructions: `Produce multiple Instagram ad copy options aligned with campaign strategy.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolScrapeWebsite,
    toolSearchInternet,
    toolSearchInstagram,
  },
})
