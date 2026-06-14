/**
 * Mastra AI Instance - MastraAgentSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { agentDane } from './agents/agentDane'
import { agentDaneCommitMessage } from './agents/agentDaneCommitMessage'
import { agentDaneIssueLabeler } from './agents/agentDaneIssueLabeler'
import { agentDaneLinkChecker } from './agents/agentDaneLinkChecker'
import { agentDanePackagePublisher } from './agents/agentDanePackagePublisher'
import { agentDaneNewContributor } from './agents/agentDaneNewContributor'

// Import workflows
import { workflowCommitMessage } from './workflows/workflowCommitMessage'
import { workflowTelephoneGame } from './workflows/workflowTelephoneGame'
import { workflowLinkChecker } from './workflows/workflowLinkChecker'
import { workflowChangelog } from './workflows/workflowChangelog'
import { workflowPackagePublisher } from './workflows/workflowPackagePublisher'
import { workflowMessage } from './workflows/workflowMessage'
import { workflowGithubIssueLabeler } from './workflows/workflowGithubIssueLabeler'
import { workflowGithubFirstContributor } from './workflows/workflowGithubFirstContributor'

// Import memory instances
import { memoryUpstash } from './memory/memoryUpstash'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Collection of agents and tools composing the CLI assistant 'Dane' and associated workflows.
 */
export const mastra = new Mastra({
  agents: {
    agentDane,
    agentDaneCommitMessage,
    agentDaneIssueLabeler,
    agentDaneLinkChecker,
    agentDanePackagePublisher,
    agentDaneNewContributor,
  },
  workflows: {
    workflowCommitMessage,
    workflowTelephoneGame,
    workflowLinkChecker,
    workflowChangelog,
    workflowPackagePublisher,
    workflowMessage,
    workflowGithubIssueLabeler,
    workflowGithubFirstContributor,
  },
  memory: {
    memoryUpstash,
  },
})
