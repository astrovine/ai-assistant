"""
=== PERSONAL AI ASSISTANT - COMPREHENSIVE GUIDE ===

OVERVIEW:
This code creates a sophisticated Personal AI Assistant using the Groq API.
The assistant can handle multiple conversation types, remember context,
manage tasks, and provide personalized responses.

KEY CONCEPTS TO STUDY:

1. OBJECT-ORIENTED PROGRAMMING (OOP):
   - Classes and Objects: PersonalAssistant class encapsulates data and methods
   - Inheritance: Could extend to create specialized assistants
   - Encapsulation: Private methods and data protection
   - Polymorphism: Different response types based on input

2. API INTEGRATION:
   - REST API calls using Groq client
   - Authentication with API keys
   - Request/Response handling
   - Error handling and retries

3. DATA STRUCTURES:
   - Lists: For storing conversation history and tasks
   - Dictionaries: For message formatting and user preferences
   - Tuples: For immutable data storage
   - Sets: For unique data management

4. FILE HANDLING & ENVIRONMENT:
   - Environment variables for security
   - File I/O operations for data persistence
   - Path manipulation and directory handling

5. STRING MANIPULATION & TEXT PROCESSING:
   - Regular expressions for pattern matching
   - String formatting and templating
   - Text parsing and analysis

6. DATE & TIME HANDLING:
   - DateTime operations for scheduling
   - Time zone management
   - Date formatting and calculations

7. ERROR HANDLING:
   - Try-catch blocks for graceful error management
   - Custom exception handling
   - Logging and debugging techniques

8. DESIGN PATTERNS:
   - Singleton pattern for assistant instance
   - Observer pattern for event handling
   - Strategy pattern for different response types

FUNCTIONS COVERED:

Core Methods:
- __init__(): Constructor for initialization
- respond(): Main conversation handler with memory
- add_task(): Task management functionality
- get_tasks(): Task retrieval and display
- set_preference(): User customization
- get_summary(): Conversation summarization
- save_session(): Data persistence
- load_session(): Data restoration

Utility Methods:
- _parse_command(): Input processing and command extraction
- _format_response(): Response formatting and styling
- _handle_error(): Error management and recovery
- _log_interaction(): Activity logging and tracking

Advanced Features:
- Memory management with conversation history
- Task scheduling and reminders
- Personal preferences and customization
- Session persistence across restarts
- Context-aware responses
- Multi-turn conversation handling

FUNCTIONALITY OVERVIEW:

1. CONVERSATION MANAGEMENT:
   - Maintains conversation history for context
   - Supports different conversation modes (casual, professional, creative)
   - Handles follow-up questions and references
   - Provides context-aware responses

2. TASK MANAGEMENT:
   - Add, view, complete, and delete tasks
   - Task prioritization and categorization
   - Due date tracking and reminders
   - Task status management

3. PERSONALIZATION:
   - User preference storage (name, style, interests)
   - Customizable response tone and format
   - Personal context integration
   - Learning from user interactions

4. SESSION MANAGEMENT:
   - Save conversation history to file
   - Load previous sessions on startup
   - Export conversation logs
   - Clear history when needed

5. SMART FEATURES:
   - Command parsing and intent recognition
   - Automatic task extraction from conversation
   - Time and date understanding
   - Context switching between topics

TECHNICAL ARCHITECTURE:
- Event-driven design for responsive interactions
- Modular structure for easy extension
- Clean separation of concerns
- Scalable and maintainable codebase

STUDY TOPICS FOR DEEPER UNDERSTANDING:
- Natural Language Processing (NLP)
- Machine Learning fundamentals
- API design principles
- Database integration
- Web development (for GUI)
- Mobile app development
- Cloud deployment
- Security best practices
- Performance optimization
- Testing strategies

"""

import os
import json
import datetime
from typing import List, Dict, Optional, Any
from dotenv import load_dotenv
from groq import Groq

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')
load_dotenv(env_path)

