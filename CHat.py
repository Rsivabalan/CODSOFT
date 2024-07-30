def chatbot():
    print("Hello! I'm a simple rule-based chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I assist you?")
        elif user_input in ["how are you?", "how are you doing?"]:
            print("Chatbot: I'm just a bot, but I'm here to help you!")
        elif user_input in ["what's your name?", "who are you?"]:
            print("Chatbot: I'm a simple rule-based chatbot.")
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
