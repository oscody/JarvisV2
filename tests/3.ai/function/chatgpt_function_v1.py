import threading
import datetime
import pygame
import time
import os
# import openai
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional
import uuid

# Initialize pygame mixer for sound
try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Pygame mixer initialization failed: {e}")

# Global dictionary to manage multiple alarms
alarms = {}
alarm_lock = threading.Lock()

def play_alarm_sound(alarm_id):
    print(f"starting audio")
    file_path = "alarm/alarm.WAV"
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    while alarms.get(alarm_id, False):
        # print(f"playing audio")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        time.sleep(5)  # Adjust sleep time according to the length of the sound

def start_alarm(alarm_id, alarm_time, label=None):
    with alarm_lock:
        alarms[alarm_id] = True
    alarm_thread = threading.Thread(target=play_alarm_sound, args=(alarm_id,))
    alarm_thread.start()
    print(f"Alarm '{label}' set for {alarm_time} with ID {alarm_id}.")

def stop_alarm(alarm_id):
    with alarm_lock:
        if alarm_id in alarms:
            alarms[alarm_id] = False
            pygame.mixer.music.stop()
            print(f"Alarm '{alarm_id}' stopped.")
        else:
            print(f"No alarm found with ID: {alarm_id}")

# Define the CreateAlarm schema
class CreateAlarm(BaseModel):
    time: str = Field(..., description="Time to set the alarm in HH:MM format (24-hour).")
    label: Optional[str] = Field(None, description="Optional label for the alarm.")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def create_alarm_via_ollama(user_input: str):
    system_message = "You are an assistant that helps users create alarms."

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_input}
    ]

    # Define the function schema for create_alarm
    functions = [
        {
            "name": "create_alarm",
            "description": "Create an alarm with a specified time and optional label.",
            "parameters": {
                "type": "object",
                "properties": {
                    "time": {
                        "type": "string",
                        "description": "Time to set the alarm in HH:MM format (24-hour)."
                    },
                    "label": {
                        "type": "string",
                        "description": "Optional label for the alarm."
                    }
                },
                "required": ["time"]
            }
        }
    ]

    try:
        response = client.chat.completions.create(
             model="gpt-3.5-turbo",
            messages=messages,
            functions=functions,
            function_call="auto"  # Let the model decide to call a function
        )
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return

    choice = response.choices[0]
    if choice.finish_reason == "function_call":
        function_call = choice.message.function_call
        function_name = function_call.name
        arguments = function_call.arguments
        
        if function_name == "create_alarm":
            try:
                args = CreateAlarm.parse_raw(arguments)
                # Generate a unique alarm ID
                alarm_id = str(uuid.uuid4())
                start_alarm(alarm_id, args.time, args.label)
                print(f"Alarm set for {args.time} with label '{args.label}' (ID: {alarm_id}).")
            except Exception as e:
                print(f"Error parsing function arguments: {e}")
        else:
            print(f"Unknown function called: {function_name}")
    else:
        # Accessing the content directly
        print("Assistant response:", choice.message.content)


def main():
    while True:
        user_input = input("\nOptions:\n1. Create Alarm\n2. Stop Alarm\n3. Quit\nEnter your choice: ").strip().lower()
        
        if user_input in ["1", "create alarm"]:
            alarm_details = input("Please describe your alarm (e.g., 'Set an alarm for 07:30 labeled Morning Workout'):\n")
            create_alarm_via_ollama(alarm_details)
        
        elif user_input in ["2", "stop alarm"]:
            alarm_id = input("Enter the Alarm ID to stop: ").strip()
            stop_alarm(alarm_id)
        
        elif user_input in ["3", "quit"]:
            print("Exiting...")
            # Stop all running alarms
            with alarm_lock:
                for alarm_id in list(alarms.keys()):
                    stop_alarm(alarm_id)
            break
        
        else:
            print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()
