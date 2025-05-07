# Tasks

This document outlines the planned steps during the workshop.

## Technical requirements
The following programs/runtimes should be installed on yp
- Python (https://www.python.org/downloads/)
- Node.js + npm (https://nodejs.org/en)
- VS Code (https://code.visualstudio.com/)
- Angular CLI (https://angular.dev/tools/cli/setup-local)




## Ollama
First, we want to get to know ollama, how to chat with models and modify them

1. Install Ollama from https://ollama.com/ 
2. Open a terminal and run `ollama run <MODEL_NAME>` to chat with a model
3. Download and run a second model
4. Create your own Model with a Modelfile and `ollama create`

## Python Backend
Next, we want to incrementally build a python backend that utilized ollama via api

1. Install a virtual environment for python development with `python -m venv .venv`
2. Activate that venv by executing `.venv/Scripts/activate` 
3. Write a first simple python backend, using the requests module [00_response.py]
4. Modify your file, so that the response is shown as a stream in the terminal (flushed) [02_stream_response.py]
5. Make an interactive version of your backend
   1. Prompt the user to ask a question
   2. Implement a strategy to allow the user to ask other questions after the first question was answered[03_restricted_interactive.py]
   3. Make the LLM "remember the conversation" so you can chat with it on a continuous topic [04_interactive.py]

## Flask and Angular basics
In order to make the app more capable, we first need to install Flask to build a REST-API and make it visually more appealing by using Angular, a TypeScript based Frontend Framework.

1. First Flask app
   1. Create a new python file and initialize a Flask app
   2. Create a first get route that returns an arbitrary string
   3. Start the app and test the route in the browser
2. Clone the angular repository with `git clone https://github.com/c-giese/idw-frontend.git` + run `npm install` in the directory
3. Run `ng serve` in the frontend directory to start the app and test the implemented get request.
4. Add a static request to ollama in the backend, and return that value as answer to the get request.
5. Implement post requests and make the frontend interactive
   1. Implement a post request with static payload, that is used to make a request to ollama. Return that value to the frontend and display it.
   2. Add an input field and a send button to make custom prompts available.


## Your own project
Now it is time for you to play around and build your own application

Here are some possible projects:

### Chatbot
Finish the started project and implement all the features, we have learned about in the backend part, e.g.
    - Make the backend remember the chat history
    - Visualize the chat history
    - Implement concurrent chats (so not all chats share the same history)
    - Modify the system prompt by creating a new model
    - You can test the ollama module in the backend, that makes handling requests easier


### FAQ/Course Chatbot
Basically the same as the first chatbot idea, but a bit enhanced. This leads into the direction of RAG (Retrieval Augmented Generation).
We want to be able to ask the bot questions about specific university courses or courses of study in general.
So we need to make sure, that the llm has data about the courses we have questions about.
The Moduldatenbank of the FH is openly accessible, so we can get data from there. 
If interested, we can discuss possible ways to address this task in person.

### Your Idea
