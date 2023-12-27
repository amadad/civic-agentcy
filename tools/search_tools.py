import json
import os

import requests
from langchain.tools import tool


class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet about a given topic and return relevant results"""
        top_result_to_return = 4
        url = "https://serpapi.com/search"
        payload = {
            "q": query,
            "api_key": os.environ['SERPAPI_API_KEY'],
            "num": top_result_to_return
        }
        response = requests.get(url, params=payload)
        results = response.json().get('organic_results', [])
        string = []
        for result in results:
            try:
                string.append('\n'.join([
                    f"Title: {result.get('title')}", 
                    f"Link: {result.get('link')}",
                    f"Snippet: {result.get('snippet')}", 
                    "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)