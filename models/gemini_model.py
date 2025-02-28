import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class GeminiAPI:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_text(self, input_text):
        try:
            response = self.model.generate_content(input_text)
            if response and hasattr(response, "text"):
                return response.text
            else:
                print("DEBUG: Empty response from Gemini API")
                return "Error: No response from Gemini API"
        except Exception as e:
            print(f"DEBUG: Gemini API Error - {e}")
            return f"Error: {str(e)}"

    def stream_text(self, input_text):
        try:
            response_stream = self.model.generate_content(input_text, stream=True)
            for chunk in response_stream:
                if hasattr(chunk, "text"):
                    yield chunk.text
        except Exception as e:
            print(f"DEBUG: Gemini Streaming API Error - {e}")
            yield f"Error: {str(e)}"
