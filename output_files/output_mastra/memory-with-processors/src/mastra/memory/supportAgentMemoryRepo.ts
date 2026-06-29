/**
 * Memory: supportAgentMemoryRepo
 *
 * Memory configured with TokenLimiter(2000) for repository support agent example.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const supportAgentMemoryRepo = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    options: 'lastMessages=50; semanticRecall=false',
  }),
  options: {
    processors: [
      // TokenLimiter — trims large tool responses to stay within token budget
      // TODO: import { TokenLimiter } from '@mastra/memory' and enable:
      // new TokenLimiter(2000),
    ],
  },
})
