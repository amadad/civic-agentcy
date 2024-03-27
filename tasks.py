from textwrap import dedent
from crewai import Task
from typing import List
from pydantic import BaseModel, Field

class PolicyResearch(BaseModel):
    policy_topic: str
    research_questions: List[str] = Field(..., description="Specific research questions guiding the investigation")
    current_status: List[str] = Field(..., description="Overview of the policy's current status and relevant debates")
    stakeholder_perspectives: List[str] = Field(..., description="Analysis of different stakeholders' views and opinions")
    evidence_base: List[str] = Field(..., description="Empirical evidence supporting various positions on the policy")
    key_findings: List[str] = Field(..., description="Summary of key insights and divergent viewpoints identified through research")

class PolicyTasks:
    def research_policy(self, agent, policy_topic: str, research_questions: List[str]):
        return Task(
            description=dedent(f"""\
                **Research Policy Issues**
                - **Policy Topic**: {policy_topic}
                - **Research Questions**: {', '.join(research_questions)}
                Conduct a comprehensive investigation on the current status, debates, and evidence related to the policy topic. 
                Analyze stakeholder perspectives and empirical evidence to formulate a detailed report.
                """),
            expected_output=dedent("""\
                **Expected Markdown Formatted Output:**
                ## Executive Summary
                Summarize key points, challenges, and recommendations.

                ## Current Status
                Discuss whether the policy is passed, being discussed, debated, or scheduled for a vote.

                ## Background and Context
                Provide detailed background information on the policy issue.

                ## Analysis of the Issue
                Outline main challenges and barriers.

                ## Opportunities for Improvement
                Highlight opportunities for positive change.

                ## Proposed Solutions and Recommendations
                Detail action plans and strategies.

                ## Conclusion and Call to Action
                Conclude with a summary of key points and a call to action.

                ## Unanswered Questions and Likelihood of Passage
                Discuss unresolved issues and the policy's likelihood of success.

                ## Recent News or Events
                Provide updates on relevant news or events.

                Format the deliverable as a structured Markdown document, ensuring clarity and effective communication.
                """),
            agent=agent,
            output_pydantic=PolicyResearch,
        )

    def analyze_policy(self, agent, policy_topic):
        return Task(
            description=dedent(f"""\
                Based on the research conducted, analyze potential policy options for "{policy_topic}". 
                Evaluate the pros and cons of each option, considering effectiveness, feasibility, and potential impact. 
                Develop a set of evidence-based policy recommendations that align with policy objectives and societal needs.
                """),
            expected_output=dedent("""\
                # Policy Options Analysis for "{policy_topic}"

                ## Introduction
                This section presents an overview of the policy options considered for addressing the issues identified within the policy area of "{policy_topic}". 

                ## Policy Option 1: [Option Name]
                ### Pros
                - Benefit 1
                - Benefit 2
                ### Cons
                - Challenge 1
                - Challenge 2

                ## Policy Option 2: [Option Name]
                ### Pros
                - Benefit 1
                - Benefit 2
                ### Cons
                - Challenge 1
                - Challenge 2

                # Recommendations
                Based on the analysis, the following recommendations are proposed:
                1. **Recommendation 1**: [Brief Description]
                2. **Recommendation 2**: [Brief Description]

                Each recommendation is supported by the analysis of policy options, aimed at aligning with the overarching goals of [policy objectives] and addressing societal needs effectively.
                """),
            agent=agent,
        )

    def draft_brief(self, agent, policy_topic, recommendations_summary):
        return Task(
            description=dedent(f"""\
                Draft a policy brief for "{policy_topic}" using the research findings and policy recommendations. 
                Start with an executive summary that encapsulates the issue and recommendations, followed by a detailed discussion on the policy context, analysis, and proposed recommendations. 
                Ensure the brief is concise, engaging, and persuasive, tailored to inform and influence policy stakeholders.
                Summary of recommendations: "{recommendations_summary}"
                """),
            expected_output=dedent("""\
                # Executive Summary
                A brief overview highlighting key points, challenges, opportunities, and recommendations regarding the policy.
                # Current Status
                Details on the policy's current status, including whether it's passed, under discussion, debated, or scheduled for a vote.
                # Introduction
                ## Background and Context
                Provides a detailed overview of the policy's history, current situation, and key stakeholders.
                ## Objective of the Policy Brief
                Defines the brief's purpose, goals, and scope, setting the stage for the reader's expectations.
                # Analysis of the Issue
                ## Challenges and Barriers
                Identifies main obstacles to the policy's success, including specific challenges and potential impacts.
                ## Opportunities for Improvement
                Presents possibilities for positive changes, including potential benefits and strategies for realization.
                # Proposed Solutions and Recommendations
                Details a step-by-step action plan with responsible parties, timeline, and milestones. Discusses policy reform or intervention strategies and expected outcomes.
                # Conclusion and Call to Action
                Reiterates key points and benefits of the proposed solutions, encouraging stakeholder commitment.
                # Unanswered Questions and Likelihood of Passage
                Discusses significant unresolved issues and analyzes the policy's chances of success.
                # Recent News or Events
                Covers the latest news or events relevant to the policy, providing updates on developments, stakeholder reactions, or shifts in public opinion.
                **This policy brief aims to inform, persuade, and guide stakeholders, offering a comprehensive analysis for decision-making and advocacy.**
                """),
            agent=agent,
        )

    def review_brief(self, agent, policy_topic):
        return Task(
            description=dedent(f"""\
                **Review and Refine Policy Brief on "{policy_topic}"**

                You are tasked with reviewing a draft policy brief related to "{policy_topic}". This document is critical for influencing policy and must be clear, concise, and compelling. 

                **Your objectives are:**
                - Ensure the brief is coherent, presenting a logical flow of ideas.
                - Confirm the document is concise, avoiding unnecessary details while covering all critical aspects of the policy.
                - Verify the brief effectively communicates the policy analysis and recommendations.
                - Check for clarity and accuracy in the presentation of data and arguments.
                - Align the brief with policy advocacy goals, ensuring it persuades and motivates action.
                - Incorporate any necessary feedback for improvements to enhance persuasiveness and impact.

                **Your deliverables are:**
                - A final version of the policy brief, revised based on the above objectives.
                - Feedback on specific improvements made and any areas that required significant changes.
                """),
            expected_output=dedent("""\
                # Final Version of Policy Brief on "{policy_topic}"

                ## Executive Summary
                - A concise summary that captures the essence of the policy issues, analysis, and recommendations.

                ## Analysis of the Issue
                - Detailed analysis that is clear, accurate, and logically structured.

                ## Proposed Solutions and Recommendations
                - Well-formulated recommendations that are compelling and aligned with advocacy goals.

                ## Conclusion and Call to Action
                - A strong closing section that reiterates the key points and urges stakeholders to act.

                ## Feedback Summary
                - Specific improvements made during the review process.
                - Areas that required significant refinement for clarity, conciseness, and impact.

                The document should be formatted in Markdown to ensure proper structure and readability.
                """),
            agent=agent,
            output_file="output/policy_brief_final.md",
        )