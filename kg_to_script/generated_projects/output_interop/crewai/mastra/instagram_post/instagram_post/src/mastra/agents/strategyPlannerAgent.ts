/**
 * Agent: Chief Marketing Strategist
 * ID: strategy_planner_agent
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
 * Chief Marketing Strategist
 * 
 * Instructions:
 * Formulate marketing strategies and creative ideas based on product and competitor analysis.
 */
export const strategyPlannerAgent = new Agent({
  id: `strategy_planner_agent`,
  name: `Chief Marketing Strategist`,
  instructions: `Formulate marketing strategies and creative ideas based on product and competitor analysis.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolScrapeWebsite,
    toolSearchInternet,
    toolSearchInstagram,
  },
})
