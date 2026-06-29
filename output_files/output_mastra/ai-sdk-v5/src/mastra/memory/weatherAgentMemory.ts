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
    id: 'ai-sdk-v5-storage',
    url: 'file:./mastra.db',
  }),
  options: {
    lastMessages: 5,
    semanticRecall: false,
  },
})
