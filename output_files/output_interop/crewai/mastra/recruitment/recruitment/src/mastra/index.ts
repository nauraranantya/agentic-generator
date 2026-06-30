/**
 * Mastra AI Instance - RecruitmentCrew
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Find potential candidates for the job: Find potential candidates for the job specified in inputs (job_requirements). Use multiple public resources to assemble candidate brief profiles and contact info.
 *   - Match the candidates to the best jobs and score them: Evaluate candidates relative to the job_requirements, compute scores and rank candidates with justifications.
 *   - Develop outreach strategies for the selected candidates: Produce outreach methods and message templates tailored to prioritized candidates.
 *   - Report the best candidates to the recruiters: Assemble a concise report for recruiters with profiles, scores, and outreach plan; follow output formatting instruction from tasks configuration.
 * Objectives:
 *   - Find and report best candidates for a job opening: Coordinate research, matching/scoring, outreach strategy, and reporting to produce a ranked and actionable list of candidates for a given job requirement input.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { researcher, matcher, communicator, reporter } from './agents'

// Import workflows
import { recruitmentWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    researcher,
    matcher,
    communicator,
    reporter,
  },
  workflows: {
    recruitmentWorkflow,
  },
})
