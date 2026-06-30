/**
 * Agent: Restaurant Scout
 * ID: restaurant_scout
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Produce a per-day list of recommended activities and events including details and suitability rationale.
 *   - : Produce recommended restaurants and scenic locations with ratings and descriptions for each relevant day.
 *   - : Produce a single integrated itinerary document that schedules flights, hotel, day plans, activities and restaurants.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { serperDevTool, scrapeWebsiteTool } from '../tools'

/**
 * Restaurant Scout
 * 
 * Instructions:
 * Use internet search tools, restaurant review sites, and travel guides to find restaurants and scenic locations aligned with traveler preferences.
 */
export const restaurantScout = new Agent({
  id: `restaurant_scout`,
  name: `Restaurant Scout`,
  instructions: `Use internet search tools, restaurant review sites, and travel guides to find restaurants and scenic locations aligned with traveler preferences.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    serperDevTool,
    scrapeWebsiteTool,
  },
})
