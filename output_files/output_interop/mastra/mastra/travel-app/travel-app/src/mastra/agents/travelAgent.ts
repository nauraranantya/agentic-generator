/**
 * Agent: travel agent
 * ID: travelAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : 
 *   - : 
 *   - : 
 *   - : 
 *   - : 
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSearchFlights, toolSearchHotels, toolSearchAttractions, toolSearchAirbnbLocation, toolSearchAirbnb } from '../tools'

/**
 * travel agent
 * 
 * Instructions:
 * You are travel agent.
 */
export const travelAgent = new Agent({
  id: `travelAgent`,
  name: `travel agent`,
  instructions: `You are travel agent.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSearchFlights,
    toolSearchHotels,
    toolSearchAttractions,
    toolSearchAirbnbLocation,
    toolSearchAirbnb,
  },
})
