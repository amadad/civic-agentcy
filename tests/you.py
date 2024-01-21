import os

import requests
from dotenv import load_dotenv

load_dotenv()
you_api_key = os.getenv("YOU_API_KEY")
topic = input("Please enter your public policy for research: ")

def get_ai_snippets_for_query(query):
    headers = {"X-API-Key": you_api_key}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()

results = get_ai_snippets_for_query(topic)
print(results)