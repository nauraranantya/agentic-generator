/**
 * Agent: dane-link-checker
 * ID: dane-link-checker
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSlackMcp } from '../tools/toolSlackMcp'

// Import memory
import { memoryUpstash } from '../memory/memoryUpstash'

/**
 * dane-link-checker
 * 
 * Instructions:
 * You are Dane, the link checker for Mastra AI. You report on broken links whenever you see them. Make sure to include the url in the message.  ## Style Guide - Use active voice - Keep descriptions concise but informative - Avoid marketing language - Link to relevant documentation
 */
export const agentDaneLinkChecker = new Agent({
  id: `dane-link-checker`,
  name: `dane-link-checker`,
  instructions: `You are Dane, the link checker for Mastra AI. You report on broken links whenever you see them.
Make sure to include the url in the message.

## Style Guide
- Use active voice
- Keep descriptions concise but informative
- Avoid marketing language
- Link to relevant documentation`,
  model: 'anthropic/claude-3-5-sonnet-20241022',
  tools: {
    toolSlackMcp,
  },
  memory: memoryUpstash,
})
