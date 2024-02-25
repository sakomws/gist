import requests

# Define the API URL
url = "https://api.twelvelabs.io/v1.2/search"

user_interest = "text to video generation"
search_index = "65da909babd7318d014732e5"
api_key = "tlk_1FAJK0E1FF0HQ82H2MYYJ1VWWKE7"

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

print(joined_text)

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

joined_text: {{joined_text}}

expected result:
Give me a json object with prompt and snippet
'''

responses = {
  "search_pool": {
    "total_count": 3,
    "total_duration": 3385,
    "index_id": "65da909babd7318d014732e5"
  },
  "data": [
    {
      "clips": [
        {
          "score": 84.04,
          "start": 378.829,
          "end": 383.6,
          "metadata": [
            {
              "type": "conversation",
              "text": "And so you said like the Apple Vision Pro being a video feed actually reduces the technical challenge."
            }
          ],
          "video_id": "65da9c5d48db9fa780cb426b",
          "confidence": "high",
          "thumbnail_url": "https://project-one-thumbnail.s3.us-west-2.amazonaws.com/65da9c5d48db9fa780cb426b/379.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYRWJPOVHXE5SJ77T%2F20240225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240225T024402Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=be697f3e45560d55ce7ec6620c59a82a9fce751e3e64f7beb77be44c781ca530"
        },
        {
          "score": 84.73,
          "start": 556.4,
          "end": 564.539,
          "metadata": [
            {
              "type": "conversation",
              "text": "Yeah, that's exactly as you were talking about what this is and that springs to mind like light R plus a bunch of cameras and processing the video feed. Yeah."
            }
          ],
          "video_id": "65da9c5d48db9fa780cb426b",
          "confidence": "high",
          "thumbnail_url": "https://project-one-thumbnail.s3.us-west-2.amazonaws.com/65da9c5d48db9fa780cb426b/557.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYRWJPOVHXE5SJ77T%2F20240225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240225T024402Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=d01a418df719f9e694e4b116a263c24de7dbb169d3c2e3f6322884252eb7470a"
        },
        {
          "score": 83.24,
          "start": 804.739,
          "end": 817.969,
          "metadata": [
            {
              "type": "conversation",
              "text": "And uh one of the things you notice is so much of it is about eye tracking and communicating, communicating information with depth and space. And"
            }
          ],
          "video_id": "65da9c5d48db9fa780cb426b",
          "confidence": "high",
          "thumbnail_url": "https://project-one-thumbnail.s3.us-west-2.amazonaws.com/65da9c5d48db9fa780cb426b/805.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYRWJPOVHXE5SJ77T%2F20240225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240225T024402Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=455f74d25ba9828ea2e61a9ef9e86d10b0049d5b4372807c0fe9232d37f0e11d"
        }
      ],
      "id": "65da9c5d48db9fa780cb426b"
    },
    {
      "clips": [
        {
          "score": 83.75,
          "start": 738.005,
          "end": 744.674,
          "metadata": [
            {
              "type": "conversation",
              "text": "And then at the end of this research, it'll offer to generate a knowledge graph around all this. So this is something I was like working on."
            }
          ],
          "video_id": "65da9a7448db9fa780cb4269",
          "confidence": "high",
          "thumbnail_url": "https://project-one-thumbnail.s3.us-west-2.amazonaws.com/65da9a7448db9fa780cb4269/739.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYRWJPOVHXE5SJ77T%2F20240225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240225T024402Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=94f7fd7f4360edbcae0143bb64cfc681e606e943ee4b0e086255c6c06d8f9eda"
        },
        {
          "score": 84.24,
          "start": 800.609,
          "end": 818.45,
          "metadata": [
            {
              "type": "conversation",
              "text": " So this is all based on a pretty long conversation. So, but uh my question is like for each of like, is it interactive at all? No, that's the thing. So right now the graph isn't interactive but the way it's generated, it's actually taking into account like a layered structure of what's the, what's the main topic?"
            }
          ],
          "video_id": "65da9a7448db9fa780cb4269",
          "confidence": "high",
          "thumbnail_url": "https://project-one-thumbnail.s3.us-west-2.amazonaws.com/65da9a7448db9fa780cb4269/801.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYRWJPOVHXE5SJ77T%2F20240225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240225T024402Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=aea817c86b1ef5d7bbdd354a8bee13a0a9f40a963e15bcedb37bd9e952068f06"
        }
      ],
      "id": "65da9a7448db9fa780cb4269"
    }
  ],
  "page_info": {
    "limit_per_page": 10,
    "total_results": 2,
    "page_expired_at": "2024-02-25T02:44:02Z",
    "total_inner_matches": 5
  }
}

print(responses['data'])