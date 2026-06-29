import { ChatAnthropic } from "@langchain/anthropic";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";


const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});



const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addEdge("stepFindStore", "stepOrderPizza")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
