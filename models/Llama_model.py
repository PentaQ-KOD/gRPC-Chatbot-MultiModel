from together import Together


class LlamaModelAPI:
    def __init__(self):
        self.client = Together()

    def generate_text(self, prompt: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                messages=[{"role": "user", "content": prompt}],
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def stream_text(self, prompt: str):
        try:
            response = self.client.chat.completions.create(
                model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
            for chunk in response:
                yield chunk.choices[0].delta.content if chunk.choices else ""
        except Exception as e:
            yield f"Error: {str(e)}"


# Compare this snippet from models/Llama_model.py:
# from together import Together
