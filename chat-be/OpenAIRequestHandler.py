import openai
from openai import OpenAI


class OpenAIRequestHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def send_text(self, text):
        try:
            client = OpenAI(
                # This is the default and can be omitted
                api_key=self.api_key,
            )

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": text,
                    }
                ],
                model="gpt-4",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Error while sending text to OpenAI: {e}")
            return None
