/**
 * Memory: weatherMemory
 *
 * Memory instance created for the weather agent. Configured with lastMessages=10, semanticRecall=false, threads.generateTitle=false. Uses a LibSQLStore storage (file:../mastra.db) as defined in agent setup.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const weatherMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    lastMessages: 10,
    semanticRecall: 'false',
    threads.generateTitle: 'false',
    storage.url: 'file:../mastra.db',
  }),
})
