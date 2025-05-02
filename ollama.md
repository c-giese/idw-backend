## What is it?
Local LLM Runner: Its primary function is to make it easy to download, run, and interact with various open-source large language models directly on your machine, rather than relying solely on cloud-based services.
Simplified Setup: Ollama simplifies the often complex process of getting LLMs running locally. It handles tasks like downloading model weights, setting up the necessary environment, and optimizing the models for your hardware.   
Model Library: It provides access to a library of popular open-source models that you can easily pull (download) and run with simple commands. Examples include models like Llama 2, Mistral, Gemma, Cohere, and many others.   
API and Command Line Interface: Ollama offers both a command-line interface for direct interaction and scripting, and a local API that developers can use to integrate LLMs into their own applications.   
Hardware Acceleration: It's designed to leverage hardware acceleration (like GPUs) if available on your system to improve performance, though it can also run models on the CPU.   
Customization: It allows users to create, customize, and share their own models using Modelfiles.   
In essence, Ollama acts like a server or runtime specifically for running LLMs locally. It democratizes access to powerful AI models, allowing developers and users to experiment, build applications, and run models privately and offline without needing external API calls or complex configurations.   

## How to use it?

1. Install ollama from https://ollama.com/
2. In commandline `ollama serve` Starts the background server and show information
3. `ollama run <MODEL_NAME>` Starts the model locally (If absent, it loads it first)
4. Now you can chat with the model
5. Create a custom version of an llm with Modelfile and `ollama create <NEW_MODEL_NAME> -f ./modelfile`
    -> This model can be used like the others with `ollama run` or via api