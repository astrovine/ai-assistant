#!/usr/bin/env python3

print("🔍 Starting Agent Test...")

try:
    import os
    print("✅ os imported")
    
    from dotenv import load_dotenv
    print("✅ dotenv imported")
    
    from groq import Groq
    print("✅ Groq imported")
    
    # Load environment
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, '.env')
    load_dotenv(env_path)
    print(f"✅ Environment loaded from: {env_path}")
    
    # Get API key
    groq_api_key = os.getenv("GROQ_API_KEY")
    print(f"✅ API Key found: {'Yes' if groq_api_key else 'No'}")
    
    if groq_api_key:
        client = Groq(api_key=groq_api_key)
        print("✅ Groq client created")
        
        # Test API call
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=50
        )
        print(f"✅ API Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("🏁 Test completed!")
