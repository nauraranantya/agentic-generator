/**
 * Agent: Itinerary Compiler
 * ID: itinerary_compiler
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
import { toolSerperDevTool } from '../tools'

/**
 * Itinerary Compiler
 * 
 * Instructions:
 * You are Itinerary Compiler.
 */
export const itineraryCompiler = new Agent({
  id: `itinerary_compiler`,
  name: `Itinerary Compiler`,
  instructions: `You are Itinerary Compiler.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperDevTool,
  },
})
