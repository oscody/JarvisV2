import openai
from openai import OpenAI


def send_to_ai(user_input):

    print(f"send_to_ai-{user_input}")

    system_message = "You are  a assistant use swear words like to spice up the conversation. KEEP THE RESPONSES VERY SHORT AND CONVERSATIONAL."

    # Initialize the OpenAI client with the API key
    client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

    messages = [{"role": "system", "content": system_message}] + [{"role": "user", "content": user_input}]

    streamed_completion = client.chat.completions.create(
        model="llama3",
        messages=messages,
        temperature=1,
        stream=True
    )

    # Extract and return the response
    response = ''
    for chunk in streamed_completion:
            response += chunk.choices[0].delta.content

    print(f"send_to_ai-{response}")
    return response
