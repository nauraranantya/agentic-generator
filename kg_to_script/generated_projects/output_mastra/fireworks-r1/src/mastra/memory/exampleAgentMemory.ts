/**
 * Memory: exampleAgentMemory
 *
 * Memory instance created by new Memory() and assigned to the agent. Used to store short-term or session state. Implementation details omitted; represented as a KnowledgeBase/Memory individual.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const exampleAgentMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
})
