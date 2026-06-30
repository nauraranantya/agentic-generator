/**
 * Mastra AI Instance - ExpandIdeaCrewteam
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Understand and expand the idea into a comprehensive idea report, detailing value proposition and features.
 *   - : Provide WHY, HOW, WHAT messaging and core message for the idea.
 *   - : Select a Tailwind template that fits the idea and copy it into the working folder; then update components.
 *   - : Produce content for components, update components, and QA them according to rules.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { seniorIdeaAnalyst, seniorStrategist, seniorReactEngineer, seniorContentEditor } from './agents'

// Import workflows
import { expandIdeaWorkflowPattern, chooseTemplateWorkflowPattern, createContentWorkflowPattern, landingPageWorkflowPattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Derived from src/landing_page_generator/crew.py ExpandIdeaCrew class. Process: sequential (expand_idea -> refine_idea).
 */
export const mastra = new Mastra({
  agents: {
    seniorIdeaAnalyst,
    seniorStrategist,
    seniorReactEngineer,
    seniorContentEditor,
  },
  workflows: {
    expandIdeaWorkflowPattern,
    chooseTemplateWorkflowPattern,
    createContentWorkflowPattern,
    landingPageWorkflowPattern,
  },
})
