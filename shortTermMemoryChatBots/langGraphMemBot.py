# Using Ollama - llama3.2 as model to chat
"""
This is an example of a chatbot using LangGraph with short-term memory.

It uses the ChatOllama model from LangChain to process user inputs and generate responses.
The regular model invocation does not wrap the AImessages properly resulting in a HumanMessage Loop

This chatbot maintains a conversation state using LangGraph's StateGraph and MessagesState.
It allows for a more interactive and context-aware conversation by keeping track of the messages exchanged.
The messages are passed to the model each time and are stored in the state of the graph.
"""

from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage


print("Initializing chatbot...")

model = ChatOllama(model="llama3.2")

print("Using Ollama - llama3.2 as model to chat")
print("Type 'exit' to quit the chatbot.")

workflow = StateGraph(
    state_schema=MessagesState
)

def call_model(state: MessagesState) -> MessagesState:

    response = model.invoke(state["messages"])
    return {"messages": response}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "testing"}}

while True:
    user_input_text = input("You: ")

    bot_output_state = app.invoke({"messages": HumanMessage(user_input_text)}, config=config)
    if user_input_text.lower() == "exit":
        print("Exiting chatbot.")
        break

    print(f"Chatbot: {bot_output_state["messages"][-1].content}")

print(bot_output_state)
