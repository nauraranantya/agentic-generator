/**
 * Memory: sharedMemoryStore
 *
 * A Memory instance configured with a PostgresStore for storage and a PgVector vector store for embeddings.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: pg
 */

import { Memory } from '@mastra/memory'
import { PostgresStore } from '@mastra/pg'


export const sharedMemoryStore = new Memory({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  storage: new PostgresStore({
    id: 'mastra-pg-store',
    host: 'localhost',
    port: 5432,
    user: 'postgres',
    database: 'postgres',
    password: 'postgres',
    "memory.vector.connectionString": 'postgresql://postgres:postgres@localhost:5432',
    "memory.options.lastMessages": 10,
    "memory.options.semanticRecall.topK": 3,
    "memory.options.semanticRecall.messageRange": 2,
  }) as any,
  embedder: text-embedding-3-small,
})
