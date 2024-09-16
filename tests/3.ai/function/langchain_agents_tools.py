# this code is deprecated
from langchain_openai import ChatOpenAI

from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
import os
from dotenv import load_dotenv

# Load environment variables if needed
load_dotenv()

# Initialize Arxiv and Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

search = DuckDuckGoSearchRun(name="Search")

# Get Groq API Key from environment variable or prompt user input
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    api_key = input("Enter your Groq API Key: ")

# Initial message from the assistant
messages = [
    {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
]

# Display initial message
for msg in messages:
    if msg['role'] == 'assistant':
        print(f"Assistant: {msg['content']}")
    else:
        print(f"User: {msg['content']}")

# Main loop to interact with the chatbot
while True:
    prompt = input("You: ")

    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": prompt})

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    
    tools = [search, arxiv, wiki]
    
    # Initialize the agent
    search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=True)
    
    # Run the agent
    response = search_agent.run(messages)
    
    # Append and display assistant's response
    messages.append({'role': 'assistant', "content": response})
    print(f"Assistant: {response}")
