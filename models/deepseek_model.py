import os
from openai import OpenAI
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()


class DeepSeekAPI:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

    def generate_text(self, prompt: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                model="deepseek/deepseek-chat:free",
                messages=[{"role": "user", "content": prompt}],
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def stream_text(self, prompt: str):
        try:
            response = self.client.chat.completions.create(
                model="deepseek/deepseek-chat:free",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
            for chunk in response:
                yield chunk.choices[0].delta.content if chunk.choices else ""
        except Exception as e:
            yield f"Error: {str(e)}"
