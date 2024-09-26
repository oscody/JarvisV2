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
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from langchain_core.messages import HumanMessage, AIMessage
import openai
from langchain_openai import ChatOpenAI
import os
import atexit
from dotenv import load_dotenv
load_dotenv()


# Correct path to the PDF file
temppdf = "/Users/bogle/Dev/Agent/JarvisV2/uploads/Clean code.pdf"

# I want to change the way i define
# I want to move to a new folder
# Define the SQLite database
DATABASE_URL = "sqlite:///chat_history.db"
Base = declarative_base()

# Define the Session model
class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    session_id = Column(String, unique=True, nullable=False)
    messages = relationship("Message", back_populates="session")

# Define the Message model
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    session = relationship("Session", back_populates="messages")

# Create the database and the tables
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to save a single message
def save_message(session_id: str, role: str, content: str):
    db = next(get_db())
    try:
        session = db.query(Session).filter(Session.session_id == session_id).first()
        if not session:
            session = Session(session_id=session_id)
            db.add(session)
            db.commit()
            db.refresh(session)

        db.add(Message(session_id=session.id, role=role, content=content))
        db.commit()
    except SQLAlchemyError:
        db.rollback()
    finally:
        db.close()

# Function to load chat history
def load_session_history(session_id: str) -> BaseChatMessageHistory:
    db = next(get_db())
    chat_history = ChatMessageHistory()
    try:
        session = db.query(Session).filter(Session.session_id == session_id).first()
        if session:
            for message in session.messages:
                if message.role == "human":
                    chat_history.add_message(HumanMessage(content=message.content))
                elif message.role == "ai":
                    chat_history.add_message(AIMessage(content=message.content))
    except SQLAlchemyError:
        pass
    finally:
        db.close()

    return chat_history


# set up session


# Modify the get_session_history function to use the database
def get_session_history(session_id:str)->BaseChatMessageHistory:
    if session_id not in session_state:
        # session_state[session_id]=ChatMessageHistory()
        chat_history = load_session_history(session_id)
        print(f'chat hist--{chat_history}')
        session_state[session_id] = chat_history
    return session_state[session_id]

# Ensure you save the chat history to the database when needed
def save_all_sessions():
    for session_id, chat_history in session_state.items():
        for message in chat_history.messages:
            # Determine role based on message type
            if isinstance(message, HumanMessage):
                role = "human"
            elif isinstance(message, AIMessage):
                role = "ai"
            else:
                role = "system"  # Or any other roles if applicable
            save_message(session_id, role, message.content)



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

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

session_id = input("Session ID : ").strip().lower()

session_state = {}

while True:

    try:
        user_input = input("your question ").strip().lower()

        # save_message(session_id, "human", user_input)

        # Check for exit command
        if user_input == 'exit':
            atexit.register(save_all_sessions)
            print("Exiting the application...")
            break  # Exit the while loop

        if user_input:
            session_history=get_session_history(session_id)
            response = conversational_rag_chain.invoke(
                {"input": user_input},
                config={
                    "configurable": {"session_id":session_id}
                },  # constructs a key "abc123" in `store`.
            )
            
            print("Assistant:", response['answer'])


            # save_message(session_id, 'ai', response.content)
                # print(message.content)
            # print(session_state)
            # print("Chat History:", session_history.messages)

    except KeyboardInterrupt:
        # Example of saving all sessions before exiting the application
        atexit.register(save_all_sessions)
        print("\saving...")
        break

    finally:
        print("ending code")
        

