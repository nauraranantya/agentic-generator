/**
 * Agent: assistant / trip-planner
 * ID: trip-planner-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : 
 *   - : 
 *   - : 
 *   - : 
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolExtract, toolClassify, toolListAccommodations, toolListRestaurants } from '../tools'

/**
 * assistant / trip-planner
 * 
 * Instructions:
 * You are assistant / trip-planner.
 */
export const tripPlannerAgent = new Agent({
  id: `trip-planner-agent`,
  name: `assistant / trip-planner`,
  instructions: `You are assistant / trip-planner.`,
  model: 'openai/gpt-4o',
  tools: {
    toolExtract,
    toolClassify,
    toolListAccommodations,
    toolListRestaurants,
  },
})
