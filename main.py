import os
from crewai import Agent, Task, Crew, Process
from decouple import config
from dotenv import load_dotenv
from textwrap import dedent
from agents import PublicPolicyResearchAgents
from tasks import PublicPolicyResearchTasks

load_dotenv()
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

tasks = PublicPolicyResearchTasks()
agents = PublicPolicyResearchAgents()

print("## Welcome to Public Policy Crew")
print("-------------------------------")
policy_area = input("Enter the policy area of interest: ")
policy_details = input("Enter any specific details or context for the policy analysis: ")

# Create Agents
policy_analyst = agents.policy_analyst_agent()
stakeholder_engagement = agents.stakeholder_engagement_agent()
legislative_affairs = agents.legislative_affairs_agent()
policy_planning = agents.policy_planning_agent()
policy_report = agents.policy_report_compiler_agent()

# Create Tasks
policy_analysis_task = tasks.policy_analysis(policy_analyst, policy_area, policy_details)
stakeholder_analysis_task = tasks.stakeholder_analysis(stakeholder_engagement, policy_area, policy_details)
policy_recommendation = tasks.policy_recommendation(policy_planning, policy_area, policy_details)
legislative_briefing_task = tasks.legislative_briefing(legislative_affairs, policy_area, policy_details)
implementation_plan_task = tasks.implementation_plan(policy_planning, policy_area, policy_details)
policy_report_task = tasks.summary_and_briefing_task(policy_report, [
    policy_analysis_task,
    stakeholder_analysis_task,
    policy_recommendation,
    legislative_briefing_task,
    implementation_plan_task
], policy_area, policy_details)

# Create Crew responsible for Copy
policy_crew = Crew(
        agents=[
                policy_analyst, 
                stakeholder_engagement, 
                legislative_affairs, 
                policy_planning, 
                policy_report
            ],
            tasks=[
                policy_analysis_task, 
                stakeholder_analysis_task, 
                policy_recommendation,
                legislative_briefing_task, 
                implementation_plan_task, 
                policy_report_task
            ]
        )

result = policy_crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(result)