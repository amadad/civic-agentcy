from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools.tools import WebsiteSearchTool, SeperDevTool, FileReadTool
from tools.search_tools import search_internet, perplexity_search, you_search

web_search_tool = WebsiteSearchTool()
seper_dev_tool = SeperDevTool()
file_read_tool = FileReadTool(
	file_path='policy_brief_example.md',
	description='A tool to read the policy brief example file.'
)

#OpenAIGPT3 = ChatOpenAI(model_name="gpt-3.5-turbo-0125")
OpenAIGPT4 = ChatOpenAI(model="gpt-4-0125-preview")

class PolicyAgents():
    def research_agent(self):
        return Agent(
            role='Policy Researcher',
            goal='Investigate current policy issues, trends, and evidence through comprehensive web and database searches to gather relevant data and insights.',
			tools=[perplexity_search, you_search],
            backstory='An expert in navigating complex policy landscapes to extract critical data and insights from a multitude of sources.',
            verbose=True,
            llm=OpenAIGPT4
        )

    def analysis_agent(self):
        return Agent(
            role='Policy Analyst',
            goal='Analyze gathered data to understand policy impacts, challenges, and opportunities, synthesizing findings into actionable insights.',
			tools=[search_internet, file_read_tool],
            backstory='Skilled in transforming raw data into meaningful policy analysis, identifying key trends, and suggesting evidence-based recommendations.',
            verbose=True,
            llm=OpenAIGPT4
        )

    def review_agent(self):
        return Agent(
            role='Policy Brief Reviewer',
            goal='Critically review the draft policy brief for coherence, alignment with policy objectives, evidence strength, and persuasive clarity. Refine content to ensure high-quality, impactful communication.',
			tools=[search_internet, file_read_tool],
            backstory='A meticulous reviewer with a keen understanding of policy advocacy, ensuring each brief is clear, compelling, and grounded in solid evidence.',
            verbose=True,
            llm=OpenAIGPT4
        )