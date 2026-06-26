/**
 * Memory: Famous person generator memory
 *
 * Memory used by the Famous Person Generator agent.
- vector store adapter: LibSQLVector (connectionUrl: file:../mastra.db)
- embedder model: text-embedding-3-small
- memory options (semanticRecall.topK=10, messageRange=1, lastMessages=5)
- memory resource ID in code: 'heads-up-game'
- thread name in code: 'famous-person-generator'
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const famousPersonMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    memory.options: '{"lastMessages":5,"semanticRecall":{"topK":10,"messageRange":1},"resource":"heads-up-game","thread":"famous-person-generator"}',
  }),
})
