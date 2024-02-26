import os
import requests
from langchain.tools import tool

class SearchTools:
    def __init__(self):
        self.serpapi_api_key = os.environ['SERPAPI_API_KEY']

    @tool("Search internet")
    def search_internet(self, query):
        """Useful to search the internet with Serpapi about a given topic and return relevant results"""
        url = "https://serpapi.com/search"
        payload = {"q": query, "api_key": self.serpapi_api_key, "num": 4}
        response = requests.get(url, params=payload)
        return response.json().get('organic_results', [])

    def parse_output(self, output):
        string = []
        for result in output:
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