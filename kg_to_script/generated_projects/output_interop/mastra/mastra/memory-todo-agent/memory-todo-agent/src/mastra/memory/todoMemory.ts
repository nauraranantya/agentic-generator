/**
 * Memory: todoMemory
 *
 * Memory configuration used by the TODO Agent. Options extracted from source:
- lastMessages: 1
- semanticRecall: false
- workingMemory.enabled: true
- workingMemory.template: (see separate Config entry)
The agent depends on a single previous message and MUST store working memory in every response to remain consistent with the original implementation and instruction set.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const todoMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
})
