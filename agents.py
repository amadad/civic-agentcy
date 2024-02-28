from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool, SeperDevTool, FileReadTool
from tools.search_tools import search_internet, perplexity_search, you_search

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
            tools=[you_search],
            backstory='An expert in navigating complex policy landscapes to extract critical data and insights from a multitude of sources.',
            verbose=True,
        )

    def writer_agent(self):
        return Agent(
            role='Policy Writer',
            goal='Use insights from the Policy Researcher to create a detailed, engaging, and impactful policy brief.',
            tools=[perplexity_search, search_internet, file_read_tool],
            backstory='Skilled in crafting impactful policy briefs that articulate insights, key trends, and evidence-based recommendations.',
            verbose=True,
        )

    def review_agent(self):
        return Agent(
            role='Policy Brief Reviewer',
            goal='Critically review the draft policy brief for coherence, alignment with policy objectives, evidence strength, and persuasive clarity. Refine content to ensure high-quality, impactful communication.',
            tools=[search_internet, file_read_tool],
            backstory='A meticulous reviewer with a keen understanding of policy advocacy, ensuring each brief is clear, compelling, and grounded in solid evidence.',
            verbose=True,
        )