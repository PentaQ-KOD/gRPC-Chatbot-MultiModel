import os
from openai import OpenAI
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ตั้งค่า OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),  # ดึง API Key จาก .env
)

completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="anthropic/claude-3.5-haiku-20241022:beta",
    messages=[{"role": "user", "content": "What is the meaning of life?"}],
)
print(completion.choices[0].message.content)
