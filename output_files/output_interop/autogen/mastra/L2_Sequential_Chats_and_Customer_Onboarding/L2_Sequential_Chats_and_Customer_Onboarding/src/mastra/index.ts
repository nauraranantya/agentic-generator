/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Human Agents:
 *   - customer_proxy_agent (customer_proxy)
 */

import { Mastra } from '@mastra/core'

// Import agents
import { onboardingPersonalInformationAgent, onboardingTopicPreferenceAgent, customerEngagementAgent } from './agents'

// Import workflows
import { customerOnboardingWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    onboardingPersonalInformationAgent,
    onboardingTopicPreferenceAgent,
    customerEngagementAgent,
  },
  workflows: {
    customerOnboardingWorkflow,
  },
})
