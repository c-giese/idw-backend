import requests
import json
import time

url = 'http://localhost:11434/api/chat'

greeting = "Hi how can i help you?"

print(greeting)

while True:
    userMessage = input("You: ")
    payload = {
        "model": "phi3:latest",
        "messages": [
            {
                "role": "user",
                "content": userMessage
            }
        ],
    }

    response = requests.post(url, json = payload, stream = True)

    if response.status_code == 200:
        for line in response.iter_lines(decode_unicode=True):
            if line:
                data = json.loads(line)
                chunk = data["message"]["content"]
                print(chunk, flush = True, end="")
                time.sleep(0.05)
        print()
    else:
        print(f"Error {response.status_code}")    
