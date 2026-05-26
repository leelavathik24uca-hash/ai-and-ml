# Simple AI Chatbot

def simple_chatbot():
    print("Hello! I am a simple AI. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        user_input = user_input.lower()  # make it case-insensitive

        if user_input == "exit":
            print("AI: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("AI: Hello there!")
        elif "how are you" in user_input:
            print("AI: I'm just a program, but I'm doing fine!")
        elif "your name" in user_input:
            print("AI: I am a simple AI chatbot.")
        else:
            print("AI: Sorry, I don't understand that.")

# Run the chatbot
simple_chatbot()