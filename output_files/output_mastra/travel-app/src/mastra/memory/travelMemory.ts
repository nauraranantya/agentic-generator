/**
 * Memory: TravelAgent Memory
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const travelMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
})
