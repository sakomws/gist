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

    def generate_and_save_image(self, prompt, save_path):
        """
        Generates an image based on the given prompt and saves it to the specified path.

        :param prompt: Text description to generate the image.
        :param save_path: Local directory path to save the generated image.
        """
        try:
            client = OpenAI(
                # This is the default and can be omitted
                api_key=self.api_key,
            )

            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024",
                response_format="url"
            )

            # print(response)
            # Extract the URL of the generated image from the response
            return response.data[0].url

        except Exception as e:
            print(f"Error in generating or saving image: {e}")
