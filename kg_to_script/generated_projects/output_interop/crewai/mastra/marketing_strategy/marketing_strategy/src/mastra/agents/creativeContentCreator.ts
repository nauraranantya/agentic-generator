/**
 * Agent: Creative Content Creator
 * ID: creative_content_creator
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Perform web search queries and return relevant search results.
 *   - : Retrieve and parse website content for analysis.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Creative Content Creator
 * 
 * Instructions:
 * Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact ad copies.
 */
export const creativeContentCreator = new Agent({
  id: `creative_content_creator`,
  name: `Creative Content Creator`,
  instructions: `Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact ad copies.`,
  model: 'openai/gpt-4o-mini',
})
