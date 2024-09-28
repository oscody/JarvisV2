#  pip install langchain-groq 

import time
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
print(groq_api_key)

# Initialize OpenAI client for GPT-3.5-turbo
model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

# Define the prompt and system message
user_input = "what is the capital of jamaica?"
system_message = "You are a helpful assistant"

# Start the timer for GPT-3.5-turbo
start_time = time.time()

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = model.invoke(messages)


# Stop the timer
end_time = time.time()
elapsed_time_turbo = end_time - start_time

# Print GPT-3.5-turbo results
print(ai_msg)
print(f"Time taken groq Gemma2 : {elapsed_time_turbo:.2f} seconds")


