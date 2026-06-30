/**
 * Agent: scorer
 * ID: scorer
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
 * scorer
 * 
 * Instructions:
 * role: scorer; goal: Score dialogue 1-10; backstory: scoring expert
 */
export const scorer = new Agent({
  id: `scorer`,
  name: `scorer`,
  instructions: `role: scorer; goal: Score dialogue 1-10; backstory: scoring expert`,
  model: 'openai/gpt-4o-mini',
})
