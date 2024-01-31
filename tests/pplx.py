import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
topic = input("Please enter your public policy for research: ")

def parse_response(response_text):
    try:
        response_json = json.loads(response_text)
        if 'choices' not in response_json:
            return "Sorry, the response is not in the expected format."

        parsed_content = []
        for choice in response_json['choices']:
            message = choice.get('message', {})
            content = message.get('content', '')
            if content:
                parsed_content.append(content)

        return '\n-----------------\n'.join(parsed_content)

    except json.JSONDecodeError:
        return "Error parsing the response."

# API request setup
url = "https://api.perplexity.ai/chat/completions"
payload = {
    "model": "pplx-7b-online",
    "messages": [
        {
            "role": "system",
            "content": "You are an artificial intelligence assistant and you need to engage in a helpful, detailed, polite conversation with a user."
        },
        {
            "role": "user",
            "content": f"Provide a comprehensive political analysis of {topic}. Include discussion on legal implications, economic benefits and challenges, social effects, and health-related consequences. Please consider various perspectives, including those of lawmakers, health professionals, economists, and the general public. Summarize the current state of legalization in different regions, highlighting key policies, debates, and public opinion trends. Include citations and sources."
        }
    ]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {perplexity_api_key}"
}

# Making the API request
response = requests.post(url, json=payload, headers=headers)

# Parsing and printing the response
parsed_response = parse_response(response.text)
print(parsed_response)
