/**
 * Memory: Upstash Memory Store (example_token @ localhost:8079)
 *
 * Memory instance using UpstashStore at http://localhost:8079 with token 'example_token'. Used by many agents for persistent memory.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const memoryUpstash = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
})
