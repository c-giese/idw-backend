import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "ENDPOINT_URL"
model_name = "MODEL_NAME"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential("API_KEY"),
    
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="I am going to Paris, what should I see?"),
    ],
    max_tokens=2048,
    model=model_name
)

print(response.choices[0].message.content)