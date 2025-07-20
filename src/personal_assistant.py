import os
import json
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(script_dir, '.env')
load_dotenv(env_path)

class PersonalAssistant:
    def __init__(self, name="Dhee", user_name="User"):
        self.name = name
        self.user_name = user_name
        self.api_key = os.getenv("GROQ_API_KEY")
        
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        self.client = Groq(api_key=self.api_key)
        self.conversation_history = []
        self.tasks = []
        self.preferences = {}
        self.data_dir = os.path.join(script_dir, "data")
        
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        self.load_session()

    def respond(self, user_input):
        try:
            self.conversation_history.append({
                "role": "user",
                "content": user_input,
                "timestamp": datetime.now().isoformat()
            })
            
            system_prompt = f"""You are {self.name}, a helpful personal AI assistant.
            User's name: {self.user_name}
            Current tasks: {len(self.tasks)} pending
            
            Be conversational, helpful, and remember our conversation context.
            If asked about tasks, refer to the task management system.
            """
            
            messages = [{"role": "system", "content": system_prompt}]
            
            for msg in self.conversation_history[-10:]:
                if msg["role"] in ["user", "assistant"]:
                    messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })
            
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            assistant_response = response.choices[0].message.content
            
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_response,
                "timestamp": datetime.now().isoformat()
            })
            
            self.save_session()
            return assistant_response
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def add_task(self, task_description, priority="medium"):
        task = {
            "id": len(self.tasks) + 1,
            "description": task_description,
            "priority": priority,
            "status": "pending",
            "created": datetime.now().isoformat(),
            "completed": None
        }
        self.tasks.append(task)
        self.save_session()
        return f"Task added: {task_description}"

    def get_tasks(self, status="pending"):
        filtered_tasks = [task for task in self.tasks if task["status"] == status]
        if not filtered_tasks:
            return f"No {status} tasks found."
        
        task_list = []
        for task in filtered_tasks:
            task_list.append(f"• [{task['id']}] {task['description']} ({task['priority']})")
        
        return "\n".join(task_list)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                task["completed"] = datetime.now().isoformat()
                self.save_session()
                return f"Task completed: {task['description']}"
        return "Task not found."

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_session()
        return "Task deleted."

    def set_preference(self, key, value):
        self.preferences[key] = value
        self.save_session()
        return f"Preference set: {key} = {value}"

    def get_conversation_summary(self):
        if not self.conversation_history:
            return "No conversation history yet."
        
        total_messages = len(self.conversation_history)
        user_messages = len([msg for msg in self.conversation_history if msg["role"] == "user"])
        
        return f"Conversation: {user_messages} messages exchanged, {len(self.tasks)} tasks managed"

    def save_session(self):
        session_data = {
            "conversation_history": self.conversation_history,
            "tasks": self.tasks,
            "preferences": self.preferences,
            "last_updated": datetime.now().isoformat()
        }
        
        session_file = os.path.join(self.data_dir, f"{self.user_name}_session.json")
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)

    def load_session(self):
        session_file = os.path.join(self.data_dir, f"{self.user_name}_session.json")
        if os.path.exists(session_file):
            try:
                with open(session_file, 'r') as f:
                    session_data = json.load(f)
                
                self.conversation_history = session_data.get("conversation_history", [])
                self.tasks = session_data.get("tasks", [])
                self.preferences = session_data.get("preferences", {})
            except Exception as e:
                print(f"Error loading session: {e}")

    def clear_session(self):
        self.conversation_history = []
        self.tasks = []
        self.preferences = {}
        self.save_session()
        return "Session cleared."

if __name__ == "__main__":
    assistant = PersonalAssistant()
    
    print(f"🤖 {assistant.name}: Hello! I'm your personal AI assistant.")
    print("Type 'help' for commands or 'quit' to exit.")
    
    while True:
        user_input = input(f"\n{assistant.user_name}: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"🤖 {assistant.name}: Goodbye!")
            break
        elif user_input.lower() == 'help':
            print("""
Commands:
- add task [description] - Add a new task
- show tasks - View pending tasks
- complete task [id] - Mark task as completed
- clear session - Clear all data
- summary - Show conversation summary
            """)
        elif user_input.startswith('add task '):
            task_desc = user_input[9:]
            print(f"🤖 {assistant.name}: {assistant.add_task(task_desc)}")
        elif user_input == 'show tasks':
            print(f"🤖 {assistant.name}: {assistant.get_tasks()}")
        elif user_input.startswith('complete task '):
            try:
                task_id = int(user_input[14:])
                print(f"🤖 {assistant.name}: {assistant.complete_task(task_id)}")
            except ValueError:
                print(f"🤖 {assistant.name}: Please provide a valid task ID.")
        elif user_input == 'clear session':
            print(f"🤖 {assistant.name}: {assistant.clear_session()}")
        elif user_input == 'summary':
            print(f"🤖 {assistant.name}: {assistant.get_conversation_summary()}")
        else:
            response = assistant.respond(user_input)
            print(f"🤖 {assistant.name}: {response}")
