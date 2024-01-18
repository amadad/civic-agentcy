import datetime
import os

from crewai import Agent, Crew, Process, Task

#from langchain.llms import Ollama
from langchain.chat_models import ChatOllama

from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

#from langchain.tools import DuckDuckGoSearchRun

#ollama_dolphinmixtral = ChatOllama(model="dolphin")
ollama_hermes2 = ChatOllama(model="nous-hermes2-mixtral")
#search_tool = DuckDuckGoSearchRun()
search_tool = SearchTools()
policy_task = input("Please enter your public policy for research: ")

policy_analyst = Agent(
  role='Policy Analyst',
  goal='Conduct in-depth policy research and analysis for voter influence',
  backstory=f"""You are a policy analyst at a prominent think tank specializing in {policy_task}.
  You have a strong background in analyzing the impacts of {policy_task} on society and regulations.
  Your expertise includes synthesizing complex policy documents into actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[
    SearchTools.search_internet,
    BrowserTools.scrape_and_summarize_website,
    ],
  llm=ollama_hermes2
)

policy_writer = Agent(
  role='Policy Content Writer',
  goal='Create informative and engaging content on persuasive policy',
  backstory="""As a skilled writer, you specialize in translating policy research into clear, 
  engaging articles for a broad audience. You excel in making complex policy issues 
  understandable and relevant to the public discourse.""",
  verbose=True,
  allow_delegation=True,
  llm=ollama_hermes2
)

# Create tasks for your agents
task1 = Task(
  description=f"""Research and analyze the most recent policies and regulations regarding {policy_task}.
  Examine their implications, effectiveness, and areas for improvement.
  Your final answer MUST be a full analysis report.""",
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
  verbose=True, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

# Specify the path to your existing output directory
output_folder = "output"
current_date = datetime.datetime.now().strftime("%B-%d-%Y")
policy_task_shortened = policy_task[:12]
output_filename = f"{policy_task_shortened}_{current_date}.md"
output_file_path = os.path.join(output_folder, output_filename)
with open(output_file_path, "a") as markdown_file:
    markdown_file.write(f"# {policy_task}\n\n")
    markdown_file.write(result)
print(f"Result saved to {output_file_path}")