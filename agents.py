from crewai import Agent
from tools.search import SearchTools
from tools.perplexity_tools import PerplexityTool
from langchain_openai import ChatOpenAI
    
class PublicPolicyResearchAgents():
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0)

    def analyst_agent(self):
        return Agent(
            role="Policy Analyst",
            goal='Recent news and analysis of public policies',
            backstory='As a Policy Analyst at a leading think tank, you specialize in evaluating focusing on recent news, objectives, effectiveness, and areas for improvement. Provide in-depth insights to guide policy formulation and refinement. the impact of public policies on society, economy, and environment.',
            tools=[lambda query: PerplexityTool.perplexity_search(query)],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def change_agent(self):
        return Agent(
            role="Policy Engagement Specialist",
            goal='Identify and analyze key stakeholders related to specific policy areas',
            backstory='You are a Stakeholder Engagement Specialist, known for your ability to navigate complex policy landscapes and facilitate dialogue between diverse groups to achieve policy objectives. Develop strategies for engagement and consensus-building.',
            tools=[lambda query: PerplexityTool.perplexity_search(query)],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def policy_writer(self):
        return Agent(
            role="Senior Policy Brief Writer",
            goal="Write engaging and interesting blog post about latest AI projects using simple, layman vocabulary",
            backstory='You are an Expert Writer on technical, social, policitical and social matters. Be informative and engaging.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
)
    
    #SearchTools.search_internet