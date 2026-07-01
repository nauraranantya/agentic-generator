/**
 * Workflow: a2_a_example_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Two-step pattern: (1) research by a first agent; (2) transformation of research into content by a second agent. Matches the sequential steps in src/index.ts demonstrating A2A interactions.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { myAgent, contentCreatorAgent } from '../agents'

// ── Workflow Steps ──

const researchTask = createStep({
  id: 'research_task',
  description: `Task where the first agent gathers information. In code: researchTaskId = \`research-\${Date.now()}\` and a message with the researchQuery is sent via a2aClient.sendMessage. The task returns a message/status object and the resulting textual research output is stored in the ResearchResult resource.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Provide a brief summary of agent networks in AI
    // This step uses agent: myAgent
    // const result = await myAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('research_task not implemented yet')
  },
})

const contentTask = createStep({
  id: 'content_task',
  description: `Task where the content-creator agent receives research output and transforms it into an engaging blog post introduction. In the code the prompt is constructed by embedding researchResult into a template and sending via secondA2aClient.sendMessage.`,
  inputSchema: z.object({researchResult: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Transform this research into an engaging blog post introduction:
    // This step uses agent: contentCreatorAgent
    // const result = await contentCreatorAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('content_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * a2_a_example_pattern
 *
 * Two-step pattern: (1) research by a first agent; (2) transformation of research into content by a second agent. Matches the sequential steps in src/index.ts demonstrating A2A interactions.
 */
export const a2AExamplePattern = createWorkflow({
  id: 'a2_a_example_pattern',
  inputSchema: z.object({Two: z.string()}),
  outputSchema: z.object({}),
  steps: [researchTask, contentTask],
})
  .then(researchTask)
  .then(contentTask)
  .commit()
