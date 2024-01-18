import os

from langchain.llms import Ollama
from langchain.tools import DuckDuckGoSearchRun

from crewai import Agent, Crew, Process, Task

ollama_dolphinmixtral = Ollama(model="dolphin")
search_tool = DuckDuckGoSearchRun()
policy_task = input("Please enter your public policy for research: ")

# Define your agents with roles and goals focusing on policy research and analysis
policy_analyst = Agent(
  role='Policy Analyst',
  goal='Conduct in-depth policy research and analysis for voter influence',
  backstory=f"""You are a policy analyst at a prominent think tank specializing in {policy_task}.
  You have a strong background in analyzing the impacts of {policy_task} on society and regulations.
  Your expertise includes synthesizing complex policy documents into actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  llm=ollama_dolphinmixtral
)

policy_writer = Agent(
  role='Policy Content Writer',
  goal='Create informative and engaging content on persuasive policy',
  backstory="""As a skilled writer, you specialize in translating policy research into clear, 
  engaging articles for a broad audience. You excel in making complex policy issues 
  understandable and relevant to the public discourse.""",
  verbose=True,
  allow_delegation=True,
  llm=ollama_dolphinmixtral
)

# Create tasks for your agents
task1 = Task(
  description=f"""Research and analyze the most recent policies and regulations regarding {policy_task}.
  Examine their implications, effectiveness, and areas for improvement.
  Produce a comprehensive policy analysis report, detailing your findings and recommendations.""",
  agent=policy_analyst
)

task2 = Task(
  description=f"""Based on the policy analysis, write an informative article targeting a general audience.
  The article should highlight key aspects of current {policy_task} policies and their societal impact.
  Make it engaging and accessible, using language that resonates with non-experts.
  The final output should be a well-structured article of at least four paragraphs.""",
  agent=policy_writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[policy_analyst, policy_writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)