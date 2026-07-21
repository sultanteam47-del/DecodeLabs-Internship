# ---------------------------------------
# Project 1: Rule-Based AI Chatbot
# Developed by: Abdullah
# Internship: DecodeLabs AI Internship
# Language: Python
# ---------------------------------------

from datetime import datetime

print("=" * 50)
print("🤖 Welcome to AI Chatbot")
print("Type 'bye' anytime to exit.")
print("=" * 50)

while True:

    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")

    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")

    elif user == "hey":
        print("Bot: Hey! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "who made you":
        print("Bot: I was created by Ali.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "help":
        print("Bot: You can ask me about AI, date, time, greetings, or type 'bye' to exit.")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a great day!")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams!")

    elif user == "thanks":
        print("Bot: You're welcome!")

    elif user == "thank you":
        print("Bot: My pleasure!")

    elif user == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif user == "time":
        print("Bot:", datetime.now().strftime("%I:%M %p"))

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry! I don't understand. Please try another question.")