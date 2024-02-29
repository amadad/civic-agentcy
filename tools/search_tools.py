import json
import os
import requests
from openai import OpenAI
from crewai_tools import tool
from langchain.chains.summarize import load_summarize_chain

"""
List of tools available in the search_tools module:
- basic_search: Performs a basic search using Serper.
- search_internet: Searches the internet using SerpApi.
- perplexity_search: Searches the internet using Perplexity.
- you_search: Searches the internet using You Search.
- exa_search: Searches the internet using Exa.
- exa_find_similar: Finds similar links to a given URL using Exa.
- exa_get_content: Retrieves the contents of documents using Exa.
"""

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
def you_search(query: str) -> list:
    """
    Fetches AI-generated snippets based on the given query from the YDC Index API,
    parses the JSON response, and returns the relevant parts of the search results.

    Args:
        query (str): The search query to fetch snippets for.

    Returns:
        list: A list of dictionaries, each containing the title, description, and URL of a search result.
    """
    you_api_key = os.getenv('YOU_API_KEY')
    headers = {"X-API-Key": you_api_key}
    try:
        response = requests.get(
            f"https://api.ydc-index.io/news",
            params={"q": query},
            headers=headers,
        )
        response.raise_for_status()  # Raises an error for bad responses
        json_response = response.json()

        # Parsing the JSON response
        results = json_response.get('news', {}).get('results', [])
        parsed_results = []

        for result in results:
            title = result.get('title')
            description = result.get('description')
            url = result.get('url')

            if title and description and url:
                parsed_results.append({
                    'title': title,
                    'description': description,
                    'url': url
                })

        return parsed_results
    except requests.RequestException as e:
        return [{"error": str(e)}]
    
@tool("Retrieve contents of documents based on a list of document IDs.")
def exa_get_content(doc_ids: str) -> str:
    """
    Retrieves the contents of documents from the Exa API based on a list of document IDs.
    
    Args:
        doc_ids (str): A comma-separated list of document IDs to retrieve contents for.
    
    Returns:
        str: The JSON response from the Exa API containing the documents' contents.
    """
    url = "https://api.exa.ai/contents"
    payload = {"ids": doc_ids.split(",")}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": os.getenv("EXA_API_KEY")
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.text

@tool("Perform a search with an Exa prompt-engineered query.")
def exa_search(query: str, use_autoprompt: bool = True, include_domains: str = "", exclude_domains: str = "", start_published_date: str = "", end_published_date: str = "") -> str:
    """
    Performs a search with the Exa API using a prompt-engineered query and retrieves relevant results.
    
    Args:
        query (str): The search query.
        use_autoprompt (bool): Whether to use autoprompt for the search.
        include_domains (str): Comma-separated domains to include.
        exclude_domains (str): Comma-separated domains to exclude.
        start_published_date (str): Start date for when the document was published (YYYY-MM-DD format).
        end_published_date (str): End date for when the document was published (YYYY-MM-DD format).
    
    Returns:
        str: The JSON response from the Exa API with search results.
    """
    url = "https://api.exa.ai/search"
    payload = {
        "query": query,
        "useAutoprompt": use_autoprompt,
        "includeDomains": include_domains.split(",") if include_domains else [],
        "excludeDomains": exclude_domains.split(",") if exclude_domains else [],
        "startPublishedDate": start_published_date,
        "endPublishedDate": end_published_date
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": os.getenv("EXA_API_KEY")
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.text

@tool("Find similar links to the provided URL.")
def exa_find_similar(url: str, include_domains: str = "", exclude_domains: str = "", start_published_date: str = "", end_published_date: str = "") -> str:
    """
    Finds similar links to the provided URL using the Exa API, optionally filtering by domain and publication date.
    
    Args:
        url (str): The base URL to find similar links with.
        include_domains (str): Comma-separated domains to include.
        exclude_domains (str): Comma-separated domains to exclude.
        start_published_date (str): Start date for when the document was published (YYYY-MM-DD format).
        end_published_date (str): End date for when the document was published (YYYY-MM-DD format).
    
    Returns:
        str: The JSON response from the Exa API with similar links.
    """
    api_url = "https://api.exa.ai/findSimilar"
    payload = {
        "url": url,
        "includeDomains": include_domains.split(",") if include_domains else [],
        "excludeDomains": exclude_domains.split(",") if exclude_domains else [],
        "startPublishedDate": start_published_date,
        "endPublishedDate": end_published_date
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": os.getenv("EXA_API_KEY")
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.text