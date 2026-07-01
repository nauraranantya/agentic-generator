/**
 * Agent: Lead Market Analyst
 * ID: lead_market_analyst
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
 * Lead Market Analyst
 * 
 * Instructions:
 * Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.
 */
export const leadMarketAnalyst = new Agent({
  id: `lead_market_analyst`,
  name: `Lead Market Analyst`,
  instructions: `Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperDevTool,
    toolScrapeWebsiteTool,
  },
})
