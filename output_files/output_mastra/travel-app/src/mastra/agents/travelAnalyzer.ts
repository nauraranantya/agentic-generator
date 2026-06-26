/**
 * Agent: LLM Agent
 * ID: travel-analyzer
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

// Import memory
import { travelMemory } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * Analyzer agent base instructions.
 */
export const travelAnalyzer = new Agent({
  id: `travel-analyzer`,
  name: `LLM Agent`,
  instructions: `Analyzer agent base instructions.`,
  model: 'openai/gpt-4.1',
  memory: travelMemory,
})
