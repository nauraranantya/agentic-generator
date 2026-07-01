/**
 * Agent: Local Expert at this city
 * ID: local_expert_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Search the internet for relevant results using Serper API.
 *   - : Scrape and summarize website content using browserless and HTML partitioning.
 *   - : Perform safe mathematical calculations.
 *   - : Analyze travel data to select an optimal city based on weather, season, and prices.
 *   - : Provide deep local insights, attractions, cultural context, and practical tips.
 *   - : Create detailed itineraries, budgets, packing suggestions, and logistics.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSearch, toolBrowser } from '../tools'

/**
 * Local Expert at this city
 * 
 * Instructions:
 * Provide the BEST insights about the selected city
 */
export const localExpertAgent = new Agent({
  id: `local_expert_agent`,
  name: `Local Expert at this city`,
  instructions: `Provide the BEST insights about the selected city`,
  model: 'openai/gpt-4',
  tools: {
    toolSearch,
    toolBrowser,
  },
})
