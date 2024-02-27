import streamlit as st
from dotenv import load_dotenv
from crewai import Crew  # Ensure this import matches your project structure
# Ensure these imports match your file structure and contain the necessary classes
from tasks import PolicyTasks  
from agents import PolicyAgents

load_dotenv()  # Load environment variables at the start

# Initialize tasks and agents from your custom classes
policy_tasks = PolicyTasks()
policy_agents = PolicyAgents()

# Instantiate agents
researcher_agent = policy_agents.research_agent()
analysis_agent = policy_agents.analysis_agent()
review_agent = policy_agents.review_agent()

# Streamlit app configuration
st.set_page_config(page_title="Civic Agentcy", page_icon="🗳️")
st.title('Civic Agentcy')
st.markdown("##### 🗳️ topical and timely intelligence on public policy")

policy_topic = st.text_input("What is the policy area of interest?", placeholder="E.g., Solar energy policy in Michigan")
research_questions = st.text_input("What specific research questions should the policy analysis address?", placeholder="E.g., What are the current barriers to solar energy adoption?")
recommendations_summary = st.text_input("Provide a summary of your policy recommendations.", placeholder="E.g., Incentives for solar installation, streamlined permitting process")
external_factors = st.text_input("What external factors should be considered in the policy analysis?", placeholder="E.g., Federal energy policies, technological advancements in solar panels")

if st.button('Start Research'):

    research_policy_issues_task = policy_tasks.research_policy_issues_task(researcher_agent, policy_topic, research_questions)
    analyze_policy_options_task = policy_tasks.analyze_policy_options_task(analysis_agent, policy_topic)
    draft_policy_brief_task = policy_tasks.draft_policy_brief_task(analysis_agent, policy_topic, recommendations_summary)
    review_and_refine_policy_brief_task = policy_tasks.review_and_refine_policy_brief_task(review_agent, policy_topic)
    industry_and_policy_impact_analysis_task = policy_tasks.industry_and_policy_impact_analysis_task(analysis_agent, policy_topic, external_factors)

    crew = Crew(
        agents=[
            researcher_agent, 
            analysis_agent, 
            review_agent
        ], 
        tasks=[
            research_policy_issues_task, 
            analyze_policy_options_task, 
            industry_and_policy_impact_analysis_task, 
            draft_policy_brief_task, 
            review_and_refine_policy_brief_task
        ]
    )

    result = crew.kickoff()

    st.markdown(result)
    st.download_button(
        label="Download", 
        data=result, 
        file_name="policy_brief.md", 
        mime="text/plain"
    )
