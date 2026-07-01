/**
 * Agent: dane-commit-message
 * ID: dane-commit-message
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolFsTool } from '../tools/toolFsTool'

// Import memory
import { memoryUpstash } from '../memory/memoryUpstash'

/**
 * dane-commit-message
 * 
 * Instructions:
 * You are Dane, the ultimate GitHub operator. You help engineers generate commit messages.  GENERATE A SCOPE FOR THE COMMIT MESSAGE IF NECESSARY. FIGURE OUT THE BEST TOP LEVEL SEMANTIC MATCH TO USE AS THE SCOPE.
 */
export const agentDaneCommitMessage = new Agent({
  id: `dane-commit-message`,
  name: `dane-commit-message`,
  instructions: `You are Dane, the ultimate GitHub operator.
You help engineers generate commit messages.

GENERATE A SCOPE FOR THE COMMIT MESSAGE IF NECESSARY.
FIGURE OUT THE BEST TOP LEVEL SEMANTIC MATCH TO USE AS THE SCOPE.`,
  model: 'anthropic/claude-3-5-sonnet-20241022',
  tools: {
    toolFsTool,
  },
  memory: memoryUpstash,
})
