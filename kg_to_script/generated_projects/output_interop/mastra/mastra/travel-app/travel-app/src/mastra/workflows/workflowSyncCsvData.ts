/**
 * Workflow: workflow_sync_csv_data
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { travelAnalyzer } from '../agents'

// ── Workflow Steps ──

const taskSyncCsvData = createStep({
  id: 'task_sync_csv_data',
  description: `Sync data from City CSV (src/data/city-data.csv). Read CSV rows, map columns to CityData, and call mastra.engine.syncRecords to sync City records. This step is executed by the Mastra engine runtime.`,
  inputSchema: z.object({}),
  outputSchema: z.object({status: z.string()}),
  execute: async ({ inputData }) => {
    // Sync data from City CSV (src/data/city-data.csv). Read CSV rows, map columns to CityData, and call mastra.engine.syncRecords to sync City records. This step is executed by the Mastra engine runtime.
    // This step uses agent: travelAnalyzer
    // const result = await travelAnalyzer.generate('...')
    // TODO: Implement step logic
    throw new Error('task_sync_csv_data not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * workflow_sync_csv_data
 */
export const workflowSyncCsvData = createWorkflow({
  id: 'workflow_sync_csv_data',
  inputSchema: z.object({}),
  outputSchema: z.object({status: z.string()}),
  steps: [taskSyncCsvData],
})
  .then(taskSyncCsvData)
  .commit()
