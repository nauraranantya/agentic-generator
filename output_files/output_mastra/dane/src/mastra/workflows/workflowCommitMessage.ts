/**
 * Workflow: commit-message workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow to generate and optionally commit a sensible git commit message for staged changes.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// ── Workflow Steps ──

const stepGetDiff = createStep({
  id: 'getDiff',
  description: `Compute git diff of staged changes. Runs \`git diff --staged\` in provided repoPath.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Compute git diff of staged changes. Runs \`git diff --staged\` in provided repoPath.
    // TODO: Implement step logic
    throw new Error('getDiff not implemented yet')
  },
})

const stepReadConventionalCommitSpec = createStep({
  id: 'readConventionalCommitSpec',
  description: `Reads local JSON file data/crawl/conventional-commit.json using fsTool to obtain optional guidelines.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Reads local JSON file data/crawl/conventional-commit.json using fsTool to obtain optional guidelines.
    // TODO: Implement step logic
    throw new Error('readConventionalCommitSpec not implemented yet')
  },
})

const stepGenerateMessage = createStep({
  id: 'generateMessage',
  description: `Uses dane-commit-message agent to generate commit message given diff and guidelines. Expects structured output with commitMessage, generated boolean, guidelines array.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Uses dane-commit-message agent to generate commit message given diff and guidelines. Expects structured output with commitMessage, generated boolean, guidelines array.
    // TODO: Implement step logic
    throw new Error('generateMessage not implemented yet')
  },
})

const stepConfirmation = createStep({
  id: 'confirmation',
  description: `Prompt CLI user to confirm generated commit message; uses inquirer.confirm in code. If confirm false, workflow stops.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Prompt CLI user to confirm generated commit message; uses inquirer.confirm in code. If confirm false, workflow stops.
    // TODO: Implement step logic
    throw new Error('confirmation not implemented yet')
  },
})

const stepCommit = createStep({
  id: 'commit',
  description: `If user confirms, runs \`git commit -m "<message>"\` in repoPath to create commit.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // If user confirms, runs \`git commit -m "<message>"\` in repoPath to create commit.
    // TODO: Implement step logic
    throw new Error('commit not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * commit-message workflow
 *
 * Workflow to generate and optionally commit a sensible git commit message for staged changes.
 */
export const workflowCommitMessage = createWorkflow({
  id: 'commit-message workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [stepGetDiff, stepReadConventionalCommitSpec, stepGenerateMessage, stepConfirmation, stepCommit],
})
  .then(stepGetDiff)
  .then(stepReadConventionalCommitSpec)
  .then(stepGenerateMessage)
  .then(stepConfirmation)
  .then(stepCommit)
  .commit()
