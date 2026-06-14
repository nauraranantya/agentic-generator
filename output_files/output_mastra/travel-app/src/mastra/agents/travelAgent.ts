/**
 * Agent: travel-agent
 * ID: travel-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { searchFlightsTool } from '../tools/searchFlightsTool'
import { searchHotelsTool } from '../tools/searchHotelsTool'
import { searchAttractionsTool } from '../tools/searchAttractionsTool'
import { searchAirbnbLocationTool } from '../tools/searchAirbnbLocationTool'
import { searchAirbnbTool } from '../tools/searchAirbnbTool'

// Import memory
import { travelMemory } from '../memory/travelMemory'

/**
 * travel-agent
 * 
 * Instructions:
 * You are an expert travel agent responsible for finding a flight, hotel, and three attractions for a user. You will be given a set of user preferences along with some tools and you will need to find the best options for them. Be as concise as possible with your response.
 */
export const travelAgent = new Agent({
  id: `travel-agent`,
  name: `travel-agent`,
  instructions: `You are an expert travel agent responsible for finding a flight, hotel, and three attractions for a user. You will be given a set of user preferences along with some tools and you will need to find the best options for them. Be as concise as possible with your response.`,
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
