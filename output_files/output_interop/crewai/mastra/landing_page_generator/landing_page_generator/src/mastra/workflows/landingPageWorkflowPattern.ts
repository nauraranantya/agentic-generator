/**
 * Workflow: Landing page overall workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Top-level sequence: ExpandIdea -> ChooseTemplate -> CreateContent. ExpandIdeaWorkflowPattern is the first sub-pattern; nextPattern points to the subsequent pattern.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import nested sub-workflows
import { expandIdeaWorkflowPattern } from './expandIdeaWorkflowPattern'
import { chooseTemplateWorkflowPattern } from './chooseTemplateWorkflowPattern'
import { createContentWorkflowPattern } from './createContentWorkflowPattern'


// ── Workflow Definition ──

/**
 * Landing page overall workflow
 *
 * Top-level sequence: ExpandIdea -> ChooseTemplate -> CreateContent. ExpandIdeaWorkflowPattern is the first sub-pattern; nextPattern points to the subsequent pattern.
 */
export const landingPageWorkflowPattern = createWorkflow({
  id: 'Landing page overall workflow',
  inputSchema: z.object({Top_level_sequence: z.string()}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
