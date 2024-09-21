# ConversationChain ConversationChain` was deprecated in LangChain 0.2.7 
# and will be removed in 1.0. Use RunnableWithMessageHistory

import time
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


# Initialize the OpenAI client with the API key
llm=Ollama(model="phi3")


memory = ConversationBufferMemory(return_messages=True,memory_key="chat_history")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant answer questions in 1 sentence"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])

conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory = ConversationBufferMemory(return_messages=True,memory_key="chat_history")
)

while True:

    user_input = input("ask me something:\n").strip().lower()
    result = conversation.invoke({"input": {user_input}})
    # print(f"\n{result}")
    print(f"\n{result}")


