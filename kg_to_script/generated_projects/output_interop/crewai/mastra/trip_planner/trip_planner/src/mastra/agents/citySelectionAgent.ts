/**
 * Agent: City Selection Expert
 * ID: city_selection_agent
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
 * City Selection Expert
 * 
 * Instructions:
 * Select the best city based on weather, season, and prices
 */
export const citySelectionAgent = new Agent({
  id: `city_selection_agent`,
  name: `City Selection Expert`,
  instructions: `Select the best city based on weather, season, and prices`,
  model: 'openai/gpt-4',
  tools: {
    toolSearch,
    toolBrowser,
  },
})
