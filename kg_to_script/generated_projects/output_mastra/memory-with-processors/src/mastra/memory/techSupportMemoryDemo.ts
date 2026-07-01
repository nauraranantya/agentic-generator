/**
 * Memory: techSupportMemoryDemo
 *
 * Memory configured with TokenLimiter(500) and semanticRecall=true for support demo.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const techSupportMemoryDemo = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    options: 'lastMessages=50; semanticRecall=true',
  }),
  options: {
    processors: [
      // TokenLimiter — trims large tool responses to stay within token budget
      // TODO: import { TokenLimiter } from '@mastra/memory' and enable:
      // new TokenLimiter(500),
    ],
  },
})
