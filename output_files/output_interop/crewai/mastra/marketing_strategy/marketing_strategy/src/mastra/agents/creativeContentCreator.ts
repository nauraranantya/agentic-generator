/**
 * Agent: Creative Content Creator
 * ID: creative_content_creator
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Produce campaign ideas: Objective: generate creative campaign ideas for the marketing project.
 * Capabilities:
 *   - web search capability: Capability to perform web searches and retrieve online information (used by SerperDevTool).
 *   - web scraping capability: Capability to scrape website content and extract structured information.
 *   - analyze market: Capability to research and analyze markets, competitors, and customers.
 *   - formulate strategy: Capability to synthesize analysis into strategic plans and marketing strategies.
 *   - create content: Capability to produce creative campaign ideas and marketing copy.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Creative Content Creator
 * 
 * Instructions:
 * Role and backstory for agent
 */
export const creativeContentCreator = new Agent({
  id: `creative_content_creator`,
  name: `Creative Content Creator`,
  instructions: `Role and backstory for agent`,
  model: 'openai/gpt-4o-mini',
})
