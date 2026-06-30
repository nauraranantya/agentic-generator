/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Select the best city based on weather patterns, seasonal events, and travel costs
 *   - : Provide in-depth local guide content, hidden gems, and practical tips.
 *   - : Create a 7-day travel itinerary with detailed daily plans, budgets, packing suggestions, and logistics.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { citySelectionAgent, localExpertAgent, travelConciergeAgent } from './agents'

// Import workflows
import { tripPlanningPattern } from './workflows'

// Import memory instances
import { tripMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * A crew composed of multiple LLM agents and tools to plan trips: city selection, local expertise gathering, and travel concierge planning.
 */
export const mastra = new Mastra({
  agents: {
    citySelectionAgent,
    localExpertAgent,
    travelConciergeAgent,
  },
  workflows: {
    tripPlanningPattern,
  },
  memory: {
    tripMemory,
  },
})
