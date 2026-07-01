/**
 * Memory: Global Memory (Mastra Memory instance)
 *
 * Memory instance with workingMemory enabled in some agent configurations.
    Source semantics:
      - workingMemory.enabled: true (for some agents)
      - used as an agent knowledge base to store short-term context and conversation history.
    Implementation details omitted; configuration preserved here.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const globalMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
})
