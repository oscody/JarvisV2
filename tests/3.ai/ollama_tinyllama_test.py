import time
import openai
from openai import OpenAI

user_input = "Can you tell me a joke?"

system_message = "You are a helpful assistant"

# Initialize the OpenAI client with the API key
client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

messages = [{"role": "system", "content": system_message}] + [{"role": "user", "content": user_input}]

# Start the timer
start_time = time.time()

completion = client.chat.completions.create(
    model="tinyllama",
    messages=messages
)

# Stop the timer
end_time = time.time()
elapsed_time = end_time - start_time

print(completion.choices[0].message)
answer = completion.choices[0].message.content
print(f"Answer = {answer}")
print(f"Time taken tinyllama : {elapsed_time:.2f} seconds")
