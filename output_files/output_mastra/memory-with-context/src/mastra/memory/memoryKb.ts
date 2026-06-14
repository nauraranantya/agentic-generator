/**
 * Memory: Memory component (Memory instance for Memory Agent)
 *
 * Memory configured with lastMessages, semanticRecall and workingMemory options as in source code.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const memoryKb = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
  options: {
    lastMessages: 4,
    semanticRecall: {
      topK: 1,
      messageRange: 0,
    },
    workingMemory: {
      enabled: true,
    },
  },
})
