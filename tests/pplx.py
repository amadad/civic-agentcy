import os

import openai
from dotenv import load_dotenv

load_dotenv()
perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")

topic = input("Please enter your public policy for research: ")

messages = [
    {
        "role": "system",
        "content": (
            "You are an artificial intelligence assistant and you need to "
            "engage in a helpful, detailed, polite conversation with a user."
        ),
    },
    {
        "role": "user",
        "content": (
            "Provide a comprehensive political analysis of {topic} "
            "Include discussion on legal implications, economic benefits and challenges, "
            "social effects, and health-related consequences. "
            "Please consider various perspectives, including those of lawmakers, "
            "health professionals, economists, and the general public. "
            "Summarize the current state of legalization in different regions, "
            "highlighting key policies, debates, and public opinion trends. "
            "Include citations and sources."
        ),
    }
]

response_stream = openai.ChatCompletion.create(
    model="pplx-7b-online",
    messages=messages,
    api_base="https://api.perplexity.ai",
    api_key=perplexity_api_key,
    stream=True,
)

for response in response_stream:
    print(response)