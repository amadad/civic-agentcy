Public Policy Crew Project

Overview

The Public Policy Crew Project is a comprehensive framework designed to automate the process of analyzing public policies, engaging stakeholders, preparing legislative briefings, developing policy recommendations, and compiling detailed reports. Utilizing a combination of advanced language models and web scraping tools, this project aims to provide in-depth insights that guide policy formulation, refinement, and implementation planning.

Setup

Requirements
Python 3.6+
crewai
dotenv
decouple
langchain_community
langchain_openai
Installation
Clone the repository to your local machine.
Navigate to the project directory.
Install the required dependencies:
Copy code
pip install -r requirements.txt
Create a .env file in the project root directory and add your OPENAI_API_KEY:
makefile
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Usage

To run the Public Policy Crew application, execute the following command from the terminal:

css
Copy code
python main.py
You will be prompted to enter a policy area of interest and any specific details or context for the policy analysis. The system will then automatically conduct a comprehensive policy analysis, engage with stakeholders, prepare legislative briefings, develop policy recommendations, and compile a detailed policy report.

Custom Agents
Policy Analyst: Conducts a comprehensive analysis of public policies, focusing on objectives, effectiveness, and areas for improvement.
Stakeholder Engagement Specialist: Identifies and analyzes key stakeholders, developing strategies for engagement and consensus-building.
Legislative Affairs Advisor: Prepares legislative briefings and recommends policy actions to lawmakers.
Policy Planning Specialist: Develops implementation plans for policy recommendations.
Policy Report Compiler: Compiles comprehensive policy reports integrating analysis, stakeholder perspectives, and recommendations.
Tasks
Policy Analysis: Analyzes the designated policy area, providing a comprehensive evaluation of the policy.
Stakeholder Analysis: Conducts an analysis of stakeholders related to the policy area.
Policy Recommendation: Develops clear, targeted, and feasible policy recommendations.
Legislative Briefing: Prepares a briefing suitable for policymakers, summarizing key findings and recommendations.
Implementation Plan: Outlines steps for the adoption, execution, and evaluation of policies.
Development

This project utilizes the crewai package to define agents and tasks that automate the analysis and reporting process. Language models from langchain_community and langchain_openai are used to process and analyze text, while SearchTools and BrowserTools enable web scraping for up-to-date information.

Contributing

Contributions to the Public Policy Crew Project are welcome. Please ensure to follow the project's code standards and submit pull requests for review.

License

Specify your license or state if the project is open-source and free to use.
