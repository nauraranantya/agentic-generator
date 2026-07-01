/**
 * Workflow: next_pattern_placeholder
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Placeholder used to indicate there is no explicitly chained workflow pattern in source code.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * next_pattern_placeholder
 *
 * Placeholder used to indicate there is no explicitly chained workflow pattern in source code.
 */
export const nextPatternPlaceholder = createWorkflow({
  id: 'next_pattern_placeholder',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
