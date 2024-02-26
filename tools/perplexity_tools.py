import os
from openai import OpenAI
from langchain.tools import tool

class PerplexityTool:
    def __init__(self):
        self.api_key = os.getenv("PERPLEXITY_API_KEY")
        if not self.api_key:
            raise ValueError("PERPLEXITY_API_KEY environment variable not set")
        self.client = OpenAI(api_key=self.api_key, base_url="https://api.perplexity.ai")
    
    @staticmethod
    def perplexity_search(self, query: str) -> str:
        """
        Fetches information on a specific policy topic using the OpenAI API.

        Args:
            query (str): The user query about a specific policy topic.

        Returns:
            str: The AI-generated response as a string.
        """
        system_message = (
            "You are an artificial intelligence assistant and you need to "
            "engage in a helpful, detailed, polite conversation with a user."
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": query},
        ]

        response = self.client.chat.completions.create(
            model="sonar-medium-online",
            messages=messages,
        )

        # Adjusted to navigate through the response structure
        content = response.choices[0].message.content
        return content