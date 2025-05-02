import requests
import json
import threading
import time

# Visual feedback for the user while waiting for the response
def typing_animation(stop_event):
    animation = "|/-\\"
    idx = 0
    print("Sending request to Ollama...")
    while not stop_event.is_set():
        print(f"\rWaiting for response... {animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.1)
    print("\rResponse received!")

stop_event = threading.Event()
t = threading.Thread(target=typing_animation, args=(stop_event,))
t.start()

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


# Handling the response
if response.status_code == 200:
    full_text = ""
    # Read each line as it arrives and add it to the full text
    for line in response.iter_lines(decode_unicode=True):
        if line:
            data = json.loads(line)
            chunk = data["message"]["content"]
            full_text += chunk
    stop_event.set()
    t.join()
    print(full_text)
else:
    print(f"Error: {response.status_code}")
    
