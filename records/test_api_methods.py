import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the environment variable for the API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def list_available_models():
    try:
        # List available models and print them
        models = list(genai.list_models())  # Convert generator to list
        print("Available Models:")
        for model in models:
            print(model)
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_available_models()
