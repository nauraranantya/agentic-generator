/**
 * Agent: scriptwriter
 * ID: scriptwriter
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
 * scriptwriter
 * 
 * Instructions:
 * role: scriptwriter; goal: Produce dialogue-only screenplay; backstory: hates directional notes
 */
export const scriptwriter = new Agent({
  id: `scriptwriter`,
  name: `scriptwriter`,
  instructions: `role: scriptwriter; goal: Produce dialogue-only screenplay; backstory: hates directional notes`,
  model: 'openai/gpt-4o-mini',
})
