/**
 * Agent: spamfilter
 * ID: spamfilter
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
 * spamfilter
 * 
 * Instructions:
 * You are spamfilter.
 */
export const spamfilter = new Agent({
  id: `spamfilter`,
  name: `spamfilter`,
  instructions: `You are spamfilter.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    mistralTool,
    togetherTool,
    anyscaleTool,
  },
})
