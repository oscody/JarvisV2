import time
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Start the timer
start_time = time.time()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helful assistant"},
        {"role": "user", "content": "Can you tell me a joke?"}
    ]
)

# Stop the timer
end_time = time.time()
elapsed_time = end_time - start_time

print(completion.choices[0].message)
answer = completion.choices[0].message.content
print(f"Answer = {answer}")
print(f"Time taken gpt-3.5-turbo : {elapsed_time:.2f} seconds")
