/**
 * Agent: analyse
 * ID: analyst
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
 * analyse
 * 
 * Instructions:
 * role: analyse; goal: Distill arguments and identify who said what; backstory: Expert discussion analyst.
 */
export const analyst = new Agent({
  id: `analyst`,
  name: `analyse`,
  instructions: `role: analyse; goal: Distill arguments and identify who said what; backstory: Expert discussion analyst.`,
  model: 'openai/gpt-4o-mini',
})
