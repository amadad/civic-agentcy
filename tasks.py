from textwrap import dedent
from crewai import Task
from typing import List
from pydantic import BaseModel, Field


class PolicyResearch(BaseModel):
    policy_topic: str
    research_questions: List[str] = Field(
        ..., description="Specific research questions guiding the investigation")
    current_status: List[str] = Field(
        ...,
        description="Overview of the policy's current status and relevant debates"
    )
    stakeholder_perspectives: List[str] = Field(
        ...,
        description="Analysis of different stakeholders' views and opinions")
    evidence_base: List[str] = Field(
        ...,
        description="Empirical evidence supporting various positions on the policy")
    key_findings: List[str] = Field(
        ...,
        description="Summary of key insights and divergent viewpoints identified through research"
    )
    url_citation: List[str] = Field(
        ...,
        description="URLs linking to sources that provide additional information or evidence supporting the key findings"
    )


class PolicyTasks:
    def research_policy(self, agent, policy_topic: str, research_focus: str):
        return Task(
            description=dedent(f"""
                **Research Policy Issues**
                - **Policy Topic**: {policy_topic}
                - **Research Focus**: {research_focus}
                Conduct a comprehensive investigation on the current status, debates, and evidence related to the policy topic. 
                Analyze stakeholder perspectives and empirical evidence to formulate a detailed report.
            """),
            expected_output=dedent("""
                **Executive Summary**: Overview highlighting the urgency, challenges, and preliminary recommendations.
                **Current Status & Background**: Brief on the policy's present scenario and debates.
                **Stakeholder Perspectives**: Summary of key stakeholder viewpoints.
                **Evidence Base & Key Findings**: 
                - Empirical evidence points.
                - Critical insights from the research.
                - URL citation
            """),
            agent=agent,
            output_pydantic=PolicyResearch,
        )

    def analyze_and_draft_brief(self, agent, policy_topic, research_findings):
        return Task(
            description=dedent(f"""
                Based on the research conducted, analyze potential policy options for {policy_topic}. 
                Evaluate the pros and cons of each option, considering effectiveness, feasibility, and potential impact.
                Draft a policy brief that includes:
                1. An executive summary
                2. Current status and background
                3. Analysis of policy options
                4. Evidence-based recommendations
                5. Conclusion and call to action
            """),
            expected_output=dedent(f"""
                ## Policy Brief on {policy_topic}
                **Executive Summary**: 
                  - Highlights key points, challenges, and recommendations.
                **Current Status & Background**: 
                  - Overview of the policy's present scenario and debates.
                **Analysis of Policy Options**:
                  - Evaluation of different policy options with pros and cons.
                **Recommendations**: 
                  - Evidence-based policy recommendations.
                **Conclusion and Call to Action**: 
                  - Summary urging action on the policy topic.
                **Citations**:
                  - [Source Title, Author, Date](URL)
            """),
            agent=agent,
        )

    def review_brief(self, agent, policy_topic):
        return Task(
            description=dedent(f"""
                **Review and Refine Policy Brief on {policy_topic}**
                You are tasked with reviewing a draft policy brief related to {policy_topic}. This document is critical for influencing policy and must be clear, concise, and compelling. 
                **Your objectives are:**
                - Ensure the brief is coherent, presenting a logical flow of ideas.
                - Confirm the document is concise, avoiding unnecessary details while covering all critical aspects of the policy.
                - Verify the brief effectively communicates the policy analysis and recommendations.
                - Check for clarity and accuracy in the presentation of data and arguments.
                - Align the brief with policy advocacy goals, ensuring it persuades and motivates action.
                - Incorporate any necessary feedback for improvements to enhance persuasiveness and impact.
                **Your deliverables are:**
                - A final version of the policy brief, revised based on the above objectives.
            """),
            expected_output=dedent(f"""
                ## Policy Brief on {policy_topic}
                **Executive Summary**: 
                  - Highlights key points, challenges, and recommendations related to {policy_topic}.
                  - **Citations**:
                    - [Title of Source Article, Author, Publication Date](URL)
                **Current Status**: 
                  - Information on the current legislative or policy status concerning {policy_topic}.
                  - **Citations**:
                    - [Legislation on {policy_topic}, Government Department or Body](URL)
                **Background and Context**: 
                  - An overview of the issue underlying {policy_topic}.
                  - **Citations**:
                    - [Historical Context of {policy_topic}, Author, Publication](URL)
                **Analysis of the Issue**: 
                - A detailed examination of the main challenges related to {policy_topic}.
                - **Citations**:
                  - [Challenges Facing {policy_topic}, Expert Name, Think Tank or Research Institute](URL)
                **Opportunities for Improvement**: 
                - Outlines potential avenues for positive change within {policy_topic}.
                - **Citations**:
                  - [Innovations in {policy_topic}, Innovator or Researcher Name, Date](URL)
                **Proposed Solutions and Recommendations**: 
                - Lists detailed action plans or policy recommendations for {policy_topic}.
                - **Citations**:
                  - [Policy Solutions for {policy_topic}, Policy Analyst or Expert, Date](URL)
                **Conclusion and Call to Action**: 
                - A summary urging action on {policy_topic}.
                - **Citations**:
                  - [The Urgency of Action on {policy_topic}, Influential Figure or Organization](URL)
                **Unanswered Questions and Likelihood of Passage**: 
                - Insights into unresolved aspects and policy success chances.
                - **Citations**:
                  - [Forecasting Policy Outcomes for {policy_topic}, Forecaster Name, Publication Date](URL)
                **Recent News or Events**: 
                - The latest relevant developments related to {policy_topic}.
                - **Citations**:
                  - [Breaking News on {policy_topic}, News Source, Date](URL)
            """),
            agent=agent,
        )