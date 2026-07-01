/**
 * Agent: Restaurant Scout
 * ID: restaurant_scout
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Performs web searches for information such as events, activities, and restaurant listings.
 *   - : Extracts structured information from web pages (addresses, ratings, descriptions).
 *   - : Research and recommend activities suitable to traveler preferences.
 *   - : Find and recommend restaurants and scenic dining locations.
 *   - : Compile research into a day-by-day itinerary document.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSerperDevTool, toolScrapeWebsiteTool } from '../tools'

/**
 * Restaurant Scout
 * 
 * Instructions:
 * You are Restaurant Scout.
 */
export const restaurantScout = new Agent({
  id: `restaurant_scout`,
  name: `Restaurant Scout`,
  instructions: `You are Restaurant Scout.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperDevTool,
    toolScrapeWebsiteTool,
  },
})
