/**
 * Memory: Mastra Memory (KnowledgeBase instance)
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: mongodb
 */

import { Memory } from '@mastra/memory'
import { MongoDBStore } from '@mastra/mongodb'


export const mastraMemory = new Memory({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  storage: new MongoDBStore({
    id: 'mastra-mongodb-store',
    url: process.env.MONGODB_URI,
    dbName: process.env.MONGODB_DB_NAME || 'mastra_memory',
    uri: process.env.MONGODB_URI,
  }) as any,
  embedder: openai.embedding('text-embedding-3-small'),
  options: {
    lastMessages: 10,
    semanticRecall: {
      topK: 3,
      messageRange: 2,
    },
  },
})
