/**
 * Memory: weather-agent-memory
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const weatherAgentMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    storage.id: 'ai-sdk-v5-storage',
    storage.url: 'file:./mastra.db',
    semanticRecall: 'false',
    workingMemory.enabled: 'false',
    lastMessages: 5,
  }),
})
