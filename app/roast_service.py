import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API with your key
genai.configure(api_key=GEMINI_API_KEY)

def generate_roast(message):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # You can change to "gemini-1.5-pro" or "gemini-2"
        response = model.generate_content(f"Roast this: {message}")

        if response and response.text:
            return response.text
        return "No roast generated."
    except Exception as e:
        return f"Error generating roast: {str(e)}"
