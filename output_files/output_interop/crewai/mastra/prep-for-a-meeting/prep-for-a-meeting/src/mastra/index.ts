/**
 * Mastra AI Instance - MeetingPreparationCrew
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Prepare meeting briefing and strategy: Prepare comprehensive research, industry analysis, strategic talking points, and a concise briefing document to support an upcoming meeting. This goal represents the overall purpose of the Meeting Preparation Crew created in main.py.
 *   - : Conduct thorough research on people and companies involved in the meeting
 *   - : Analyze the current industry trends, challenges, and opportunities relevant to the meeting context
 *   - : Develop talking points, questions, and strategic angles for the meeting
 *   - : Compile research, analysis, and strategy into a concise briefing document
 */

import { Mastra } from '@mastra/core'

// Import agents
import { researcherAgent1, industryAnalystAgent1, meetingStrategyAgent1, briefingCoordinatorAgent1 } from './agents'

// Import workflows
import { meetingPreparationPattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    researcherAgent1,
    industryAnalystAgent1,
    meetingStrategyAgent1,
    briefingCoordinatorAgent1,
  },
  workflows: {
    meetingPreparationPattern,
  },
})
