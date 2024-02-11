import os
import json
import requests
from dotenv import load_dotenv
from langchain.tools import BaseTool, tool

load_dotenv()

class PerplexityTool(BaseTool):
    name = "Perplexity Search"
    description = "Perform a comprehensive political analysis using Perplexity AI."
    perplexity_api_key: str  # Define perplexity_api_key as a class attribute

    def __init__(self):
        super().__init__()
        # Assigning instance attributes directly, ensure BaseTool doesn't enforce Pydantic schema.
        self.perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
        self.perplexity_api_base = "https://api.perplexity.ai"
        self.model = "pplx-7b-online"

    def _run(self, topic: str) -> str:
        """Internal method to perform a comprehensive political analysis using Perplexity AI.
        
        This method encapsulates the functionality that sends a request to Perplexity AI,
        performs a political analysis based on the given topic, formats the request, handles
        the response, and parses it into a readable format.

        Args:
            topic (str): The political topic to analyze.
        
        Returns:
            str: A comprehensive analysis of the given topic. This is intended to be
                 used internally by the tool infrastructure.
        """
        return self.perplexity_search(topic)

    @tool("Perplexity Search")
    def perplexity_search(self, topic: str) -> str:
        """Public method exposed as a tool for performing a comprehensive political analysis
        using Perplexity AI.
        
        This method prepares and sends a request to the Perplexity AI to analyze a specific
        political topic, then processes and returns the analysis results.

        Args:
            topic (str): The political topic to analyze.
        
        Returns:
            str: A comprehensive analysis of the given topic.
        """
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an artificial intelligence assistant."},
                {"role": "user", "content": f"Provide a comprehensive political analysis of {topic}."}
            ]
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.perplexity_api_key}"
        }

        try:
            response = requests.post(f"{self.perplexity_api_base}/chat/completions", json=payload, headers=headers)
            response.raise_for_status()  # Raises an exception for HTTP errors
            return self.parse_response(response.text)
        except requests.RequestException as e:
            return f"An error occurred: {str(e)}"

    def parse_response(self, response_text: str) -> str:
        """Parse the JSON response from the Perplexity API and extract the analysis content."""
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
