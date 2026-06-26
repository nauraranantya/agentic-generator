/**
 * Agent: LLM Agent
 * ID: travel-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Assemble trip components: 
 * Capabilities:
 *   - Find Flights: Capability to search and select flight options.
 *   - Find Hotels: Capability to search and select hotels.
 *   - Find Attractions: Capability to search and select attractions.
 *   - Search Airbnb: Capability to search airbnb locations and listings.
 *   - Analyze Travel Results: Capability to analyze raw agent search outputs and reformat into application schema.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { searchFlightsTool, searchHotelsTool, searchAttractionsTool, searchAirbnbLocationTool, searchAirbnbTool } from '../tools'

// Import memory
import { travelMemory } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * Agent-level instruction used on agent initialization
 */
export const travelAgent = new Agent({
  id: `travel-agent`,
  name: `LLM Agent`,
  instructions: `Agent-level instruction used on agent initialization`,
  model: 'openai/gpt-4.1',
  tools: {
    searchFlightsTool,
    searchHotelsTool,
    searchAttractionsTool,
    searchAirbnbLocationTool,
    searchAirbnbTool,
  },
  memory: travelMemory,
})
