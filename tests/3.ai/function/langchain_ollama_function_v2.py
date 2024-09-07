import asyncio
import threading
import datetime
import pygame
import time
import os
from langchain_ollama import ChatOllama

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
        print(f"play alarm")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        time.sleep(5)  # Adjust sleep time according to the length of the sound

def start_alarm():
    print(f"start alarm")
    global alarm_running
    alarm_running = True
    alarm_thread = threading.Thread(target=play_alarm_sound)
    alarm_thread.start()

def stop_alarm():
    print(f"stop alarm")
    global alarm_running
    alarm_running = False
    pygame.mixer.music.stop()

def get_current_time() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def run(modelName: str):
    
    # Initialize the ChatOllama model
    model = ChatOllama(
        model=modelName,
        keep_alive=-1,
        format="json",
    )
    
    # Bind the tools to the model
    model = model.bind_tools(
        tools=[
            {
                "name": "start_alarm",
                "description": "Starts an alarm sound",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
            {
                "name": "stop_alarm",
                "description": "Stops the alarm sound",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
            {
                "name": "get_current_time",
                "description": "Gets the current date and time",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        ],
        function_call={"name": "start_alarm"},
    )

    # Invoke the model
    response = model.invoke("create an alarm for 5:19")  # Ensure this is an async call
    print(response)

run('llama3.1')
# run('phi3') not working
