import json
import os

import requests
from langchain.tools import tool


class SearchTools():
   def __init__(self):
       self.top_result_to_return = 4
       self.url = "https://serpapi.com/search"
       self.api_key = os.environ['SERPAPI_API_KEY']

   def search_internet(self, query):
       """Useful to search the internet about a given topic and return relevant results"""
       payload = {
           "q": query,
           "api_key": self.api_key,
           "num": self.top_result_to_return
       }
       response = requests.get(self.url, params=payload)
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