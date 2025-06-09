# Using Ollama - llama3.2 as model to chat
"""
This is a simple chatbot implementation using the LangChain library.

One thing to note about this chatbot is that it does not have shot-term memory.
It simply takes the user input and invokes the model to get a response.

For exampled, given a name, it will not remember the name in the next interaction.
It is a naive implementation to demonstrate how to use the Ollama LLM with LangChain.
"""

from langchain_ollama import OllamaLLM

def testing_message(message: str):
    return f"testing message: {message}"

if __name__ == "__main__":

    print("Initializing chatbot...")

    model = OllamaLLM(model="llama3.2")

    print("Using Ollama - llama3.2 as model to chat")
    print("Type 'exit' to quit the chatbot.")


    while True:
        user_input_text = input("You: ")
        bot_output_text = model.invoke(user_input_text)
        if user_input_text.lower() == "exit":
            print("Exiting chatbot.")
            break

        print(f"Chatbot: {bot_output_text}")
        