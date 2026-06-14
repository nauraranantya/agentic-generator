/**
 * Memory: Upstash Memory Store (example_token @ localhost:8079)
 *
 * Memory instance using UpstashStore at http://localhost:8079 with token 'example_token'. Used by many agents for persistent memory.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: upstash
 */

import { Memory } from '@mastra/memory'
import { UpstashStore } from '@mastra/upstash'


export const memoryUpstash = new Memory({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  storage: new UpstashStore({
    id: 'mastra-upstash-store',
    url: process.env.UPSTASH_REDIS_REST_URL!,
    token: process.env.UPSTASH_REDIS_REST_TOKEN!,
  }) as any,
})
