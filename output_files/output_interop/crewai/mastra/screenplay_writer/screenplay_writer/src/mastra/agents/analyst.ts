/**
 * Agent: analyse
 * ID: analyst
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
 * analyse
 * 
 * Instructions:
 * You are analyse.
 */
export const analyst = new Agent({
  id: `analyst`,
  name: `analyse`,
  instructions: `You are analyse.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    mistralTool,
    togetherTool,
    anyscaleTool,
  },
})
