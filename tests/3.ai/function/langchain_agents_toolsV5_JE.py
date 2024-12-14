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
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import json

# Load environment variables
load_dotenv()

# Initialize pygame mixer for sound
try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Pygame mixer initialization failed: {e}")

# Global variables
alarm_running = False
scheduler = BackgroundScheduler()
scheduler.start()
scheduled_tasks = {}

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
        time.sleep(5)

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
        return "Alarm started successfully"

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
        return "Alarm stopped successfully"

class ScheduleTaskTool(Tool):
    def __init__(self):
        super().__init__(
            name="schedule_task",
            func=self._run,
            description="Schedule a task. Input should be JSON with 'task', 'schedule_type' (cron/interval), and 'schedule_value'"
        )

    def _run(self, task_input: str):
        try:
            task_data = json.loads(task_input)
            task = task_data['task']
            schedule_type = task_data['schedule_type']
            schedule_value = task_data['schedule_value']
            
            job_id = f"task_{len(scheduled_tasks)}"
            
            if schedule_type == 'cron':
                trigger = CronTrigger.from_crontab(schedule_value)
            elif schedule_type == 'interval':
                trigger = {'seconds': int(schedule_value)}
            else:
                return "Invalid schedule_type. Use 'cron' or 'interval'"

            scheduler.add_job(
                self._execute_task,
                trigger,
                args=[task],
                id=job_id
            )
            
            scheduled_tasks[job_id] = {
                'task': task,
                'schedule_type': schedule_type,
                'schedule_value': schedule_value
            }
            
            return f"Task scheduled successfully with ID: {job_id}"
        except Exception as e:
            return f"Error scheduling task: {str(e)}"

    def _execute_task(self, task):
        messages = {"input": task}
        agent_executor.invoke(messages)

class ListScheduledTasksTool(Tool):
    def __init__(self):
        super().__init__(
            name="list_scheduled_tasks",
            func=self._run,
            description="List all scheduled tasks"
        )

    def _run(self):
        return json.dumps(scheduled_tasks, indent=2)

class CancelTaskTool(Tool):
    def __init__(self):
        super().__init__(
            name="cancel_task",
            func=self._run,
            description="Cancel a scheduled task by ID"
        )

    def _run(self, task_id: str):
        if task_id in scheduled_tasks:
            scheduler.remove_job(task_id)
            del scheduled_tasks[task_id]
            return f"Task {task_id} cancelled successfully"
        return f"Task {task_id} not found"

def initialize_agent():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    tools = [
        StartAlarmTool(),
        StopAlarmTool(),
        ScheduleTaskTool(),
        ListScheduledTasksTool(),
        CancelTaskTool()
    ]

    agent_prompt = hub.pull("hwchase17/react")
    search_agent = create_react_agent(tools=tools, llm=llm, prompt=agent_prompt)
    return AgentExecutor(agent=search_agent, tools=tools, verbose=True)

def main():
    global agent_executor
    agent_executor = initialize_agent()

    try:
        while True:
            user_input = input("Enter your command (or 'exit' to quit): ")
            
            if user_input.lower() == 'exit':
                break
                
            messages = {"input": user_input}
            response = agent_executor.invoke(messages)
            print(f"Assistant: {response['output']}")
            
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        scheduler.shutdown()
        pygame.mixer.quit()

if __name__ == "__main__":
    main()
