/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Goal to illustrate that TokenLimiter ensures conversation memory stays within token limits while preserving recent context.
 *   - : Goal to show custom memory processors can filter or redact content based on keywords or types (e.g., tool calls).
 *   - : Goal to validate that the support agent can use tools, recall recent context, and that TokenLimiter prunes older content when exceeding token limits.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { tokenTestAgent, technicalSupport, technicalSupportRepo, forgetfulJobInterviewer, forgetfulJobInterviewerRepo } from './agents'

// Import memory instances
import { tokenTestMemory, techSupportMemoryDemo, supportAgentMemoryRepo, interviewMemoryRepo, forgetfulDemoMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Logical orchestration/system instance that groups and manages the agent instances defined in the project.
 */
export const mastra = new Mastra({
  agents: {
    tokenTestAgent,
    technicalSupport,
    technicalSupportRepo,
    forgetfulJobInterviewer,
    forgetfulJobInterviewerRepo,
  },
  memory: {
    tokenTestMemory,
    techSupportMemoryDemo,
    supportAgentMemoryRepo,
    interviewMemoryRepo,
    forgetfulDemoMemory,
  },
})
