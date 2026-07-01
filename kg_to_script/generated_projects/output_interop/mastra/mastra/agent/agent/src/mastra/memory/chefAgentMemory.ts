/**
 * Memory: Chef Agent Memory (per-agent)
 *
 * Memory instance used by Chef agents. Options: workingMemory enabled.
    Purpose: store per-agent conversation state and short-term context.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const chefAgentMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
})
