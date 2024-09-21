from langchain_core.tools import tool
import threading
from datetime import datetime, timedelta
import pygame
import time
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
import math
import pytz
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Initialize pygame mixer for sound
try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Pygame mixer initialization failed: {e}")

# Global list to keep track of timers
alarm_timers = []

def play_alarm_sound():
    file_path = "alarm/alarm.WAV"

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print("Playing alarm")
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        time.sleep(5)  # Adjust sleep time according to the length of the sound
        pygame.mixer.music.stop()
    except pygame.error as e:
        print(f"Error playing sound: {e}")

class ScheduleAlarmInput(BaseModel):
    alarm_time: str = Field(
        description="The time in '%I:%M %p' format when the alarm should ring, e.g., '12:32 PM'."
    )
    timezone_str: str = Field(
        default='America/New_York',
        description="The timezone string, e.g., 'America/New_York'."
    )

@tool("schedule_alarm", args_schema=ScheduleAlarmInput)
def schedule_alarm(input: ScheduleAlarmInput):
    """
    Schedule an alarm at the specified time in the given timezone.
    """
    try:
        # Get the timezone object
        tz = pytz.timezone(input.timezone_str)

        # Get the current time in the specified timezone
        current_time = datetime.now(tz)
        print(f"current_time: {current_time}")

        # Parse the alarm time into a naive datetime object
        alarm_naive = datetime.strptime(input.alarm_time, "%I:%M %p")

        # Localize the alarm time to the specified timezone and today's date
        alarm_time_obj = tz.localize(datetime.combine(current_time.date(), alarm_naive.time()))

        # If the alarm time has already passed, set it for the next day
        if alarm_time_obj < current_time:
            alarm_time_obj += timedelta(days=1)

        delay = (alarm_time_obj - current_time).total_seconds()

        # Schedule the alarm using threading.Timer
        alarm_timer = threading.Timer(delay, play_alarm_sound)
        alarm_timer.start()

        # Add the timer to the list
        alarm_timers.append(alarm_timer)

        # Calculate hours, minutes, and seconds from delay
        hours = int(delay // 3600)
        minutes = int((delay % 3600) // 60)
        seconds = delay % 60
        print(f"Delay: {hours} hours, {minutes} minutes, {seconds:.2f} seconds")

        return f"Delay: {hours} hours, {minutes} minutes, {seconds:.2f} seconds. The alarm has been successfully scheduled for {input.alarm_time} {input.timezone_str}."
    except Exception as e:
        return f"Error scheduling alarm: {e}"

class GetCurrentTimeTool(Tool):
    def __init__(self):
        super().__init__(
            name="get_current_time",
            func=self._run,
            description="Get the current date and time in a specified timezone."
        )

    def _to_args_and_kwargs(self, tool_input: str):
        return (), {}

    def _run(self):
        tz = pytz.timezone('America/New_York') 
        return datetime.now(tz).strftime('%I:%M %p')

    def _arun(self):
        raise NotImplementedError("get_current_time does not support async")

# Main loop to interact with the chatbot
if __name__ == "__main__":
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-0613", temperature=0)

    tools = [schedule_alarm, GetCurrentTimeTool()]

    agent_prompt = hub.pull("hwchase17/react")

    # Initialize the agent
    search_agent = create_react_agent(tools=tools, llm=llm, prompt=agent_prompt)
    agent_executor = AgentExecutor(agent=search_agent, tools=tools, verbose=True)

    # Define user input
    user_input = "set an alarm for 12:40 pm"

    # Prepare conversation messages
    messages = {"input": user_input}

    # Run the agent
    response = agent_executor.invoke(messages)

    # Print the assistant's response
    print(f"Assistant: {response}")

    time.sleep(120)

    print("Goodbye!")
