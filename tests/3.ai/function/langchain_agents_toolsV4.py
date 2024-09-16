from langchain_core.tools import tool
import threading
import datetime
import pygame
import time
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool

# Load environment variables
load_dotenv()

# Initialize pygame mixer for sound
try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Pygame mixer initialization failed: {e}")

# Global flag to control the alarm sound
alarm_running = False

def play_alarm_sound():
    global alarm_running
    file_path = "alarm/alarm.WAV"
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    while alarm_running:
        print("Playing alarm")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        time.sleep(5)  # Adjust sleep time according to the length of the sound

# Custom tool class to prevent passing unnecessary arguments
class StartAlarmTool(Tool):
    def __init__(self):
        super().__init__(
            name="start_alarm",
            func=self._run,
            description="Start an alarm sound."
        )

    def _to_args_and_kwargs(self, tool_input: str):
        return (), {}

    def _run(self):
        global alarm_running
        print("Starting alarm")
        alarm_running = True
        alarm_thread = threading.Thread(target=play_alarm_sound)
        alarm_thread.start()

    def _arun(self):
        raise NotImplementedError("start_alarm does not support async")

class StopAlarmTool(Tool):
    def __init__(self):
        super().__init__(
            name="stop_alarm",
            func=self._run,
            description="Stop the alarm sound."
        )

    def _to_args_and_kwargs(self, tool_input: str):
        return (), {}

    def _run(self):
        global alarm_running
        print("Stopping alarm")
        alarm_running = False
        pygame.mixer.music.stop()

    def _arun(self):
        raise NotImplementedError("stop_alarm does not support async")

class GetCurrentTimeTool(Tool):
    def __init__(self):
        super().__init__(
            name="get_current_time",
            func=self._run,
            description="Get the current date and time."
        )

    def _to_args_and_kwargs(self, tool_input: str):
        return (), {}

    def _run(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _arun(self):
        raise NotImplementedError("get_current_time does not support async")

# Main loop to interact with the chatbot
while True:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    tools = [StartAlarmTool(), StopAlarmTool(), GetCurrentTimeTool()]

    agent_prompt = hub.pull("hwchase17/react")
    
    # Initialize the agent
    search_agent = create_react_agent(tools=tools, llm=llm, prompt=agent_prompt)
    agent_executor = AgentExecutor(agent=search_agent, tools=tools, verbose=True)

    # Define user input
    user_input = "ring the alarm"

    # Prepare conversation messages
    messages = {"input": user_input}

    # Run the agent
    response = agent_executor.invoke(messages)

    # Print the assistant's response
    print(f"Assistant: {response}")

    print("Goodbye!")
    break
