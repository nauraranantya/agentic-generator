/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Human Agents:
 *   - user_human ()
 */

import { Mastra } from '@mastra/core'

// Import agents
import { emailAssistantAgent } from './agents'

// Import workflows
import { emailAssistantWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    emailAssistantAgent,
  },
  workflows: {
    emailAssistantWorkflow,
  },
})
