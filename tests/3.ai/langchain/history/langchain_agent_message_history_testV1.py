
#  Not working

import time
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.tools.render import format_tool_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents import AgentExecutor
from langchain.tools import tool
import os

# Initialize the OpenAI client with the API key
llm=Ollama(model="phi3")

@tool
def get_weather(location: str) -> str:
    """
    Fetches the current weather for the specified location.

    Args:
        location (str): The name of the location to get the weather for.

    Returns:
        str: A string describing the weather in the location.
    """
    return f"The weather in {location} is sunny."


memory = ConversationBufferMemory(return_messages=True,memory_key="chat_history")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant answer questions in 1 sentence"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])

tools = [get_weather]  


chain = prompt | llm 


agent_chain = RunnablePassthrough.assign(
    agent_scratchpad= lambda x: format_to_openai_functions(x["intermediate_steps"])
) | chain

agent_executor = AgentExecutor(agent=agent_chain, tools=tools, verbose=True)

chat_history = memory.load_memory_variables({})

while True:

    
    user_input = input("ask me something:\n").strip().lower()

    result = chain.invoke({"input": user_input, "chat_history": chat_history.get("chat_history", [])})
    print(f"\n{result}")


