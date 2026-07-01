/**
 * Memory: Shared Memory (Mastra Memory)
 *
 * Memory instance used by both agents. Configured with lastMessages and semanticRecall options. Shared across agents in the implementation.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const mastraMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
  options: {
    lastMessages: 100,
    semanticRecall: {
      topK: 2,
      messageRange: 2,
    },
  },
})
