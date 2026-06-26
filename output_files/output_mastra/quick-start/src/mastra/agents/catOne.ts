/**
 * Agent: feline expert
 * ID: cat-one
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Ability to answer questions about cat species, their behavior, biology and taxonomy.
 */

import { Agent } from '@mastra/core/agent'

/**
 * feline expert
 * 
 * Instructions:
 * Default agent-level instructions to guide behavior when the agent is asked about cat species. This prompt is intended to be used by the agent as its core persona/instructions.
 */
export const catOne = new Agent({
  id: `cat-one`,
  name: `feline expert`,
  instructions: `Default agent-level instructions to guide behavior when the agent is asked about cat species. This prompt is intended to be used by the agent as its core persona/instructions.`,
  model: 'openai/gpt-4o',
})
