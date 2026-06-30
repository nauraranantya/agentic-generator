/**
 * Agent: Activity Planner
 * ID: personalized_activity_planner
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
 * Activity Planner
 * 
 * Instructions:
 * Use internet search tools and recommendation engines to gather information; produce day-by-day activities with name, location, description and suitability rationale.
 */
export const personalizedActivityPlanner = new Agent({
  id: `personalized_activity_planner`,
  name: `Activity Planner`,
  instructions: `Use internet search tools and recommendation engines to gather information; produce day-by-day activities with name, location, description and suitability rationale.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    serperDevTool,
    scrapeWebsiteTool,
  },
})
