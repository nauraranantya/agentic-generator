/**
 * Memory: memoryKb
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
    lastMessages: 4,
    semanticRecall.topK: 1,
    semanticRecall.messageRange: 0,
    workingMemory.enabled: 'true',
  }),
})
