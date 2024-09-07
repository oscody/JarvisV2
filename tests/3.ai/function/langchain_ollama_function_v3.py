from typing import List
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
import threading
import datetime
import pygame
import time
import os

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
        print(f"Playing alarm")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        time.sleep(5)  # Adjust sleep time according to the length of the sound

@tool
def start_alarm() -> None:
    """Start an alarm sound."""
    global alarm_running
    print(f"Starting alarm")
    alarm_running = True
    alarm_thread = threading.Thread(target=play_alarm_sound)
    alarm_thread.start()

@tool
def stop_alarm() -> None:
    """Stop the alarm sound."""
    global alarm_running
    print(f"Stopping alarm")
    alarm_running = False
    pygame.mixer.music.stop()

@tool
def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def run(modelName: str):
    
    # Initialize the ChatOllama model
    model = ChatOllama(
        model=modelName,
        keep_alive=-1,
        format="json",
    )
    
    # Bind the tools to the model using the @tool pattern
    model = model.bind_tools([start_alarm, stop_alarm, get_current_time])

    # Invoke the model
    response = model.invoke("Could you create an alarm for 5:19?")
    print(response)

run('llama3.1')
# run('phi3') not working
