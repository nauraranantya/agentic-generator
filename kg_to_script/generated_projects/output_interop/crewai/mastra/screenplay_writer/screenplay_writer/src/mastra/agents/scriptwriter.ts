/**
 * Agent: scriptwriter
 * ID: scriptwriter
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
 * scriptwriter
 * 
 * Instructions:
 * You are scriptwriter.
 */
export const scriptwriter = new Agent({
  id: `scriptwriter`,
  name: `scriptwriter`,
  instructions: `You are scriptwriter.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    mistralTool,
    togetherTool,
    anyscaleTool,
  },
})
