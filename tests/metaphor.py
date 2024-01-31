import os
from metaphor_python import Metaphor
from dotenv import load_dotenv

load_dotenv()
metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))
topic = input("Please enter your public policy for research: ")

# Use f-string for formatting
response = metaphor.search(
    f"Here is news about {topic}",
    num_results=10,
    use_autoprompt=True,
)

# Get contents from the response
contents_response = response.get_contents()

# Extract and print only the URLs
for content in contents_response.contents:
    print(content.url)
