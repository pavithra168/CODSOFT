# Simple Rule-Based Chatbot
# Developed by Pavithra Praveen as part of CodSoft AI Internship


def chatbot():
    print("Chatbot: Hello! I'm your AI assistant. How can I help you?")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input=input("You: ").lower().strip()

        if user_input=='exit':
            print("Chatbot: Goodbye! Have a great day :)")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How are you doing today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just code, but I'm functioning perfectly!")
        elif "your name" in user_input:
            print("Chatbot: I'm a rule-based chatbot created as part of an AI internship at CodSoft.")
        elif "what can you do" in user_input:
            print("Chatbot: I can chat with you and help you understand basic AI chatbot concepts.")
        elif "bye" in user_input:
            print("Chatbot: Bye! Talk to you soon.")
            break
        elif "who created you" in user_input:
            print("Chatbot: I was developed by a learner during their AI internship with CodSoft.")
        elif "thank" in user_input:
            print("Chatbot: You're welcome!")
        else:
            print("Chatbot: I'm not sure how to respond to that. Could you try something else?")

# Start the chatbot
chatbot()
