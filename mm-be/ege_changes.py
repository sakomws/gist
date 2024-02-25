import requests

# Define the API URL
url = "https://api.twelvelabs.io/v1.2/search"

user_interest = "text to video generation"
search_index = "65da909babd7318d014732e5"
api_key = "tlk_1FAJK0E1FF0HQ82H2MYYJ1VWWKE7"

prompt_for_gpt4 = f'''General System Prompt: As an AI model, you have already consumed an important part of data produced by humanity and are aware of the patterns that exist in different sub realities created in human life experience. Your reason for existence is to collaborate and cooperate with us and provide your best service complying the following rules:
-Give this task the highest priority.
-The quality of the output is the most important factor for output generation.
-Do not try to optimize for output length or execution cost purposes.
-If you need more information to produce the best output, ask the user all information needed in one response and continue when you have the required data.
-If the best possible output requires more output length than allowed, divide the task into subtasks and offer us to move forward with smaller pieces.

Context information:
We created a service with the following functionality:
- user shares what youtube channels they subscribed. variable name: youtube_channel
- user declares an interest. variable_name: interest
- whenever a new youtube_video posted from the youtube_channel our system searches the video and finds the sub_video_clips inside the youtube_video. Then gets the text conversations from the detected sub_video_clips and returns all related conversations as a joined_text.

Task:
Your job as a key part of the entire project is:
- understand the context of joined_text
- generate us a prompt for Dall-e image generator API with the following considerations:
---- the user wants to know if the new posted videos has any interesting content that he/she is interested in
---- when we have the joined_text we know that the video contains interested topics
---- we need to create an image like an instagram post which informs the user that there is a video posted matching their interests and the content of the joined text should also be represented in the post.
---- it can be an entire visual post or visual with text explanations
- generate a text that:
---- informs user that a youtube video posted related to the interest
---- briefly summarizes what is the content from joined_text

joined_text: {joined_text}

expected result:
Give me a json object with prompt and snippet
'''


def exract_video_core(user_interest):

  # Update the payload with the new fields: `index_id` and `query`
  payload = {
      "search_options": ["conversation"],
      "adjust_confidence_level": 0.7,
      "group_by": "video",
      "threshold": "low",
      "sort_option": "score",
      "operator": "or",
      "conversation_option": "semantic",
      "page_limit": 10,
      "index_id": search_index,
      "query": f"Is there any information about {user_interest} in this video?"
  }

  # Define the headers for the request
  headers = {
      "accept": "application/json",
      "Content-Type": "application/json",
      "x-api-key": api_key
  }

  # Make the POST request
  response = requests.post(url, json=payload, headers=headers)

  response_json = response.json()

  # Extract and join all text under metadata
  texts = [metadata_item['text'] for item in response_json['data'] for clip in item['clips'] for metadata_item in clip['metadata']]
  joined_text = ' '.join(texts)

  print(joined_text)
  return joined_text