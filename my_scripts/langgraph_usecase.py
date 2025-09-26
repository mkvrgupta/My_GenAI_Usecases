import torch
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

# 1. Define the state
class State(TypedDict):
    question: str
    answer: str

# 2. Load a local Hugging Face model
# distilgpt2 is small, runs fine on CPU
generator = pipeline(
    "text-generation",
    model="google/flan-t5-small",
    device=0 if torch.cuda.is_available() else -1,  # GPU if available
    max_new_tokens=100
)
llm = HuggingFacePipeline(pipeline=generator)

# 3. Define LangGraph nodes
def ask_llm(state: State):
    response = llm.invoke(state["question"])
    return {"answer": response}

def decide_next(state: State):
    return END

# 4. Build the graph
graph = StateGraph(State)
graph.add_node("ask_llm", ask_llm)
graph.set_entry_point("ask_llm")
graph.add_conditional_edges("ask_llm", decide_next)

# 5. Compile
app = graph.compile()

# 6. Run it
result = app.invoke({"question": "What is LangGraph?"})
print(result)
