/**
 * Agent: dane-issue-labeler
 * ID: dane-issue-labeler
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { memoryUpstash } from '../memory/memoryUpstash'

/**
 * dane-issue-labeler
 * 
 * Instructions:
 * You are Dane, the ultimate GitHub operator. You help engineers label their issues.
 */
export const agentDaneIssueLabeler = new Agent({
  id: `dane-issue-labeler`,
  name: `dane-issue-labeler`,
  instructions: `You are Dane, the ultimate GitHub operator.
You help engineers label their issues.`,
  model: 'anthropic/claude-3-5-sonnet-20241022',
  memory: memoryUpstash,
})
