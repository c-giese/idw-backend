import requests
import json
import time
from flask import Flask, request
from flask_cors import CORS

url = "http://localhost:11434/api/chat"
greeting = "Hello, I am happy to assist you!"
conversation_history = []

app = Flask(__name__)
CORS(app)


@app.route('/initiate', methods=['GET'])
def initiate():
    return {"response": greeting}

@app.route('/query', methods=['POST'])
def query():
    """
    Handle the query from the user and send it to the Ollama model.
    """
    data = request.get_json()
    user_query = data.get('query')
    response = sendRequestToOllama(user_query)
    assistant_response = {"response": response}
    return assistant_response


def sendRequestToOllama(userQuery):
    """
    Send a request to the Ollama model and return the response.
    """
    global conversation_history
    # Add user message to history
    conversation_history.append({"role": "user", "content": userQuery})
    payload = {
        "model": "phi3:latest",
        "messages": conversation_history
    }

    response = requests.post(url, json=payload, stream=True)
    if response.status_code == 200:
        assistant_reply = ""
        for line in response.iter_lines(decode_unicode=True):
            if line:
                data = json.loads(line)
                chunk = data["message"]["content"]
                assistant_reply += chunk
        # Add assistant message to history
        conversation_history.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply.strip()
    else:
        print(f"Error: {response.status_code}") 

app.run(debug=True)



