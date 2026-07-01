/**
 * Agent: Chief Marketing Strategist
 * ID: chief_marketing_strategist
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Perform web search queries and return relevant search results.
 *   - : Retrieve and parse website content for analysis.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSerperDevTool, toolScrapeWebsiteTool } from '../tools'

/**
 * Chief Marketing Strategist
 * 
 * Instructions:
 * Synthesize amazing insights from product analysis to formulate incredible marketing strategies.
 */
export const chiefMarketingStrategist = new Agent({
  id: `chief_marketing_strategist`,
  name: `Chief Marketing Strategist`,
  instructions: `Synthesize amazing insights from product analysis to formulate incredible marketing strategies.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperDevTool,
    toolScrapeWebsiteTool,
  },
})
