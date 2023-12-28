import os
from metaphor_python import Metaphor


class MetaphorSimilarityTools:

    def __init__(self):
        # Initialize the Metaphor API with the API key from environment variables
        self.metaphor = Metaphor(os.environ.get('METAPHOR_API_KEY'))

    def find_similar_items(self, query, num_results=10):
        """
        Find items similar to the query using Metaphor API and return relevant results.
        """
        try:
            # Perform the find_similar operation using the Metaphor API
            response = self.metaphor.find_similar(query, num_results=num_results)

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
