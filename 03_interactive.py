import requests
import json
import time

# Set up the base URL for the local Ollama API
# Typically defaults to localhost:11434, but can be changed in the Ollama config
url = "http://localhost:11434/api/chat"

greetingMessage = "Hello! I'm your assistant. How can I help you today? \nType 'bye', 'goodbye', 'thank you', 'exit' or 'quit' to end the conversation."

conversationHistory = []
print(greetingMessage)

# Initializing the conversation
while True:
    userQuery = input("\nYou: ")
    if userQuery.lower() in ["exit", "quit", "bye", "goodbye", "thank you"]:
        print("Goodbye, have a nice day!")
        break

    # Add user message to history
    conversationHistory.append({"role": "user", "content": userQuery})

    payload = {
        "model": "phi3:latest",
        "messages": conversationHistory
    }

    response = requests.post(url, json=payload, stream=True)

    if response.status_code == 200:
        print("Assistant: ", end="", flush=True)
        assistant_reply = ""
        for line in response.iter_lines(decode_unicode=True):
            if line:
                data = json.loads(line)
                chunk = data["message"]["content"]
                print(chunk, end="", flush=True)
                assistant_reply += chunk
                time.sleep(0.05)
        print()
        # Add assistant message to history
        conversationHistory.append({"role": "assistant", "content": assistant_reply})
    else:
        print(f"Error: {response.status_code}")