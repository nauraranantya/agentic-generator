/**
 * Agent: formatter
 * ID: formatter
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Spam detection / vulgar content detection: 
 *   - Discussion analysis and summarization: 
 *   - Create dialogue-heavy screenplay from discussion: 
 *   - Text formatting, removing actions/parentheticals: 
 *   - Score a dialogue on a 1-10 scale: 
 */

import { Agent } from '@mastra/core/agent'

/**
 * formatter
 * 
 * Instructions:
 * role: formatter; goal: Format text and remove bracketed actions; backstory: expert text formatter.
 */
export const formatter = new Agent({
  id: `formatter`,
  name: `formatter`,
  instructions: `role: formatter; goal: Format text and remove bracketed actions; backstory: expert text formatter.`,
  model: 'openai/gpt-4o-mini',
})
