# Using Ollama - llama3.2 as model to chat
"""
This is an example of a chatbot provided with a prompt template that makes the chatbot respond in a specific character style.
In this case, like Mario from the Super Mario.

The user input is processed through a prompt template that sets the system's role and the user's input for every interaction.
This is also a naive implementation only using the LLM without any short-term memory.
"""

from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

def mario_prompt(input_text: str):

    template = ChatPromptTemplate([
        ("system", "You are a mean assistant that talks like Mario. And your name is also Mario, keeping every interaction in character."),
        ("human", "{user_input_text}")
    ])
    return template.invoke({"user_input_text": input_text})


if __name__ == "__main__":

    print("Initializing chatbot...")

    model = OllamaLLM(model="llama3.2")

    print("Using Ollama - llama3.2 as model to chat")
    print("Type 'exit' to quit the chatbot.")


    while True:
        user_input_text = input("You: ")
        bot_output_text = model.invoke(mario_prompt(user_input_text))
        if user_input_text.lower() == "exit":
            print("Exiting chatbot.")
            break

        print(f"Chatbot: {bot_output_text}")
        