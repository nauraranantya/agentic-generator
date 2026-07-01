/**
 * Memory: cryptoAgentMemory
 *
 * Memory object backed by a PostgresStore (connection string referenced via process.env.POSTGRES_URL). See mastra/agents/index.ts.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: pg
 */

import { Memory } from '@mastra/memory'
import { PostgresStore } from '@mastra/pg'


export const cryptoAgentMemory = new Memory({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  storage: new PostgresStore({
    id: 'mastra-pg-store',
    connectionString: process.env.POSTGRES_URL,
    "memory.options.semanticRecall": 'false',
  }) as any,
})
