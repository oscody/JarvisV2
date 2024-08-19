import time
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Get API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client for GPT-3.5-turbo
client_turbo = OpenAI(api_key=OPENAI_API_KEY)

# Define the prompt and system message
user_input = "what is the capital of jamaica?"
system_message = "You are a helpful assistant"

# Start the timer for GPT-3.5-turbo
start_time = time.time()

# Create completion request for GPT-3.5-turbo
completion_turbo = client_turbo.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_input}
    ]
)

# Stop the timer
end_time = time.time()
elapsed_time_turbo = end_time - start_time

# Print GPT-3.5-turbo results
print(completion_turbo.choices[0].message)
answer_turbo = completion_turbo.choices[0].message.content
print(f"Answer (gpt-3.5-turbo) = {answer_turbo}")
print(f"Time taken gpt-3.5-turbo : {elapsed_time_turbo:.2f} seconds")

# Initialize OpenAI client for tinyllama
client_tinyllama = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Start the timer for tinyllama
start_time = time.time()

# Create completion request for tinyllama
completion_tinyllama = client_tinyllama.chat.completions.create(
    model="tinyllama",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_input}
    ]
)

# Stop the timer
end_time = time.time()
elapsed_time_tinyllama = end_time - start_time

# Print tinyllama results
print(completion_tinyllama.choices[0].message)
answer_tinyllama = completion_tinyllama.choices[0].message.content
print(f"Answer (tinyllama) = {answer_tinyllama}")
print(f"Time taken tinyllama : {elapsed_time_tinyllama:.2f} seconds")


# Initialize OpenAI client for tinyllama
client_llama3= OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Start the timer for tinyllama
start_time = time.time()

# Create completion request for llama3
completion_llama3 = client_llama3.chat.completions.create(
    model="llama3",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_input}
    ]
)

# Stop the timer
end_time = time.time()
elapsed_time_llama3 = end_time - start_time

# Print llama3 results
print(completion_llama3.choices[0].message)
answer_llama3 = completion_llama3.choices[0].message.content
print(f"Answer (llama3) = {answer_llama3}")
print(f"Time taken llama3 : {elapsed_time_llama3:.2f} seconds")

