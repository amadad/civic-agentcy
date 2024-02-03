from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.browser_tools import BrowserTools

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def policy_analyst_agent(self):
        return Agent(
            role="Policy Analyst",
            goal=dedent("""\
                Conduct comprehensive analysis of public policies,
                focusing on their objectives, effectiveness, and areas for improvement.
                Provide in-depth insights to guide policy formulation and refinement."""),
            backstory=dedent("""\
                As a Policy Analyst at a leading think tank, you specialize in evaluating
                the impact of public policies on society, economy, and environment."""),
            tools=[
                    BrowserTools.scrape_and_summarize_website,
                    SearchTools.search_internet
            ],
            allow_delegation=False,
            llm=self.OpenAIGPT35,
            verbose=True
        )

    def stakeholder_engagement_agent(self):
        return Agent(
            role="Stakeholder Engagement Specialist",
            goal=dedent("""\
                Identify and analyze key stakeholders related to specific policy areas.
                Develop strategies for engagement and consensus-building."""),
            backstory=dedent("""\
                You are a Stakeholder Engagement Specialist, known for your ability
                to navigate complex policy landscapes and facilitate dialogue between
                diverse groups to achieve policy objectives."""),
            tools=[
                    BrowserTools.scrape_and_summarize_website,
                    SearchTools.search_internet
            ],
            llm=self.OpenAIGPT35,
            verbose=True
        )

    def legislative_affairs_agent(self):
        return Agent(
            role="Legislative Affairs Advisor",
            goal=dedent("""\
                Prepare legislative briefings and recommend policy actions to lawmakers.
                Synthesize research findings into actionable insights for policy advancement."""),
            backstory=dedent("""\
                As a Legislative Affairs Advisor, you bridge the gap between policy research
                and legislative action, ensuring that lawmakers have the information they need
                to make informed decisions."""),
            tools=[
                    BrowserTools.scrape_and_summarize_website,
                    SearchTools.search_internet
            ],
            llm=self.OpenAIGPT35,
            verbose=True
        )
    
    def policy_planning_agent(self):
        return Agent(
            role="Policy Planning Specialist",
            goal=dedent("""\
                Develop implementation plans for policy recommendations, outlining steps
                for adoption, execution, and evaluation of policies."""),
            backstory=dedent("""\
                You're a Policy Planning Specialist with expertise in transforming policy
                recommendations into actionable plans, ensuring their successful execution
                and impact assessment."""),
            tools=[
                    BrowserTools.scrape_and_summarize_website,
                    SearchTools.search_internet
            ],
            llm=self.OpenAIGPT35,
            verbose=True
        )
    
    def policy_report_compiler_agent(self):
        return Agent(
            role="Policy Report Compiler",
            goal=dedent("""\
                Compile comprehensive policy reports that integrate analysis, stakeholder perspectives,
                recommendations, and implementation strategies into a cohesive overview."""),
            backstory=dedent("""\
                As a Policy Report Compiler, you excel in synthesizing diverse insights into comprehensive
                reports that guide policymakers, stakeholders, and the public in understanding and navigating
                complex policy issues."""),
            tools=[
                    BrowserTools.scrape_and_summarize_website,
                    SearchTools.search_internet
            ],
            llm=self.OpenAIGPT35,
            verbose=True
        )