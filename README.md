# 🤖 Dhee - Personal AI Assistant (v1.0)

> A modern, conversational AI assistant with memory, task management, and a sleek dark-themed web interface.

## 🚀 Overview

Dhee is a personal AI assistant that combines **Groq's free API** with a responsive web interface. Built as a learning project with GitHub Copilot assistance for rapid prototyping, this v1 focuses on core functionality that I'll iterate and improve over time.onal AI Assistant (v1.0)

> A modern, conversational AI assistant built with **GitHub Copilot** for rapid prototyping and development.

## 🚀 Overview

Dhee is a personal AI assistant that combines the power of **Groq's free API** with a sleek dark-themed web interface.

**⚡ Built with GitHub Copilot for:**
- Fast prototyping and code generation
- Intelligent code suggestions and completions
- Rapid iteration and feature development
- Best practices implementation

## ✨ Features

- 💬 **Conversational AI** - Natural language interactions powered by Groq
- 🧠 **Memory System** - Maintains conversation context across sessions
- 📋 **Task Management** - Create, track, and manage tasks
- 🌙 **Dark Theme UI** - Modern glassmorphism design with emerald gradients
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile
- 🔄 **Real-time Chat** - Instant responses with typing indicators
- 💾 **Session Persistence** - Remembers conversations and preferences

## 🛠 Tech Stack

### Backend
- **Python 3.12** - Core language
- **Flask** - Web framework
- **Groq API** - AI language model (free tier)
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first styling
- **Alpine.js** - Reactive JavaScript framework
- **Font Awesome** - Icon library

### Development Tools
- **Git** - Version control
- **Virtual Environment** - Python dependency isolation

## 📁 Project Structure

```
AI-AGENT/
├── venv/                          # Main application directory
│   ├── personal_assistant.py     # Core AI assistant class (420+ lines)
│   ├── web_app.py                # Flask backend (177+ lines)
│   ├── multi_agent.py            # API testing utilities
│   ├── templates/
│   │   └── index.html            # Web interface (532+ lines)
│   └── data/                     # Session and task storage
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables template
└── README.md                     # This file
```

## ⚡ Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/astrovine/ai-assistant.git
cd ai-assistant
```

### 2. Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies (add to requirements.txt first)
pip install flask flask-cors groq python-dotenv
```

### 3. API Configuration
```bash
# Copy environment template
cp .env.example .env

# Get free Groq API key from: https://console.groq.com
# Add to .env file:
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the Assistant
```bash
cd venv
python web_app.py
```

Visit `http://localhost:5000` to start chatting with Dhee!

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=optional_openai_key
HUGGINGFACE_API_KEY=optional_hf_key
```

### Customization
- **Assistant Name**: Edit `name="Dhee"` in `web_app.py`
- **Theme Colors**: Modify Tailwind config in `index.html`
- **AI Model**: Change model in `personal_assistant.py` (line ~80)

## 🎯 Core Components

### PersonalAssistant Class
- **Memory Management**: Conversation history and context
- **Task System**: CRUD operations for task management
- **API Integration**: Groq client with error handling
- **Session Persistence**: File-based data storage

### Web Interface
- **Responsive Design**: Mobile-first approach
- **Dark Theme**: Elegant glassmorphism effects
- **Real-time Chat**: Smooth user experience
- **Task Dashboard**: Interactive task management

## 🚧 Development Notes

This is **version 1.0** - a foundational implementation focusing on core functionality. Future iterations will include:

- Database integration (SQLite/PostgreSQL)
- User authentication system
- Advanced AI capabilities
- Plugin architecture
- Mobile app development
- Production deployment optimization

## 🔄 API Testing

Test different AI providers:
```bash
cd venv
python multi_agent.py
```

Supports:
- ✅ **Groq** (Free, fast, recommended)
- ⚠️ **OpenAI** (Paid, high quality)
- ⚠️ **Hugging Face** (Free, limited)

## 📈 Performance

- **Response Time**: ~1-3 seconds (Groq API)
- **Memory Usage**: ~50MB Python process
- **Storage**: Minimal (JSON files)
- **Scalability**: Single-user focused (v1)

## 🐛 Known Issues (v1)

- No user authentication
- File-based storage (not scalable)
- Basic error handling
- Limited conversation export
- No conversation branching

## 🚀 Deployment

### Local Development
```bash
python web_app.py
# Access: http://localhost:5000
```

### Production (Future)
- Containerization with Docker
- Cloud deployment (AWS/Heroku)
- Database migration
- SSL/HTTPS setup

## 📄 License

MIT License - See LICENSE file for details.

## 🙏 Acknowledgments

- **Groq** - For providing free, fast AI inference
- **Tailwind CSS** - For beautiful, responsive design
- **Flask Community** - For excellent documentation

---

**Built by [@astrovine](https://github.com/astrovine) | v1.0 - More iterations coming soon!**
