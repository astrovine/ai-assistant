import os
from dotenv import load_dotenv

# Load .env file from the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')
load_dotenv(env_path)

def test_groq():
    """Test Groq API (Free and Fast)"""
    try:
        from groq import Groq
        
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env file")
            return False
            
        client = Groq(api_key=api_key)
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Free model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital of France?"}
            ],
            max_tokens=100
        )
        
        print("🦾 Groq Response:")
        print(response.choices[0].message.content)
        return True
        
    except Exception as e:
        print(f"❌ Groq Error: {e}")
        return False

def test_openai():
    """Test OpenAI API"""
    try:
        from openai import OpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("❌ OPENAI_API_KEY not found in .env file")
            return False
            
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital of France?"}
            ]
        )
        
        print("🤖 OpenAI Response:")
        print(response.choices[0].message.content)
        return True
        
    except Exception as e:
        print(f"❌ OpenAI Error: {e}")
        return False

def test_huggingface():
    """Test Hugging Face API"""
    try:
        import requests
        
        api_key = os.getenv("HUGGINGFACE_API_KEY")
        if not api_key:
            print("❌ HUGGINGFACE_API_KEY not found in .env file")
            return False
            
        headers = {"Authorization": f"Bearer {api_key}"}
        
        # Using a free model
        url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
        
        response = requests.post(
            url,
            headers=headers,
            json={"inputs": "What is the capital of France?"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("🤗 Hugging Face Response:")
            print(result)
            return True
        else:
            print(f"❌ Hugging Face Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Hugging Face Error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing AI APIs...\n")
    
    # Test available APIs
    apis_tested = []
    
    if test_groq():
        apis_tested.append("Groq")
    
    if test_openai():
        apis_tested.append("OpenAI")
        
    if test_huggingface():
        apis_tested.append("Hugging Face")
    
    print(f"\n✅ Working APIs: {', '.join(apis_tested) if apis_tested else 'None'}")
    
    if not apis_tested:
        print("\n💡 To get started:")
        print("1. Sign up for Groq (free): https://console.groq.com")
        print("2. Get your API key")
        print("3. Add GROQ_API_KEY=your_key_here to your .env file")
