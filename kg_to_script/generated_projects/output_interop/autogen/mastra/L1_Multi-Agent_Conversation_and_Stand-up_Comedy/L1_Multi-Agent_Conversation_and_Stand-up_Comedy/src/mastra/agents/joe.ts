/**
 * Agent: stand-up comedian
 * ID: joe
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * stand-up comedian
 * 
 * Instructions:
 * System message as provided at ConversableAgent creation in the notebook.
 */
export const joe = new Agent({
  id: `joe`,
  name: `stand-up comedian`,
  instructions: `System message as provided at ConversableAgent creation in the notebook.`,
  model: 'openai/gpt-4o-mini',
})
