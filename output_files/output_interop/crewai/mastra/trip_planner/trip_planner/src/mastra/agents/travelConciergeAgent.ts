/**
 * Agent: Amazing Travel Concierge
 * ID: travel_concierge_agent
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
import { toolSearch, toolBrowser, toolCalculator } from '../tools'

/**
 * Amazing Travel Concierge
 * 
 * Instructions:
 * Create the most amazing travel itineraries with budget and packing suggestions for the city
 */
export const travelConciergeAgent = new Agent({
  id: `travel_concierge_agent`,
  name: `Amazing Travel Concierge`,
  instructions: `Create the most amazing travel itineraries with budget and packing suggestions for the city`,
  model: 'openai/gpt-4',
  tools: {
    toolSearch,
    toolBrowser,
    toolCalculator,
  },
})
