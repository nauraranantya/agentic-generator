/**
 * Memory: tokenTestMemory
 *
 * Memory with TokenLimiter to demonstrate pruning of large tool responses.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const tokenTestMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: process.env.DATABASE_URL ?? 'file:local.db',
  }),
  options: {
    lastMessages: 50,
    processors: [
      // TokenLimiter — trims large tool responses to stay within token budget
      // TODO: import { TokenLimiter } from '@mastra/memory' and enable:
      // new TokenLimiter(1000),
    ],
  },
})
