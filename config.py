import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Example of how to use API keys securely
def get_api_key(service_name):
    """
    Safely retrieve API keys from environment variables
    
    Args:
        service_name (str): Name of the service (e.g., 'OPENAI', 'GOOGLE')
    
    Returns:
        str: API key or None if not found
    """
    key = os.getenv(f"{service_name}_API_KEY")
    if not key:
        print(f"Warning: {service_name}_API_KEY not found in environment variables")
    return key

# Example usage
if __name__ == "__main__":
    # Get API keys
    openai_key = get_api_key("OPENAI")
    google_key = get_api_key("GOOGLE")
    
    print("Environment loaded successfully!")
    print(f"OpenAI API Key: {'✓ Found' if openai_key else '✗ Not found'}")
    print(f"Google API Key: {'✓ Found' if google_key else '✗ Not found'}")
