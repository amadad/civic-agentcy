import os

from langchain.tools import tool
from metaphor_python import Metaphor


class MetaphorSimilarityTool:
    def __init__(self):
        # Initialize the Metaphor API with the API key from environment variables
        self.metaphor = Metaphor(os.environ.get('METAPHOR_API_KEY'))

    @tool
    def find_similar_items(self, input_str):
        """
        Find items similar to the query using Metaphor API and return relevant results.
        The input should be a string in the format 'query|num_results', where 'num_results' is optional.
        """
        try:
            # Parse the input string
            parts = input_str.split('|')
            query = parts[0]
            num_results = int(parts[1]) if len(parts) > 1 else 10

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

# Example of how to create an instance of the tool
metaphor_tool = MetaphorSimilarityTool()

# Example of using the tool
# result = metaphor_tool.find_similar_items("AI|5")
# print(result)
