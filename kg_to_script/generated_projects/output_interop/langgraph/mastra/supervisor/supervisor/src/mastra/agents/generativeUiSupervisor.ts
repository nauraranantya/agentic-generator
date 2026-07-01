/**
 * Agent: supervisor
 * ID: generative-ui-supervisor
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Handle user query: 
 *   - Route selection: 
 * Capabilities:
 *   - fetch ticker price: Fetch the price of a stock ticker.
 *   - trade ticker: Purchase or sell a ticker (trade operation).
 *   - get portfolio: Retrieve the user's portfolio.
 *   - suggest restaurants: Suggest restaurants for a given location.
 *   - suggest accommodations: Suggest places to stay for a trip.
 *   - write React TODO app: Generate a React TODO application when requested.
 *   - order pizza: Order a pizza on behalf of the user.
 *   - write document: Produce a text document for the user.
 *   - route selection: Analyze conversation and select appropriate tool route.
 *   - general assistant: Generic assistant capabilities to answer queries, summarize tool results, and follow up.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolStockbroker, toolTripPlanner, toolOpenCode, toolOrderPizza, toolWriterAgent, toolRouter, toolGeneralInput } from '../tools'

/**
 * supervisor
 * 
 * Instructions:
 * You are supervisor.
 */
export const generativeUiSupervisor = new Agent({
  id: `generative-ui-supervisor`,
  name: `supervisor`,
  instructions: `You are supervisor.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolStockbroker,
    toolTripPlanner,
    toolOpenCode,
    toolOrderPizza,
    toolWriterAgent,
    toolRouter,
    toolGeneralInput,
  },
})
