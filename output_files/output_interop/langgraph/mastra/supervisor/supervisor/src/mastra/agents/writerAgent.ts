/**
 * Agent: writer_agent_tool
 * ID: writerAgent
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
import { toolWriterAgent } from '../tools'

/**
 * writer_agent_tool
 * 
 * Instructions:
 * You are writer_agent_tool.
 */
export const writerAgent = new Agent({
  id: `writerAgent`,
  name: `writer_agent_tool`,
  instructions: `You are writer_agent_tool.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolWriterAgent,
  },
})
