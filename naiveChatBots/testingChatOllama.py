
from langchain_ollama import ChatOllama

def testing_message(message: str):
    return f"testing message: {message}"

if __name__ == "__main__":

    print("Initializing chatbot...")

    model = ChatOllama(model="llama3.2")

    print("Using Ollama - llama3.2 as model to chat")
    print("Type 'exit' to quit the chatbot.")


    while True:
        user_input_text = input("You: ")
        # In the form of an AIMessage
        bot_output_text= model.invoke(user_input_text)
        if user_input_text.lower() == "exit":
            print("Exiting chatbot.")
            break

        print(f"Chatbot: {bot_output_text}")
        