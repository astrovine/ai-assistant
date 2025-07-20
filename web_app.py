

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from personal_assistant import PersonalAssistant

app = Flask(__name__)
CORS(app)
app.secret_key = 'your-secret-key-here'

assistant = PersonalAssistant(name="Dhee", user_name="User")

@app.route('/')
def home():
    """Main page route - serves the chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages from the frontend"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        response = assistant.respond(user_message)
        
        return jsonify({
            'response': response,
            'timestamp': datetime.now().isoformat(),
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        tasks_text = assistant.get_tasks()
        tasks_list = []
        
        for task in assistant.tasks:
            tasks_list.append({
                'id': task['id'],
                'description': task['description'],
                'priority': task['priority'],
                'status': task['status'],
                'created_at': task['created_at']
            })
        
        return jsonify({
            'tasks': tasks_list,
            'tasks_text': tasks_text,
            'count': len(tasks_list)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """Add a new task"""
    try:
        data = request.get_json()
        task_description = data.get('description', '').strip()
        priority = data.get('priority', 'medium')
        
        if not task_description:
            return jsonify({'error': 'Task description required'}), 400
        
        result = assistant.add_task(task_description, priority)
        
        return jsonify({
            'message': result,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    """Mark a task as completed"""
    try:
        result = assistant.complete_task(task_id)
        return jsonify({
            'message': result,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/session/save', methods=['POST'])
def save_session():
    """Save current session"""
    try:
        data = request.get_json()
        filename = data.get('filename', None)
        
        result = assistant.save_session(filename)
        
        return jsonify({
            'message': result,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/session/clear', methods=['POST'])
def clear_session():
    """Clear conversation history"""
    try:
        result = assistant.clear_history()
        
        return jsonify({
            'message': result,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/summary', methods=['GET'])
def get_summary():
    """Get conversation summary"""
    try:
        summary = assistant.get_conversation_summary()
        
        return jsonify({
            'summary': summary,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    try:
        history = assistant.get_history()
        
        formatted_history = []
        for msg in history:
            if msg['role'] != 'system':
                formatted_history.append({
                    'role': msg['role'],
                    'content': msg['content'],
                    'timestamp': msg.get('timestamp', '')
                })
        
        return jsonify({
            'history': formatted_history,
            'count': len(formatted_history)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🌐 Starting Personal AI Assistant Web Interface...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("💡 Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
