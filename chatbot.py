def chatbot():
    print("🤖 Chatbot: Hey! I'm ChatBro.")
    print("You can ask me things like:")
    print("  ⭐ hello / hi / hey")
    print("  ⭐ how are you")
    print("  ⭐ what's your name")
    print("  ⭐ bye (to end chat)")

    user_name = None  # Variable to store the user's name
    while True:
        user_input = input("You: ").lower() 
        if user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hey there! 👋")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! ")

        elif "your name" in user_input:
            
            print("🤖 Chatbot: I'm ChatBro.")
            
            if not user_name:
                user_name = input("🤖 Chatbot: What's your name? ").capitalize()
                print(f"🤖 Chatbot: Nice to meet you, {user_name}!")

        elif user_input == "bye":
            # If user's name was given earlier, say goodbye using their name
            if user_name:
                print(f"🤖 Chatbot: Bye {user_name}, take care! 👋")
            else:
                # If name not given, say a normal goodbye
                print("🤖 Chatbot: Bye! Talk to you later! 👋")
            break  # Exit the chat loop

        else:
            # Handle unknown inputs
            print("🤖 Chatbot: Hmm, I didn’t get that.")

chatbot()


