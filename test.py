from tools.exa_tools import ResearchTools
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.schema import SystemMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-4-0125-preview")

system_message = SystemMessage(
    content="You are a web researcher who answers user questions by looking up information on the internet and retrieving contents of helpful documents. Cite your sources."
)

agent_prompt = OpenAIFunctionsAgent.create_prompt(system_message)

agent = OpenAIFunctionsAgent(
    llm=llm, 
    tools=[
        ResearchTools.exa_search, 
        ResearchTools.find_similar,
    ],
    prompt=agent_prompt
)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=[
        ResearchTools.exa_search, 
        ResearchTools.find_similar,
    ],
    verbose=True
)

agent_executor.run(
    "Summarize for me an interesting article about Tax Relief for American Families and Workers Act of 2024 published after October 2023."
)