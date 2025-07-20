"""
DEMO SCRIPT - Personal Assistant Features Showcase
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from personal_assistant import PersonalAssistant

def demonstrate_features():
    print("🚀 PERSONAL ASSISTANT DEMO")
    print("=" * 50)
    
    assistant = PersonalAssistant(name="Divine", user_name="Demo User")
    
    print("\n1. Basic Conversation:")
    response1 = assistant.respond("Hello! How are you today?")
    print(f"Response: {response1}")
    
    print("\n2. Adding Tasks:")
    task_response = assistant.add_task("Buy groceries for the week", "high")
    print(f"Task Added: {task_response}")
    
    task_response2 = assistant.add_task("Call mom", "medium")
    print(f"Task Added: {task_response2}")
    
    print("\n3. Viewing Tasks:")
    tasks = assistant.get_tasks()
    print(f"Tasks:\n{tasks}")
    
    print("\n4. Conversation with Memory:")
    response2 = assistant.respond("What tasks do I have?")
    print(f"Response: {response2}")
    
    print("\n5. Personal Context:")
    response3 = assistant.respond("My name is John")
    print(f"Response: {response3}")
    
    response4 = assistant.respond("What's my name?")
    print(f"Response: {response4}")
    
    print("\n6. Session Summary:")
    summary = assistant.get_conversation_summary()
    print(f"Summary:\n{summary}")
    
    print("\n7. Saving Session:")
    save_result = assistant.save_session("demo_session.json")
    print(f"Save Result: {save_result}")
    
    print("\n✅ Demo completed! The assistant is fully functional.")
    print("\nKey Features Demonstrated:")
    print("• Natural conversation with memory")
    print("• Task management (add, view, track)")
    print("• Personal context awareness")
    print("• Session persistence")
    print("• Command parsing")
    print("• Error handling")

if __name__ == "__main__":
    demonstrate_features()