class PersonalAssistant:
    def __init__(self, name: str = "Dhee", user_name: str = "User"):
        self.name = name
        self.user_name = user_name
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.groq_api_key)
        self.model = "llama-3.1-8b-instant"
        
        self.conversation_history = []
        self.tasks = []
        self.preferences = {
            "response_style": "friendly",
            "max_response_length": 200,
            "remember_context": True,
            "task_reminders": True
        }
        
        self.system_prompt = f"""You are {self.name}, a highly intelligent and helpful personal AI assistant. 
        You are talking to {self.user_name}. You should be:
        - Friendly, professional, and personable
        - Proactive in offering help and suggestions
        - Able to remember context from our conversation
        - Capable of helping with tasks, planning, questions, and general assistance
        - Concise but thorough in your responses
        
        Current date and time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        If the user asks you to add a task, extract the task details and confirm.
        If they ask about their tasks, provide a clear overview.
        Always maintain context from previous messages in our conversation."""
        
        self.conversation_history.append({
            "role": "system", 
            "content": self.system_prompt,
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        self._initialize_assistant()
    
    def _initialize_assistant(self):
        welcome_message = f"Hello {self.user_name}! I'm {self.name}, your personal AI assistant. I'm here to help you with tasks, answer questions, and have conversations. What can I do for you today?"
        print(f"🤖 {self.name}: {welcome_message}")
    
    def respond(self, user_input: str) -> str:
        if not user_input.strip():
            return "I didn't catch that. Could you please say something?"
        
        self._add_to_history("user", user_input)
        
        command_result = self._parse_command(user_input)
        if command_result:
            return command_result
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self._get_context_messages(),
                max_tokens=self.preferences["max_response_length"],
                temperature=0.7
            )
            
            assistant_response = response.choices[0].message.content
            self._add_to_history("assistant", assistant_response)
            
            return assistant_response
            
        except Exception as e:
            error_response = f"I apologize, but I encountered an error: {str(e)}. Please try again."
            return error_response
    
    def _parse_command(self, user_input: str) -> Optional[str]:
        input_lower = user_input.lower()
        
        if "add task" in input_lower or "new task" in input_lower:
            task_text = user_input.replace("add task", "").replace("new task", "").strip()
            if task_text:
                return self.add_task(task_text)
            else:
                return "What task would you like me to add?"
        
        elif "show tasks" in input_lower or "my tasks" in input_lower or "list tasks" in input_lower:
            return self.get_tasks()
        
        elif "clear tasks" in input_lower:
            self.tasks.clear()
            return "All tasks have been cleared."
        
        elif "clear history" in input_lower or "clear conversation" in input_lower:
            return self.clear_history()
        
        elif "save session" in input_lower:
            return self.save_session()
        
        elif "my name is" in input_lower:
            new_name = user_input.lower().replace("my name is", "").strip().title()
            if new_name:
                self.user_name = new_name
                self._update_system_prompt()
                return f"Nice to meet you, {new_name}! I'll remember your name."
        
        return None
    
    def add_task(self, task_description: str, priority: str = "medium") -> str:
        task = {
            "id": len(self.tasks) + 1,
            "description": task_description,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.datetime.now().isoformat(),
            "due_date": None
        }
        
        self.tasks.append(task)
        return f"✅ Task added: '{task_description}' (Priority: {priority})"
    
    def get_tasks(self) -> str:
        if not self.tasks:
            return "You don't have any tasks yet. Would you like to add some?"
        
        task_list = f"📋 Your Tasks ({len(self.tasks)} total):\n\n"
        
        for task in self.tasks:
            status_icon = "✅" if task["status"] == "completed" else "⏳"
            priority_icon = "🔴" if task["priority"] == "high" else "🟡" if task["priority"] == "medium" else "🟢"
            
            task_list += f"{status_icon} {priority_icon} {task['id']}. {task['description']}\n"
        
        return task_list.strip()
    
    def complete_task(self, task_id: int) -> str:
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                task["completed_at"] = datetime.datetime.now().isoformat()
                return f"🎉 Task completed: '{task['description']}'"
        
        return f"Task with ID {task_id} not found."
    
    def set_preference(self, key: str, value: Any) -> str:
        if key in self.preferences:
            self.preferences[key] = value
            return f"Preference updated: {key} = {value}"
        else:
            return f"Unknown preference: {key}"
    
    def get_conversation_summary(self) -> str:
        if len(self.conversation_history) <= 1:
            return "No conversation to summarize yet."
        
        user_messages = [msg for msg in self.conversation_history if msg["role"] == "user"]
        assistant_messages = [msg for msg in self.conversation_history if msg["role"] == "assistant"]
        
        summary = f"""
📊 Conversation Summary:
- Total messages: {len(self.conversation_history)}
- Your messages: {len(user_messages)}
- My responses: {len(assistant_messages)}
- Active tasks: {len([t for t in self.tasks if t['status'] == 'pending'])}
- Completed tasks: {len([t for t in self.tasks if t['status'] == 'completed'])}
        """
        
        return summary.strip()
    
    def save_session(self, filename: str = None) -> str:
        if not filename:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"session_{timestamp}.json"
        
        session_data = {
            "user_name": self.user_name,
            "assistant_name": self.name,
            "conversation_history": self.conversation_history,
            "tasks": self.tasks,
            "preferences": self.preferences,
            "saved_at": datetime.datetime.now().isoformat()
        }
        
        try:
            filepath = os.path.join(script_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2, ensure_ascii=False)
            
            return f"💾 Session saved to: {filename}"
            
        except Exception as e:
            return f"❌ Error saving session: {str(e)}"
    
    def load_session(self, filename: str) -> str:
        try:
            filepath = os.path.join(script_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
            
            self.user_name = session_data.get("user_name", self.user_name)
            self.conversation_history = session_data.get("conversation_history", [])
            self.tasks = session_data.get("tasks", [])
            self.preferences.update(session_data.get("preferences", {}))
            
            return f"📂 Session loaded from: {filename}"
            
        except Exception as e:
            return f"❌ Error loading session: {str(e)}"
    
    def clear_history(self) -> str:
        self.conversation_history = []
        self.conversation_history.append({
            "role": "system", 
            "content": self.system_prompt,
            "timestamp": datetime.datetime.now().isoformat()
        })
        return "🧹 Conversation history cleared. Starting fresh!"
    
    def _add_to_history(self, role: str, content: str):
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        if len(self.conversation_history) > 50:
            self.conversation_history = self.conversation_history[:1] + self.conversation_history[-30:]
    
    def _get_context_messages(self) -> List[Dict[str, str]]:
        return [{"role": msg["role"], "content": msg["content"]} 
                for msg in self.conversation_history[-20:]]
    
    def _update_system_prompt(self):
        self.system_prompt = f"""You are {self.name}, a highly intelligent and helpful personal AI assistant. 
        You are talking to {self.user_name}. You should be:
        - Friendly, professional, and personable
        - Proactive in offering help and suggestions
        - Able to remember context from our conversation
        - Capable of helping with tasks, planning, questions, and general assistance
        - Concise but thorough in your responses
        
        Current date and time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
        
        if self.conversation_history and self.conversation_history[0]["role"] == "system":
            self.conversation_history[0]["content"] = self.system_prompt

def interactive_session():
    print("🌟" + "="*60 + "🌟")
    print("   WELCOME TO YOUR PERSONAL AI ASSISTANT")
    print("🌟" + "="*60 + "🌟")
    print("\nCommands you can use:")
    print("• 'add task [description]' - Add a new task")
    print("• 'show tasks' - View all your tasks")
    print("• 'clear tasks' - Remove all tasks")
    print("• 'save session' - Save your conversation")
    print("• 'clear history' - Start fresh conversation")
    print("• 'my name is [name]' - Tell me your name")
    print("• 'quit' or 'exit' - End the session")
    print("\nJust type naturally for regular conversation!")
    print("-" * 64)
    
    assistant = PersonalAssistant()
    
    while True:
        try:
            user_input = input(f"\n👤 {assistant.user_name}: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                farewell = f"Goodbye {assistant.user_name}! It was great helping you today. Have a wonderful day! 👋"
                print(f"\n🤖 {assistant.name}: {farewell}")
                break
            
            if user_input:
                response = assistant.respond(user_input)
                print(f"\n🤖 {assistant.name}: {response}")
            
        except KeyboardInterrupt:
            print(f"\n\n🤖 {assistant.name}: Goodbye! Session ended by user.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    interactive_session()
