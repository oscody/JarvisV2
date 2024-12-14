# not working
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os
import helper.file_handler as file
from tools import fetch_mails, get_current_time

load_dotenv()

system_message = file.read_file_content('V2/system_prompt.txt')
print('AI-------', system_message)

groq_modelName = "llama-3.2-1b-preview"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

groq_api_key = os.getenv("GROQ_API_KEY")

class llm:
    def __init__(self, model_name="", platform=""):
        self.model_name = model_name
        self.store = {}
        self.platform = platform
        self.model = self._initialize_model()
        self.tools = [
            Tool(
                name="FetchMails",
                func=fetch_mails,
                description="Fetches the latest emails."
            ),
            Tool(
                name="GetCurrentTime",
                func=get_current_time,
                description="Returns the current time."
            ),
        ]
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Strict adherence to these guidelines is crucial. Answer with a maximum of 1-2 sentences. You are an assistant called Zenith. Answer any questions without any additional content. {language}.",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.model,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            memory=self.memory
        )

    def _initialize_model(self):
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        print(f"session_id-{session_id}")
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]

    def invoke(self, user_input: str, session_id: str = "1", language: str = "english"):
        print(f"user input: {user_input}")

        try:
            response = self.agent.invoke(input=user_input)
            print(f"llm: {response}")
            return response
        except Exception as e:
            print(f"Error: {e}")
            return str(e)