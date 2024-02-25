# OpenAI API Key
from AIResponseProcessor import AIResponseProcessor

openai_api_key = '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'

# Snowflake credentials structured as a dictionary for easier passing
snowflake_credentials = {
    'user': 'your_username',
    'password': 'your_password',
    'account': 'your_account_id',
    'warehouse': 'your_warehouse',
    'database': 'your_database',
    'schema': 'your_schema'
}

# Snowflake table name where data will be stored
table_name = 'your_table_name'

# Define the path to your file
file_path = 'emailtext.txt'
file_path_prompt = 'prompt.txt'

# Initialize an empty string for text_to_process
text_to_process = ''
prompt = ''

# Open the file and read its contents
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text_to_process = file.read().strip()
except FileNotFoundError:
    print(f"The file {file_path} was not found.")

try:
    with open(file_path_prompt, 'r', encoding='utf-8') as file:
        prompt = file.read().strip()
except FileNotFoundError:
    print(f"The file {file_path_prompt} was not found.")

# print(prompt)
# Use text_to_process as needed


# Create an instance of AIResponseProcessor
processor = AIResponseProcessor(openai_api_key, snowflake_credentials, table_name)

# Process the request
response = processor.process_request_image(prompt, text_to_process)

print(f"Response from AI for image: \"{response}\"")

response = processor.process_request_text(prompt, text_to_process)

print(f"Response from AI for text: \"{response}\"")
