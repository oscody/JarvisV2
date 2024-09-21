from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
import openai
from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv
load_dotenv()


# Correct path to the PDF file
temppdf = "/Users/bogle/Dev/Agent/JarvisV2/uploads/Cormen_Algorithms_3rd.pdf"


os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# Load the PDF
loader = PyPDFLoader(temppdf)
docs = loader.load()


# Initialize the documents list and extend with loaded docs
documents = docs


# Assuming 'documents' is a predefined list
documents.extend(docs)


# Split and create embeddings for the documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=500)
splits = text_splitter.split_documents(documents)


vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever()    

contextualize_q_system_prompt=(
    "Given a chat history and the latest user question"
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)
contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

history_aware_retriever=create_history_aware_retriever(llm,retriever,contextualize_q_prompt)

system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )
qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

question_answer_chain=create_stuff_documents_chain(llm,qa_prompt)
rag_chain=create_retrieval_chain(history_aware_retriever,question_answer_chain)



# set up session
session_id = input("Session ID : ").strip().lower()

session_state = {}

def get_session_history(session:str)->BaseChatMessageHistory:
    if session_id not in session_state:
        session_state[session_id]=ChatMessageHistory()
    return session_state[session_id]



conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

while True:
    user_input = input("your question ").strip().lower()
    if user_input:
        session_history=get_session_history(session_id)
        response = conversational_rag_chain.invoke(
            {"input": user_input},
            config={
                "configurable": {"session_id":session_id}
            },  # constructs a key "abc123" in `store`.
        )
        print(session_state)
        print("Assistant:", response['answer'])
        print("Chat History:", session_history.messages)