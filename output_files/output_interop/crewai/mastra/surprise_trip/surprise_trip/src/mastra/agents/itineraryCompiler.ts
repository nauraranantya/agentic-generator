/**
 * Agent: Itinerary Compiler
 * ID: itinerary_compiler
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Produce a per-day list of recommended activities and events including details and suitability rationale.
 *   - : Produce recommended restaurants and scenic locations with ratings and descriptions for each relevant day.
 *   - : Produce a single integrated itinerary document that schedules flights, hotel, day plans, activities and restaurants.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { serperDevTool } from '../tools'

/**
 * Itinerary Compiler
 * 
 * Instructions:
 * Compile all researched information into a comprehensive day-by-day itinerary for the trip; ensure integration of flights, hotel information, activities, and restaurants. Use text formatting and document creation tools.
 */
export const itineraryCompiler = new Agent({
  id: `itinerary_compiler`,
  name: `Itinerary Compiler`,
  instructions: `Compile all researched information into a comprehensive day-by-day itinerary for the trip; ensure integration of flights, hotel information, activities, and restaurants. Use text formatting and document creation tools.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    serperDevTool,
  },
})
