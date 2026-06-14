/**
 * Workflow: candidate-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow triggered by a single trigger value 'resumeText'.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { recruiterAgent } from '../agents/recruiterAgent'

// ── Workflow Steps ──

const wsGatherCandidateInfo = createStep({
  id: 'gatherCandidateInfo step',
  description: `Initial workflow step that extracts candidate information from the trigger resumeText.`,
  inputSchema: z.object({ resumeText: z.string() }),
  outputSchema: z.object({ candidateName: z.string(), isTechnical: z.boolean(), specialty: z.string(), resumeText: z.string() }),
  execute: async ({ inputData, suspend }) => {
    // Suspend/resume step
    // This step uses agent: recruiterAgent
    // You are given this resume text:
    // TODO: Check resume state and implement logic
    await suspend({
      message: 'Waiting for human input',
    })
    throw new Error('gatherCandidateInfo step resume handler not implemented yet')
  },
})

const wsAskAboutSpecialty = createStep({
  id: 'askAboutSpecialty step',
  description: `Conditional step executed when gatherCandidateInfo.isTechnical == true. Condition encoded here because ontology lacks a dedicated condition construct.`,
  inputSchema: z.object({}),
  outputSchema: z.object({ question: z.string() }),
  execute: async ({ inputData, suspend }) => {
    // Suspend/resume step
    // This step uses agent: recruiterAgent
    // You are a recruiter. Given the resume below, craft a short question for \${candidateName} about how they got into "\${specialty}". Resume: \${resumeText}
    // TODO: Check resume state and implement logic
    await suspend({
      message: 'Waiting for human input',
    })
    throw new Error('askAboutSpecialty step resume handler not implemented yet')
  },
})

const wsAskAboutRole = createStep({
  id: 'askAboutRole step',
  description: `Conditional step executed when gatherCandidateInfo.isTechnical == false. Condition encoded here because ontology lacks a dedicated condition construct.`,
  inputSchema: z.object({}),
  outputSchema: z.object({ question: z.string() }),
  execute: async ({ inputData, suspend }) => {
    // Suspend/resume step
    // This step uses agent: recruiterAgent
    // You are a recruiter. Given the resume below, craft a short question for \${candidateName} asking what interests them most about this role. Resume: \${resumeText}
    // TODO: Check resume state and implement logic
    await suspend({
      message: 'Waiting for human input',
    })
    throw new Error('askAboutRole step resume handler not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * candidate-workflow
 *
 * Workflow triggered by a single trigger value 'resumeText'.
 */
export const candidateWorkflow = createWorkflow({
  id: 'candidate-workflow',
  inputSchema: z.object({ resumeText: z.string() }),
  outputSchema: z.object({}),
  steps: [wsGatherCandidateInfo, wsAskAboutSpecialty, wsAskAboutRole],
})
  // NOTE: Branching workflow — simplified to sequential for type compatibility
  // TODO: Implement conditional branching using .branch() API
  .then(wsGatherCandidateInfo)
  .then(wsAskAboutSpecialty)  // condition: gatherCandidateInfo.isTechnical == true
  .then(wsAskAboutRole)  // condition: gatherCandidateInfo.isTechnical == false
  .commit()
