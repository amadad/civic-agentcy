import json
import os
import requests
from langchain.tools import BaseTool, tool
from exa_py import Exa

class SearchTools():
    def __init__(self):
        self.serper_api_key = os.environ['SERPER_API_KEY']
        self.serpapi_api_key = os.environ['SERPAPI_API_KEY']
        self.ydc_api_key = os.getenv("YOU_API_KEY")
        self.exa_api_key = os.environ["EXA_API_KEY"]
        self.exa = Exa(api_key=self.exa_api_key)

    @tool("Basic search internet")
    def basic_search(self, query, n_results=5):
        """Useful to search the internet with Serper about a given topic and return relevant results"""
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': self.serper_api_key,
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['organic']
        string = []
        for result in results[:n_results]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", "\n-----------------"
                ]))
            except KeyError:
                continue

        content = '\n'.join(string)
        return f"\nSearch result: {content}\n"

    @tool("Search internet")
    def search_internet(self, query):
        """Useful to search the internet with Serpapi about a given topic and return relevant results"""
        self.url = "https://serpapi.com/search"
        payload = {"q": query, "api_key": self.serpapi_api_key, "num": 4}
        response = requests.get(self.url, params=payload)
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

    @tool("TrendingNews")
    def exa_search(self, query, include_domains=None, start_published_date=None):
        """Search for a webpage based on the query."""
        return self.exa.search(
            query,
            use_autoprompt=True,
            num_results=5,
            include_domains=include_domains,
            start_published_date=start_published_date,
        )

    @tool("Similar Webpages")  
    def find_similar(url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return self.exa.find_similar(url, num_results=5)

    @tool("SiteContents")
    def get_contents(self, ids: list[str]):
        """Get the contents of a webpage."""
        return self.exa.get_contents(ids)
