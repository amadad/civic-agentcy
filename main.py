import os
from crewai import Agent, Task, Crew, Process
from decouple import config
from dotenv import load_dotenv
from textwrap import dedent
from agents import PublicPolicyResearchAgents
from tasks import PublicPolicyResearchTasks
from langchain.agents import load_tools

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

# Load human tools, assuming this is a part of your setup
human_tools = load_tools(["human"])

# Instantiate your tasks and agents managers
tasks_manager = PublicPolicyResearchTasks()
agents_manager = PublicPolicyResearchAgents()

print("## Welcome to Public Policy Crew")
print("-------------------------------")
policy_area = input("Enter the policy area of interest: ")
policy_details = input("Enter any specific details or context for the policy analysis: ")

# Create Agents
policy_analyst = agents_manager.policy_analyst_agent()
stakeholder_engagement = agents_manager.stakeholder_engagement_agent()
legislative_affairs = agents_manager.legislative_affairs_agent()
policy_planning = agents_manager.policy_planning_agent()
policy_report = agents_manager.policy_report_compiler_agent()

# Create Tasks and Assign Them to Agents
policy_analysis_task = tasks_manager.policy_analysis(policy_analyst, policy_area, policy_details)
stakeholder_analysis_task = tasks_manager.stakeholder_analysis(stakeholder_engagement, policy_area, policy_details)
policy_recommendation_task = tasks_manager.policy_recommendation(policy_planning, policy_area, policy_details)
legislative_briefing_task = tasks_manager.legislative_briefing(legislative_affairs, policy_area, policy_details)
implementation_plan_task = tasks_manager.implementation_plan(policy_planning, policy_area, policy_details)

# Execute Tasks Sequentially and Collect Outputs
executed_tasks = [
    policy_analysis_task,
    stakeholder_analysis_task,
    policy_recommendation_task,
    legislative_briefing_task,
    implementation_plan_task
]

# Assuming summary task needs to be created in a way that it can access the outputs of previous tasks
# This will depend on how your CrewAI framework is set up to handle task outputs and pass them to subsequent tasks

# Create Crew responsible for the policy analysis and report compilation
policy_crew = Crew(
    agents=[policy_analyst, stakeholder_engagement, legislative_affairs, policy_planning, policy_report],
    tasks=executed_tasks,  # Add executed tasks, the summary task will be handled within the crew execution logic
    process=Process.sequential  # Tasks are processed sequentially
)

# Kick off the crew process
result = policy_crew.kickoff()

# Print the final comprehensive report
# Ensure the crew's kickoff method or the summary task itself is set up to handle compiling the final report
print("\n\n################################################")
print("## Here is the final comprehensive report")
print("################################################\n")
print(result)
