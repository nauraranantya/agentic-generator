import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";


const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

async function capitalize(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\nNode: capitalize",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}


const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("capitalize", capitalize)
  .addEdge("capitalizeSentence", "capitalize")
  .addEdge("capitalize", "formatMessages")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
