/**
 * Agent: assistant
 * ID: trip-planner-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Creates and confirms accommodation bookings (receives accommodation and trip details, returns booking confirmation and details).
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { bookAccommodationTool } from '../tools'

/**
 * assistant
 * 
 * Instructions:
 * Used by the trip planner LLM to format messages and construct tool calls for bookings.
 */
export const tripPlannerAgent = new Agent({
  id: `trip-planner-agent`,
  name: `assistant`,
  instructions: `Used by the trip planner LLM to format messages and construct tool calls for bookings.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    bookAccommodationTool,
  },
})
