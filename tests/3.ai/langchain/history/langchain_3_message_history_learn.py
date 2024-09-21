from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

import os

from dotenv import load_dotenv
load_dotenv()

model=Ollama(model="tinyllama")


# test1 = model.invoke([HumanMessage(content="Hi! I'm Bob")])
# print(test1)

print('--------')

# test2 = model.invoke([HumanMessage(content="What's my name?")])
# print(test2)

print('--------')

test3 = model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)

print(test3)

# prompt = ChatPromptTemplate.from_messages(
#         [
#             (
#                 "system",
#                 "You are a helpful assistant. Answer all questions to the best of your ability with only 1 sentence make the response as short as possible",
#             ),
#             MessagesPlaceholder(variable_name="messages"),        
#         ]
#     )

# chain = prompt | model

# response = chain.invoke({"messages": [HumanMessage(content="hi! I'm bob")]})


# print(response)