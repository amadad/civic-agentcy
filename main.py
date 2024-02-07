import os
from crewai import Agent, Task, Crew, Process
from decouple import config
from dotenv import load_dotenv
from textwrap import dedent
from agents import PublicPolicyResearchAgents
from tasks import PublicPolicyResearchTasks
from langchain.agents import load_tools

# Load environment variables and set API keys
load_dotenv()
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

# Load tools required for agents' tasks
human_tools = load_tools(["human"])

# Instantiate managers for tasks and agents
tasks_manager = PublicPolicyResearchTasks()
agents_manager = PublicPolicyResearchAgents()

print("## Welcome to Civic Agentcy")
print("-------------------------------")
policy_area = input("Enter the policy area of interest: ")
policy_details = input("Enter any specific details or context for the policy analysis: ")

# Create Agents
policy_analyst = agents_manager.policy_analyst_agent()
stakeholder_engagement = agents_manager.stakeholder_engagement_agent()
legislative_affairs = agents_manager.legislative_affairs_agent()
policy_planning = agents_manager.policy_planning_agent()
policy_report = agents_manager.policy_report_compiler_agent()

# Create Tasks
policy_analysis_task = tasks_manager.policy_analysis(policy_analyst, policy_area, policy_details)
stakeholder_analysis_task = tasks_manager.stakeholder_analysis(stakeholder_engagement, policy_area, policy_details)
policy_recommendation_task = tasks_manager.policy_recommendation(policy_planning, policy_area, policy_details)
legislative_briefing_task = tasks_manager.legislative_briefing(legislative_affairs, policy_area, policy_details)
implementation_plan_task = tasks_manager.implementation_plan(policy_planning, policy_area, policy_details)

# Crew Kick off
policy_crew = Crew(
    agents=[policy_analyst, stakeholder_engagement, legislative_affairs, policy_planning, policy_report],
    tasks=[policy_analysis_task, stakeholder_analysis_task, policy_recommendation_task, legislative_briefing_task, implementation_plan_task],  
    verbose=2,
    process=Process.sequential  
)

result = policy_crew.kickoff()
print("\n\n################################################")
print("## Here is the final comprehensive report")
print("################################################\n")
print(result)
