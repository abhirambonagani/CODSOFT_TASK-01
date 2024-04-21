def chatbot(input_text):
    # Convert input text to lowercase for easier matching
    input_text = input_text.lower()
    # Define predefined rules and responses
    rules = {
        "hi": "Hello! How can I assist you today?",
        "how are you": "I'm just a bot, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome!",
        "default": "I'm sorry, I didn't understand that."
    }

    # Check if input matches any predefined rules
    for key in rules:
        if key in input_text:
            return rules[key]

    # If no match found, return default response
    return rules["default"]


# Simple loop to interact with the chatbot
while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print("Bot:", response)
    if user_input.lower() == "bye":
        break