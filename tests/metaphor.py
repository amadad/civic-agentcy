import os

from dotenv import load_dotenv
from metaphor_python import Metaphor

load_dotenv()
metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))
topic = input("Please enter your public policy for research: ")

# Use f-string for formatting
response = metaphor.search(
    f"Here is news about {topic}",
    num_results=10,
    use_autoprompt=True,
)

print(response)
