import os
from crewai import Crew, Process
from decouple import config
from dotenv import load_dotenv
from agents import PublicPolicyResearchAgents
from tasks import PublicPolicyResearchTasks

load_dotenv()
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

tasks = PublicPolicyResearchTasks()
agents = PublicPolicyResearchAgents()

print("## Welcome to Civic Agentcy")
print("-------------------------------")
policy_area = input("Enter the policy area of interest: ")
policy_details = input("Enter any specific details or context for the policy analysis: ")

# Create Agents
analyst = agents.analyst_agent()
change = agents.change_agent()
writer = agents.policy_writer()

# Create Tasks
policy_analysis_task = tasks.policy_analysis(analyst, policy_area, policy_details)
change_analysis_task = tasks.change_analysis(change, policy_area, policy_details)
final_report_task = tasks.policy_brief(writer, policy_analysis_task.output, change_analysis_task.output_json)

# Crew Kick off
policy_crew = Crew(
    agents=[analyst, change],
    tasks=[policy_analysis_task, change_analysis_task, final_report_task],
    process=Process.sequential,
    verbose=2
)

result = policy_crew.kickoff()
print("\n\n################################################")
print("## Here is the final comprehensive report")
print("################################################\n")
print(result)