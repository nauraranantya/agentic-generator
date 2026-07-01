/**
 * Memory: Shared conversation memory
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: pg
 */

import { Memory } from '@mastra/memory'
import { PostgresStore } from '@mastra/pg'


export const sharedConversationMemory = new Memory({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  storage: new PostgresStore({
    id: 'mastra-pg-store',
    adapter: 'UpstashStore',
    "memory.vector.connectionString": 'postgresql://postgres:postgres@localhost:5433',
    "memory.options.default": '{ lastMessages: 1, semanticRecall: { topK: 3, messageRange: 2 } }',
  }) as any,
})
