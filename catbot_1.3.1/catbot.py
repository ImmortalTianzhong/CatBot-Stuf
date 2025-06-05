import json
from difflib import get_close_matches

# Load the JSON file
with open("expanded_catbot_conversations.json", "r") as f:
    data = json.load(f)

# Build a prompt-response dictionary
conversation_dict = {}
for convo in data["conversations"]:
    prompt = convo["user"].strip().lower()
    response = convo["catbot"]
    conversation_dict[prompt] = response

print("Welcome to CatBot! Type something to begin. Type 'exit' to quit.\n")

# Chatbot loop with fuzzy matching
while True:
    user_input = input("You: ").strip().lower()
    if user_input in ["exit", "quit"]:
        print("CatBot: A message from CatBot: Goodbye! Come back soon.")
        break

    # Exact match or fuzzy match
    response = conversation_dict.get(user_input)
    if not response:
        matches = get_close_matches(user_input, conversation_dict.keys(), n=1, cutoff=0.6)
        if matches:
            response = conversation_dict[matches[0]]

    if response:
        print(f"CatBot: {response}")
    else:
        print("CatBot: A message from CatBot: I'm not sure how to respond to that yet!")
