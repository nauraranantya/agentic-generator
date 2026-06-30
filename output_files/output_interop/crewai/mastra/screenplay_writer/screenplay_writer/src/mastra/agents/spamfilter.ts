/**
 * Agent: spamfilter
 * ID: spamfilter
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
 * spamfilter
 * 
 * Instructions:
 * role: spamfilter; goal: Decide whether a text is spam or not.; backstory: You are an expert spam filter with years of experience. You DETEST advertisements, newsletters and vulgar language.
 */
export const spamfilter = new Agent({
  id: `spamfilter`,
  name: `spamfilter`,
  instructions: `role: spamfilter; goal: Decide whether a text is spam or not.; backstory: You are an expert spam filter with years of experience. You DETEST advertisements, newsletters and vulgar language.`,
  model: 'openai/gpt-4o-mini',
})
