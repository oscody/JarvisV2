import time
import openai
from openai import OpenAI

user_input = "Who painted the Mona Lisa?"

system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short"

# Initialize the OpenAI client with the API key
client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

messages = [{"role": "system", "content": system_message}] + [{"role": "user", "content": user_input}]

# Start the timer
start_time = time.time()

streamed_completion = client.chat.completions.create(
    model="tinyllama",
    messages=messages,
    stream=True
)

# Extract and return the response
response = ''
for chunk in streamed_completion:
    print(f"Response: {chunk.choices[0].delta.content}")
    response += chunk.choices[0].delta.content

# Stop the timer
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Response: {response}")
print(f"Time taken: {elapsed_time:.2f} seconds")
