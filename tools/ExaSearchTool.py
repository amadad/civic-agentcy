import os
import datetime
from datetime import timedelta
from exa_py import Exa
from langchain.agents import tool
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI

class ExaSearchTool:	
	@tool
	def search(query: str):
		"""Search for a webpage based on the query."""
		return ExaSearchTool._exa().search(f"{query}", use_autoprompt=True, num_results=3)

	@tool
	def find_similar(url: str):
		"""Search for webpages similar to a given URL.
		The url passed in should be a URL returned from `search`.
		"""
		return ExaSearchTool._exa().find_similar(url, num_results=3)

	@tool
	def get_contents(ids: str):
		"""Get the contents of a webpage.
		The ids must be passed in as a list, a list of ids returned from `search`.
		"""
		ids = eval(ids)
		contents = str(ExaSearchTool._exa().get_contents(ids))
		print(contents)
		contents = contents.split("URL:")
		contents = [content[:1000] for content in contents]
		return "\n\n".join(contents)


	@tool
	def recent_news(query: str, max_items=3):
		"""Get recent news based on a query and summarize it.
		"""
		search_response = ExaSearchTool._exa().search_and_contents(
			query,
			num_results=max_items,
			start_published_date=timedelta(days=30),
			end_published_date=datetime.now(),
			use_autoprompt=True,
			highlights={"num_sentences": 8}
        )
		results = search_response.results
		for result_item in results:
			llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0125")
			chain = load_summarize_chain(llm, chain_type="stuff")
			chain.run(result_item.text)
			print(result_item.text)

	def tools():
		return [ExaSearchTool.search, ExaSearchTool.find_similar, ExaSearchTool.get_contents, ExaSearchTool.recent_news]

	def _exa():
		return Exa(api_key=os.environ["EXA_API_KEY"])