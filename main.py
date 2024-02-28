import streamlit as st
from dotenv import load_dotenv
from crewai import Crew
from tasks import PolicyTasks  
from agents import PolicyAgents

load_dotenv()

policy_tasks = PolicyTasks()
policy_agents = PolicyAgents()

st.set_page_config(page_title="Civic Agentcy", page_icon="🗳️")
st.title('Civic Agentcy')
st.markdown("##### 🗳️ topical and timely intelligence on public policy")

policy_topic = st.text_input("What is the policy area of interest?", placeholder="E.g., Solar energy policy in Michigan")
research_questions = st.text_input("What specific research questions should the policy analysis address?", placeholder="E.g., What are the current barriers to solar energy adoption?")
recommendations_summary = st.text_input("Provide a summary of your policy recommendations.", placeholder="E.g., Incentives for solar installation, streamlined permitting process")
external_factors = st.text_input("What external factors should be considered in the policy analysis?", placeholder="E.g., Federal energy policies, technological advancements in solar panels")

# Create Agents
researcher_agent = policy_agents.research_agent()
writer_agent = policy_agents.writer_agent()
review_agent = policy_agents.review_agent()

if st.button('Start Research'):

    # Define Tasks for each agent
    research_policy_task = policy_tasks.research_policy_issues_task(researcher_agent, policy_topic, research_questions)
    legislation_policy_task = policy_tasks.decision_making_and_legislation_task(researcher_agent, research_questions, policy_topic)
    analyze_policy_options_task = policy_tasks.analyze_policy_options_task(researcher_agent, policy_topic)
    draft_policy_brief_task = policy_tasks.draft_policy_brief_task(writer_agent, policy_topic, recommendations_summary)
    review_and_refine_policy_brief_task = policy_tasks.review_and_refine_policy_brief_task(review_agent, policy_topic)


    crew = Crew(
        agents=[
            researcher_agent, 
            writer_agent, 
            review_agent
        ], 
        tasks=[
            research_policy_task, 
            legislation_policy_task,
            analyze_policy_options_task, 
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