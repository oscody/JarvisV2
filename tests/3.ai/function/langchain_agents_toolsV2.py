from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
from langchain import hub
from langchain.tools import Tool

from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
# from langchain.agents import initialize_agent, AgentType
from langchain.agents import AgentExecutor, create_react_agent

from langchain_community.tools.tavily_search import TavilySearchResults


import os
from dotenv import load_dotenv

# Load environment variables if needed
load_dotenv()







# Main loop to interact with the chatbot
while True:


    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")


    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
    

    wikipedia_tool = Tool(
    name="Wikipedia",
    func=api_wrapper.run,
    description="Useful for when you need to look up information on Wikipedia."
    )

    tools = [wikipedia_tool]  # Adjust as needed

    # # Get the prompt to use - you can modify this!
    agent_prompt = hub.pull("hwchase17/react")
    
    # Initialize the agent
    # search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=True)
    search_agent = create_react_agent(tools=tools, llm=llm, prompt=agent_prompt)

    # agent_executor = AgentExecutor(agent=search_agent, tools=tools, verbose=True)
    agent_executor = AgentExecutor(agent=search_agent, tools=tools)


    # Define user input
    user_input = "tell me about cradle by will wright"

    # Prepare conversation messages (if needed for conversational agents)
    messages = {"input": user_input}

    # Run the agent
    response = agent_executor.invoke(messages)
    
    print(f"Assistant: {response}")

    print("Goodbye!")
    break
