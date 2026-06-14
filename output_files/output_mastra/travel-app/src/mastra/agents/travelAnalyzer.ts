/**
 * Agent: travel-analyzer
 * ID: travel-analyzer
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { travelMemory } from '../memory/travelMemory'

/**
 * travel-analyzer
 * 
 * Instructions:
 * You are an expert travel agent responsible for finding a flight, hotel, and three attractions for a user. You will be given a set of user preferences along with some data to find the best options for them.
 */
export const travelAnalyzer = new Agent({
  id: `travel-analyzer`,
  name: `travel-analyzer`,
  instructions: `You are an expert travel agent responsible for finding a flight, hotel, and three attractions for a user. You will be given a set of user preferences along with some data to find the best options for them.`,
  model: 'openai/gpt-4.1',
  memory: travelMemory,
})
