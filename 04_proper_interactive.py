import requests
import json
import time
from typing import List, Dict, Optional, Generator

# --- Constants ---
# Set up the base URL for the local Ollama API
# Typically defaults to localhost:11434, but can be changed in the Ollama config
OLLAMA_API_URL: str = "http://localhost:11434/api/chat"
# The AI model to use for the chat
MODEL_NAME: str = "phi3:latest"
# Message displayed when the script starts
GREETING_MESSAGE: str = "Hello! I'm your assistant. How can I help you today? \nType 'bye', 'goodbye', 'thank you', 'exit' or 'quit' to end the conversation."
# Keywords to end the conversation
EXIT_KEYWORDS: set[str] = {"exit", "quit", "bye", "goodbye", "thank you"}
# Delay between printing response chunks for a streaming effect
STREAM_DELAY: float = 0.05

# --- Functions ---

def stream_response(response: requests.Response) -> Generator[str, None, None]:
    """Streams the response content chunk by chunk."""
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                data = json.loads(line)
                chunk = data.get("message", {}).get("content", "")
                if chunk:
                    yield chunk
            except json.JSONDecodeError:
                print(f"\nWarning: Could not decode JSON line: {line}")


def get_assistant_response(history: List[Dict[str, str]]) -> Optional[str]:
    """
    Sends the conversation history to the Ollama API and streams the response.

    Args:
        history: A list of message dictionaries representing the conversation.

    Returns:
        The full assistant reply as a string, or None if an error occurred.
    """
    payload = {
        "model": MODEL_NAME,
        "messages": history
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        print("Assistant: ", end="", flush=True)
        assistant_reply = ""
        for chunk in stream_response(response):
            print(chunk, end="", flush=True)
            assistant_reply += chunk
            time.sleep(STREAM_DELAY)
        print()  # Newline after the full response
        return assistant_reply

    except requests.exceptions.RequestException as e:
        print(f"\nError connecting to Ollama API: {e}")
        return None
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return None


def main():
    """Runs the main interactive chat loop."""
    conversation_history: List[Dict[str, str]] = []
    print(GREETING_MESSAGE)

    # Initializing the conversation loop
    while True:
        try:
            user_query = input("\nYou: ")
        except EOFError: # Handle Ctrl+D or end of input stream
            print("\nGoodbye!")
            break

        if user_query.lower() in EXIT_KEYWORDS:
            print("Goodbye, have a nice day!")
            break

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_query})

        # Get response from the assistant
        assistant_reply = get_assistant_response(conversation_history)

        # If a reply was successfully received, add it to the history
        if assistant_reply is not None:
            conversation_history.append({"role": "assistant", "content": assistant_reply})
        else:
            # Optional: Remove the last user message if the API call failed,
            # so the user can retry the same query without it being duplicated.
            # conversation_history.pop()
            print("Assistant could not respond. Please try again.")


# --- Main Execution ---
if __name__ == "__main__":
    main()