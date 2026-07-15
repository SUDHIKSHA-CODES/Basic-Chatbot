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