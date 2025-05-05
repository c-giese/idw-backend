import requests
import json
import time


# Set up the base URL for the local Ollama API
# Typically defaults to localhost:11434, but can be changed in the Ollama config
url = "http://localhost:11434/api/chat"

# Define the payload (your input prompt)
payload = {
    "model": "phi3:latest",  # Replace with the model name you're using
    "messages": [{"role": "user", "content": "What is an llm?"}]
}


# Send the HTTP POST request with streaming enabled
response = requests.post(url, json=payload, stream=True)


if response.status_code == 200:
    # Print each chunk as it arrives, simulating typing
    for line in response.iter_lines(decode_unicode=True):
        if line:
            data = json.loads(line)
            chunk = data["message"]["content"]
            print(chunk, end="", flush=True)
            time.sleep(0.05)  # Can be used to have a consistent typing speed
    print()  # Newline after completion
else:
    print(f"Error: {response.status_code}")
    
