import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: plan-activities
export const plan_activities = createStep({
  id: 'plan_activities',
  description: `Suggests activities based on weather conditions. Input: forecast array (or forecast object). The step constructs a prompt 'Based on the following weather forecast for {location}, suggest appropriate activities: {JSON}' and streams agent response. Produces an activities text resource.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
