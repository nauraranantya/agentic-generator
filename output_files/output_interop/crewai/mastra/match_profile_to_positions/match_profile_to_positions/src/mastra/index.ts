/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Top-level goal: identify and rank job opportunities for a given CV.
 * Objectives:
 *   - : Objective for producing a structured summary of the given CV.
 *   - : Objective for producing a ranked list of job matches for the candidate.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { cvReader, matcher } from './agents'

// Import workflows
import { matchToProposalWorkflowPattern, nextPatternPlaceholder } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * A Crew that coordinates reading CVs and matching them to job opportunities. Constructed with two agents (cv_reader, matcher) and two tasks run sequentially.
 */
export const mastra = new Mastra({
  agents: {
    cvReader,
    matcher,
  },
  workflows: {
    matchToProposalWorkflowPattern,
    nextPatternPlaceholder,
  },
})
