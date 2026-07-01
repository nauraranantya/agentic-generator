/**
 * Agent: router
 * ID: router
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
import { toolRouter } from '../tools'

/**
 * router
 * 
 * Instructions:
 * You are router.
 */
export const router = new Agent({
  id: `router`,
  name: `router`,
  instructions: `You are router.`,
  model: 'google/gemini-2.0-flash',
  tools: {
    toolRouter,
  },
})
