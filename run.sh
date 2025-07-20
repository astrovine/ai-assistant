#!/bin/bash

echo "🚀 Starting Dhee - Personal AI Assistant"
echo "📦 Setting up Python environment..."

# Check if virtual environment exists
if [ ! -d "env" ]; then
    echo "📋 Creating virtual environment..."
    python3 -m venv env
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source env/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Start the application
echo "🌐 Starting web server..."
cd src
python web_app.py
