from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool, SeperDevTool, FileReadTool
from tools.search_tools import basic_search
from langchain_openai import ChatOpenAI

web_search_tool = WebsiteSearchTool()
seper_dev_tool = SeperDevTool()
file_read_tool = FileReadTool(
    file_path='policy_brief_example.md',
    description='A tool to read the policy brief example file.'
)

class PolicyAgents():
    def research_agent(self):
        return Agent(
            role='Policy Researcher',
            goal='Investigate current policy issues, trends, and evidence through comprehensive web and database searches to gather relevant data and insights.',
            tools=[basic_search],
            backstory='An expert in navigating complex policy landscapes to extract critical data and insights from a multitude of sources.',
            verbose=True,
            llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0125")
        )

    def writer_agent(self):
        return Agent(
            role='Policy Writer',
            goal='Use insights from the Policy Researcher to create a detailed, engaging, and impactful policy brief.',
            tools=[basic_search, file_read_tool],
            backstory='Skilled in crafting impactful policy briefs that articulate insights, key trends, and evidence-based recommendations.',
            verbose=True,
            llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0125")
        )

    def review_agent(self):
        return Agent(
            role='Policy Brief Reviewer',
            goal='Critically review the draft policy brief for coherence, alignment with policy objectives, evidence strength, and persuasive clarity. Refine content to ensure high-quality, impactful communication.',
            tools=[basic_search, file_read_tool],
            backstory='A meticulous reviewer with a keen understanding of policy advocacy, ensuring each brief is clear, compelling, and grounded in solid evidence.',
            verbose=True,
            llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0125")
        )