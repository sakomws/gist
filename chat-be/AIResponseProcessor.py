from OpenAIRequestHandler import OpenAIRequestHandler


class AIResponseProcessor:
    def __init__(self, openai_api_key, snowflake_credentials, table_name):
        """
        Initializes the AI response processor with OpenAI and Snowflake credentials.

        :param openai_api_key: API key for OpenAI.
        :param snowflake_credentials: A dictionary containing Snowflake connection details.
        :param table_name: The name of the Snowflake table where data will be stored.
        """
        self.openai_handler = OpenAIRequestHandler(openai_api_key)
        # self.snowflake_store = SnowflakeDataStore(**snowflake_credentials)
        # self.table_name = table_name

    def process_request_text(self, prompt, text):
        """
        Sends a text request to OpenAI, receives a response, and stores both in Snowflake.

        :param text: The text to send to OpenAI for processing.
        """
        # Send text to OpenAI and get response
        aitext = prompt + " : " + text
        return self.openai_handler.send_text(aitext)

    def process_request_image(self, prompt, text, save_path='./images'):
        """
        Sends a text request to OpenAI, receives a response, and stores both in Snowflake.

        :param prompt:
        :param save_path:
        :param text: The text to send to OpenAI for processing.
        """
        # Send text to OpenAI and get response
        aitext = prompt + " : " + text
        return self.openai_handler.generate_and_save_image(aitext, save_path)
