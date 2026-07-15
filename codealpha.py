print("Welcome to Basic Chatbot!")
print("Welcome to Basic Chatbot!")

user_input = input("You: ")

print("You entered:", user_input)
print("Welcome to Basic Chatbot!")

user_input = input("You: ").lower()

if user_input == "hello":
    print("Bot: Hi!")

elif user_input == "how are you":
    print("Bot: I'm fine, thanks!")

elif user_input == "bye":
    print("Bot: Goodbye!")

else:
    print("Bot: I don't understand.")
    def chatbot(message):

    if message == "hello":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "I'm a Basic Python Chatbot."

    elif message == "help":
        return "You can say hello, how are you, or bye."

    elif message == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


print("===================================")
print("      BASIC PYTHON CHATBOT")
print("Type 'bye' to exit.")
print("===================================")

while True:

    user_input = input("You: ").lower()

    response = chatbot(user_input)

    print("Bot:", response)

    if user_input == "bye":
        break