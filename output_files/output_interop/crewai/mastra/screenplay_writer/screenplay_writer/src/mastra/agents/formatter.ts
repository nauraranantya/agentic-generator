/**
 * Agent: formatter
 * ID: formatter
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
 * formatter
 * 
 * Instructions:
 * You are formatter.
 */
export const formatter = new Agent({
  id: `formatter`,
  name: `formatter`,
  instructions: `You are formatter.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    mistralTool,
    togetherTool,
    anyscaleTool,
  },
})
