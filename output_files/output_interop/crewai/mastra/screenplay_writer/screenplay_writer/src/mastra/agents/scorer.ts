/**
 * Agent: scorer
 * ID: scorer
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Access and call Mistral LLM endpoint.
 *   - : Access and call Together.ai LLM endpoint.
 *   - : Access and call Anyscale LLM endpoint.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { mistralTool, togetherTool, anyscaleTool } from '../tools'

/**
 * scorer
 * 
 * Instructions:
 * You are scorer.
 */
export const scorer = new Agent({
  id: `scorer`,
  name: `scorer`,
  instructions: `You are scorer.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    mistralTool,
    togetherTool,
    anyscaleTool,
  },
})
