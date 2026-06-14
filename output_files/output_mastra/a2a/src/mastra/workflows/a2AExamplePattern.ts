/**
 * Workflow: A2A communication example pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Two-step pattern: (1) research by a first agent; (2) transformation of research into content by a second agent. Matches the sequential steps in src/index.ts demonstrating A2A interactions.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { myAgent } from '../agents/myAgent'
import { contentCreatorAgent } from '../agents/contentCreatorAgent'

// ── Workflow Steps ──

const a2AStep1Research = createStep({
  id: 'Research Step (Start)',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Provide a brief summary of agent networks in AI
    // This step uses agent: myAgent
    // const result = await myAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Research Step (Start) not implemented yet')
  },
})

const a2AStep2ContentTransform = createStep({
  id: 'Content Transformation Step',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Transform this research into an engaging blog post introduction:
    // This step uses agent: contentCreatorAgent
    // const result = await contentCreatorAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Content Transformation Step not implemented yet')
  },
})

const a2AStep3End = createStep({
  id: 'End Step',
  description: `Marks the completion of the two-step A2A workflow.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Marks the completion of the two-step A2A workflow.
    // TODO: Implement step logic
    throw new Error('End Step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * A2A communication example pattern
 *
 * Two-step pattern: (1) research by a first agent; (2) transformation of research into content by a second agent. Matches the sequential steps in src/index.ts demonstrating A2A interactions.
 */
export const a2AExamplePattern = createWorkflow({
  id: 'A2A communication example pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [a2AStep1Research, a2AStep2ContentTransform, a2AStep3End],
})
  .then(a2AStep1Research)
  .then(a2AStep2ContentTransform)
  .then(a2AStep3End)
  .commit()
