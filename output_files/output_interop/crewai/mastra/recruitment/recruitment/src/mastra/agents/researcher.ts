/**
 * Agent: Job Candidate Researcher
 * ID: researcher
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Find and report best candidates for a job opening: Coordinate research, matching/scoring, outreach strategy, and reporting to produce a ranked and actionable list of candidates for a given job requirement input.
 * Capabilities:
 *   - candidate_research: Search public data sources and extract candidate basic profile information.
 *   - candidate_matching_and_scoring: Evaluate candidates against job requirements and produce a numeric or ordinal score and justification.
 *   - outreach_strategy_development: Design outreach approaches and generate template messages for contacting candidates.
 *   - candidate_reporting: Compose recruiter-facing reports summarizing findings, scores and outreach strategies.
 *   - search_api: 
 *   - web_scraping: 
 *   - retrieve_linkedin_profiles: 
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSerperdev, toolScrapewebsite, toolLinkedin } from '../tools'

/**
 * Job Candidate Researcher
 * 
 * Instructions:
 * Agent-level base instruction for researcher.
 */
export const researcher = new Agent({
  id: `researcher`,
  name: `Job Candidate Researcher`,
  instructions: `Agent-level base instruction for researcher.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperdev,
    toolScrapewebsite,
    toolLinkedin,
  },
})
