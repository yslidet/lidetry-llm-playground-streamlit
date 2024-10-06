import time
from openai import OpenAI
from app.mykey import API_KEY

BASE_URL= "https://api.openai.com/v1"
# BASE_URL= "https://integrate.api.nvidia.com/v1"

client = OpenAI(
    base_url = BASE_URL,
    api_key = API_KEY
)

# print(client)

# AVAILABLE_MODELS = [
#     "google/gemma-2-27b-it",
#     "meta/llama3-70b-instruct",
#     "nvidia/nemotron-4-340b-instruct",
#     "mistralai/mixtral-8x22b-instruct-v0.1",
#     "snowflake/arctic"
# ]

AVAILABLE_MODELS = [
    "gpt-3.5-turbo"
]

def model_output(name, prompt, output_queue):
    try: 
        response = client.chat.completions.create(
            model=name,
            messages=[
                {
                    "role": "user",
                    "content":prompt
                }
            ],
            max_tokens = 150, 
            stream=True
        )
        full_output = ""
        for chuck in response:
            if chuck.choices[0].delta.content is not None:
                chuck_text = chuck.choices[0].delta.content 
                full_output += chuck_text
                output_queue.put((name, full_output))
                time.sleep(0.05) 
    except Exception as e: 
        output_queue.put((name, f"Error: {str(e)}"))