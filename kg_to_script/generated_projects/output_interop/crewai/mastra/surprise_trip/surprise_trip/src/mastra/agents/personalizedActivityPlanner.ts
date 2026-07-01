/**
 * Agent: Activity Planner
 * ID: personalized_activity_planner
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
 * Activity Planner
 * 
 * Instructions:
 * You are Activity Planner.
 */
export const personalizedActivityPlanner = new Agent({
  id: `personalized_activity_planner`,
  name: `Activity Planner`,
  instructions: `You are Activity Planner.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperDevTool,
    toolScrapeWebsiteTool,
  },
})
