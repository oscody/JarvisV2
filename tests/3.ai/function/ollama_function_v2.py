import ollama
import asyncio
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
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        time.sleep(5)  # Adjust sleep time according to the length of the sound

def start_alarm():
    global alarm_running
    alarm_running = True
    alarm_thread = threading.Thread(target=play_alarm_sound)
    alarm_thread.start()

def stop_alarm():
    global alarm_running
    alarm_running = False
    pygame.mixer.music.stop()

def get_current_time() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

async def run(model: str):
    client = ollama.AsyncClient()

    # Define system message
    system_message = "You are an assistant that helps users create alarms."

    while True:
        user_input = input("Please enter a command (start alarm, stop alarm, get time, or quit): ").strip().lower()
        
        if user_input == 'quit':
            print("Exiting...")
            break

        # Initialize conversation
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ]

        # First API call: Send the query and function description to the model
        response = await client.chat(
            model=model,
            messages=messages,
            tools=[
                {
                    'type': 'function',
                    'function': {
                        'name': 'start_alarm',
                        'description': 'Starts an alarm sound',
                        'parameters': {
                            'type': 'object',
                            'properties': {},
                            'required': [],
                        },
                    },
                },
                {
                    'type': 'function',
                    'function': {
                        'name': 'stop_alarm',
                        'description': 'Stops the alarm sound',
                        'parameters': {
                            'type': 'object',
                            'properties': {},
                            'required': [],
                        },
                    },
                },
                {
                    'type': 'function',
                    'function': {
                        'name': 'get_current_time',
                        'description': 'Gets the current date and time',
                        'parameters': {
                            'type': 'object',
                            'properties': {},
                            'required': [],
                        },
                    },
                },
            ],
        )

        # Add the model's response to the conversation history
        messages.append(response['message'])

        # Check if the model decided to use the provided functions
        if not response['message'].get('tool_calls'):
            print("The model didn't use the function. Its response was:")
            print(response['message']['content'])
            continue

        # Process function calls made by the model
        available_functions = {
            'start_alarm': start_alarm,
            'stop_alarm': stop_alarm,
            'get_current_time': get_current_time,
        }
        for tool in response['message']['tool_calls']:
            function_to_call = available_functions[tool['function']['name']]
            function_response = function_to_call(**tool['function']['arguments'])
            # Print the function response
            if function_response:
                print(function_response)

        # Second API call: Get final response from the model
        final_response = await client.chat(model=model, messages=messages)
        print(final_response['message']['content'])

# Run the async function
asyncio.run(run('llama3.1'))
