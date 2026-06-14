/**
 * Agent: My Agent
 * ID: my-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * My Agent
 * 
 * Instructions:
 * My Agent Instructions
 */
export const myAgent = new Agent({
  id: `my-agent`,
  name: `My Agent`,
  instructions: `My Agent Instructions`,
  model: 'openai/gpt-4o',
})
