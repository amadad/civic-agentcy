import os
from textwrap import dedent
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from tools.file_tools import FileTools
from tools.search import SearchTools
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
policy_task = input("Please enter your public policy for research: ")
model="gpt-3.5-turbo-1106"

# Define the Policy Analyst Agent
policy_analyst = Agent(
  role='Policy Analyst',
  goal='Conduct in-depth policy research and analysis for voter influence',
  backstory=f"You are a policy analyst specializing in {policy_task}.",
  verbose=True,
  allow_delegation=False,
  tools = [
    SearchTools.search_internet
  ],
  llm=ChatOpenAI(model_name=model, temperature=0.7, api_key=openai_api_key)
)

# Define the Policy Writer Agent
policy_writer = Agent(
  role='Policy Content Writer',
  goal='Create informative and engaging content on persuasive policy',
  backstory="As a skilled writer, you specialize in translating policy research into clear, engaging articles.",
  verbose=True,
  allow_delegation=True,
  # tools=[FileTools.write_file],
  llm=ChatOpenAI(model_name=model, temperature=0.7, api_key=openai_api_key)
)

# Define Task 1 - Policy Analysis
task1 = Task(
  description=f"Research and analyze policies regarding {policy_task}. Provide a full analysis report.",
  agent=policy_analyst
)

# Define Task 2 - Article Writing
task2 = Task(
  description=f"""Based on the policy analysis, write an article on {policy_task}. 
  The final output should be a well-structured article of at least four paragraphs.""",
  agent=policy_writer
)

# Instantiate the Crew
crew = Crew(
  agents=[policy_analyst, policy_writer],
  tasks=[task1, task2],
  verbose=True
)

# Kickoff the Crew Workflow
results = crew.kickoff()
formatted_content = FileTools.format_to_markdown(results)
file_output = FileTools.write_file(formatted_content)
print(file_output)