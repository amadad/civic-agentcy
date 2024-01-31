import json
import os
import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from exa_py import Exa

# Define the SearchTools class
class SearchTools():
    def __init__(self):
        self.top_result_to_return = 4
        self.url = "https://serpapi.com/search"
        self.serpapi_api_key = os.environ['SERPAPI_API_KEY']
        self.serper_api_key = os.environ['SERPER_API_KEY']
        self.ydc_api_key = os.getenv("YOU_API_KEY")
        self.exa_api_key = os.environ["EXA_API_KEY"]
        self.exa = Exa(api_key=self.exa_api_key)

    @tool("Search internet")
    def search_internet(self, query):
        """Useful to search the internet with Serpapi about a given topic and return relevant results"""
        payload = {
            "q": query,
            "api_key": self.serpapi_api_key,
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

    @tool("Search instagram")
    def search_instagram(self, query):
        """Useful to search for Instagram posts about a given topic and return relevant results."""
        query = f"site:instagram.com {query}"
        return self.basic_search(query)

    @tool("YDC AI Snippets")
    def get_ai_snippets(self, query):
        """Useful to search for AI-generated snippets about a given topic and return relevant results."""
        headers = {"X-API-Key": self.ydc_api_key}
        params = {"query": query}
        response = requests.get("https://api.ydc-index.io/search", params=params, headers=headers)
        return response.json()

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
    def find_similar(self, url: str):
        """Search for webpages similar to a given URL."""
        return self.exa.find_similar(url, num_results=5)

    @tool("SiteContents")
    def get_contents(self, ids: list[str]):
        """Get the contents of a webpage."""
        return self.exa.get_contents(ids)

    @tool("Perplexity Search")
    def perplexity_search(self, topic):
        """Perform a comprehensive political analysis using Perplexity AI."""
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are an artificial intelligence assistant."
                },
                {
                    "role": "user",
                    "content": (
                        f"Provide a comprehensive political analysis of {topic}."
                    )
                }
            ]
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.perplexity_api_key}"
        }
        response = requests.post(f"{self.perplexity_api_base}/chat/completions",
                                 json=payload, headers=headers)
        return self.parse_response(response.text)

    def parse_response(self, response_text):
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

# Custom Tool for Search Internet
class SearchInternetTool(BaseTool):
    def __init__(self, search_tools):
        self.search_tools = search_tools

    @tool("Run Search Internet Tool")
    def run(self, input_data):
        query = input_data.get("query")
        return self.search_tools.search_internet(query)

    def parse_output(self, output):
        return output

# Define other custom tools similarly...

# Initialize SearchTools
search_tools_instance = SearchTools()

# Initialize each custom tool with the SearchTools instance
search_internet_tool = SearchInternetTool(search_tools_instance)
# ... Initialize other custom tools similarly ...

# Define the Policy Analyst Agent
policy_analyst = Agent(
    # ... [Agent setup as before] ...
    tools=[
        search_internet_tool,
        # ... other custom tool instances ...
    ],
    # ... [remaining Agent configuration] ...
)
