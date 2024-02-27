import json
import os
import requests
from openai import OpenAI
from crewai_tools import tool

@tool("Basic Search Internet")
def basic_search(query: str, n_results: int = 5) -> str:
    """
    Searches the internet with Serper about a given topic and returns relevant results.
    """
    serper_api_key = os.getenv('SERPER_API_KEY')
    if not serper_api_key:
        raise ValueError("SERPER_API_KEY environment variable not set")

    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': serper_api_key,
        'content-type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    results = response.json()['organic']
    string = [f"Title: {result['title']}\nLink: {result['link']}\nSnippet: {result['snippet']}\n-----------------" for result in results[:n_results] if 'title' in result and 'link' in result and 'snippet' in result]

    content = '\n'.join(string)
    return f"\nSearch result: {content}\n"


@tool("Search Internet with Serpapi")
def search_internet(query: str) -> str:
    """
    Searches the internet with Serpapi about a given topic and returns relevant results.
    """
    serpapi_api_key = os.getenv('SERPAPI_API_KEY')
    if not serpapi_api_key:
        raise ValueError("SERPAPI_API_KEY environment variable not set")

    url = "https://serpapi.com/search"
    payload = {"q": query, "api_key": serpapi_api_key, "num": 4}
    response = requests.get(url, params=payload)
    results = response.json().get('organic_results', [])
    
    content = [f"Title: {result.get('title')}\nLink: {result.get('link')}\nSnippet: {result.get('snippet')}\n-----------------" for result in results if result.get('title') and result.get('link') and result.get('snippet')]

    return '\n'.join(content)


@tool("Perplexity Search Tool")
def perplexity_search(user_query: str) -> str:
    """
    This tool uses the OpenAI API to fetch information on a specific topic.
    It's designed to provide AI-generated responses based on the given query,
    leveraging the Perplexity API for in-depth analysis and insights. 
    """
    api_key = os.getenv("PERPLEXITY_API_KEY")    
    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")
    
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
            "content": user_query,
        },
    ]

    try:
        response = client.chat.completions.create(
            model="sonar-medium-online",
            messages=messages,
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

@tool("AI Snippets Search")
def you_search(query: str) -> str:
    """
    Searches for AI-generated snippets based on a given query using the YDC Index API.
    This tool fetches and returns AI-generated content snippets relevant to the query.
    """
    ydc_api_key = os.getenv('YDC_API_KEY')
    if not ydc_api_key:
        raise ValueError("YDC_API_KEY environment variable not set")
    
    headers = {"X-API-Key": ydc_api_key}
    params = {"query": query}
    response = requests.get(
        "https://api.ydc-index.io/search",
        params=params,
        headers=headers,
    )
    try:
        results = response.json()
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        return "Failed to decode JSON response."

    # Formatting the results for readability or further processing
    formatted_results = '\n'.join([f"Title: {item['title']}\nSnippet: {item['snippet']}\n-----------------" for item in results.get('results', [])])
    
    return formatted_results if formatted_results else "No results found."