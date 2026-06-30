/**
 * Memory: Open Code Memory
 *
 * Holds the planning state used by the planner/executor loop. Key structured items used at runtime:
- PLAN (ordered array of plan steps for building the todo app).
- last plan tool call args (executedPlans, rejectedPlans, remainingPlans).
This individual stores the canonical PLAN and describes how executed/rejected/remaining lists evolve.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const openCodeMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
})
