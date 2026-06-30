/**
 * Mastra AI Instance - Mastraagentsystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { dane, daneCommitMessage, daneIssueLabeler, daneLinkChecker, danePackagePublisher, daneNewContributor } from './agents'

// Import workflows
import { workflowCommitMessage, workflowTelephoneGame, workflowLinkChecker, workflowChangelog, workflowPackagePublisher, workflowMessage, workflowGithubIssueLabeler, workflowGithubFirstContributor } from './workflows'

// Import memory instances
import { memoryUpstash } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Collection of agents and tools composing the CLI assistant 'Dane' and associated workflows.
 */
export const mastra = new Mastra({
  agents: {
    dane,
    daneCommitMessage,
    daneIssueLabeler,
    daneLinkChecker,
    danePackagePublisher,
    daneNewContributor,
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
