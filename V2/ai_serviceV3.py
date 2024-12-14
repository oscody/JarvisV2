from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq
import random
from dotenv import load_dotenv
import os
import helper.file_handler as file

load_dotenv()

system_message = file.read_file_content('V2/system_prompt.txt')
print('AI-------',system_message)

groq_modelName = "llama-3.2-1b-preview"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
# print(f"OPENAI_API_KEY{OPENAI_API_KEY}")

groq_api_key=os.getenv("GROQ_API_KEY")
# print(f"groq_api_key{groq_api_key}")

class llm:
    def __init__(self, model_name="",platform=""):
        self.model_name = model_name
        self.store = {}
        self.platform = platform
        self.model = self._initialize_model()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Strict adherence to these guidelines is crucial. Answer with maximal 1-2 sentences.You are a assistant called Zenith. Answer any questions without any additional content. {language}.",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        self.chain = self.prompt | self.model

    def _initialize_model(self):

        random_number = random.choice([1, 2])
        print(f"random-{random_number}")

        # if self.platform == "Pi":
        #     if random_number == 1:
        #        return ChatOpenAI(model="gpt-3.5-turbo")
        #     else:
        #       return ChatGroq(model=groq_modelName,groq_api_key=groq_api_key)
        # else:
        #     if random_number == 2:
        #       return ChatOpenAI(model="gpt-3.5-turbo")
        #     else:
        #         return ChatGroq(model=groq_modelName,groq_api_key=groq_api_key)

        # return ChatGroq(model=groq_modelName,groq_api_key=groq_api_key,temperature=0)
        return ChatOpenAI(model="gpt-3.5-turbo",temperature=0)

    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        print(f"session_id-{session_id}")
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]

    def invoke(self, user_input: str, session_id: str = "1", language: str = "english"):
        print(f"user input-{user_input}")

        try:
            with_message_history = RunnableWithMessageHistory(
                self.chain,
                self.get_session_history,
                input_messages_key="messages",
            )
            config = {"configurable": {"session_id": session_id}}
            response = with_message_history.invoke(
                {"messages": [HumanMessage(content=user_input)], "language": language},
                config=config,
            )
            # print(f"llm-{response}")
            print(f"llm-{response.content}")
            return response.content
        except KeyboardInterrupt:
            print(f"error sending to AI")
