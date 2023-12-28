import os
from metaphor_python import Metaphor
import requests
from langchain.tools import tool


class MetaphorSearchTools:

    @tool("Search the internet")
    def __init__(self):
        # Initialize the Metaphor API with the API key from environment variables
        self.metaphor = Metaphor(os.environ.get('METAPHOR_API_KEY'))

    def search_with_metaphor(self, query, num_results=10):
        """
        Search using Metaphor API and return relevant results.
        """
        try:
            # Perform the search using the Metaphor API
            response = self.metaphor.search(query, num_results=num_results, use_autoprompt=True)

            # Process the response to create a readable format
            results = response.get('results', [])
            formatted_results = []

            for result in results:
                formatted_results.append('\n'.join([
                    f"Title: {result.get('title')}", 
                    f"Link: {result.get('link')}",
                    f"Snippet: {result.get('snippet')}", 
                    "\n-----------------"
                ]))

            return '\n'.join(formatted_results)

        except Exception as e:
            # Handle exceptions
            return f"An error occurred: {str(e)}"
