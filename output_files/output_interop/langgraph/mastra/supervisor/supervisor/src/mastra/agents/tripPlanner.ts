/**
 * Agent: trip_planner_tool_agent
 * ID: tripPlanner
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Fetch price, buy/sell tickers, retrieve user portfolio.
 *   - : Suggest restaurants, hotels, and itineraries for locations.
 *   - : Generate project code (React TODO app) and related files.
 *   - : Place pizza orders and return confirmation details.
 *   - : Generate long-form text documents or writing deliverables.
 *   - : Select the appropriate target route/tool based on user input.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolTripPlanner } from '../tools'

/**
 * trip_planner_tool_agent
 * 
 * Instructions:
 * You are trip_planner_tool_agent.
 */
export const tripPlanner = new Agent({
  id: `tripPlanner`,
  name: `trip_planner_tool_agent`,
  instructions: `You are trip_planner_tool_agent.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolTripPlanner,
  },
})
