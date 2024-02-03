import os
from crewai import Agent, Task, Crew, Process
from decouple import config
from dotenv import load_dotenv
from textwrap import dedent
from agents import CustomAgents
from tasks import PublicPolicyResearchTasks

load_dotenv()
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

class PublicPolicyCrew:
    def __init__(self, policy_area, policy_details):
        self.policy_area = policy_area
        self.policy_details = policy_details

    def run(self):
        agents = CustomAgents()
        tasks = PublicPolicyResearchTasks()

        # Define your custom agents and tasks here
        policy_analyst = agents.policy_analyst_agent()
        stakeholder_engagement = agents.stakeholder_engagement_agent()
        legislative_affairs = agents.legislative_affairs_agent()
        policy_planning = agents.policy_planning_agent()

        # Custom tasks include agent name and variables as input
        policy_analysis_task = tasks.policy_analysis(policy_analyst, self.policy_area, self.policy_details)
        stakeholder_analysis_task = tasks.stakeholder_analysis(stakeholder_engagement, self.policy_area, self.policy_details)
        legislative_briefing_task = tasks.legislative_briefing(legislative_affairs, self.policy_area, self.policy_details)
        implementation_plan_task = tasks.implementation_plan(policy_planning, self.policy_area, self.policy_details)

        # Define the crew
        policy_crew = Crew(
            agents=[
                policy_analyst, 
                stakeholder_engagement, 
                legislative_affairs, 
                policy_planning, 
            ],
            tasks=[
                policy_analysis_task, 
                stakeholder_analysis_task, 
                legislative_briefing_task, 
                implementation_plan_task, 
            ],
            verbose=True,
        )

        result = policy_crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to Public Policy Crew")
    print("-------------------------------")
    policy_area = input("Enter the policy area of interest: ")
    policy_details = input("Enter any specific details or context for the policy analysis: ")

    policy_crew = PublicPolicyCrew(policy_area, policy_details)
    result = policy_crew.run()
    print("\n\n########################")
    print("## Here is your public policy crew run result:")
    print("########################\n")
    print(result)