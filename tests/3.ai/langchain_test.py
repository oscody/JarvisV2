import time

from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate

# Initialize the OpenAI client with the API key
llm=Ollama(model="tinyllama")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant answer questions is in only 5 1 sentence"),
    ("user", "{input}"),
])


chain = prompt | llm 

# Start the timer
start_time = time.time()


result = chain.invoke({"input": "tell me about canada?"})

# Stop the timer
end_time = time.time()
elapsed_time = end_time - start_time



print(f"Time taken tinyllama : {elapsed_time:.2f} seconds")
print(f"\n{result}")

