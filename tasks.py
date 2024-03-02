from textwrap import dedent
from crewai import Task
from typing import List, Optional
from pydantic import BaseModel, Field

class PolicyResearch(BaseModel):
    policy_topic: str
    research_questions: List[str] = Field(..., description="Specific research questions guiding the investigation")
    current_status: List[str] = Field(..., description="Overview of the policy's current status and relevant debates")
    stakeholder_perspectives: List[str] = Field(..., description="Analysis of different stakeholders' views and opinions")
    evidence_base: List[str] = Field(..., description="Empirical evidence supporting various positions on the policy")
    key_findings: List[str] = Field(..., description="Summary of key insights and divergent viewpoints identified through research")

class PolicyLegislation(BaseModel):
    policy_topic: str
    external_factors: List[str] = Field(..., description="External factors like economic conditions and technological advancements affecting the policy")
    legislative_challenges: List[str] = Field(..., description="Main challenges within legislative debates")
    opportunities_for_policy: List[str] = Field(..., description="Opportunities for the policy within the current political and societal context")
    consensus_building_strategies: List[str] = Field(..., description="Strategies to build consensus among decision-makers")
    legislative_success_strategies: List[str] = Field(..., description="Actionable advice for enhancing the policy's legislative success")

class PolicyTasks:
    def research_policy_issues_task(self, agent, policy_topic, research_questions):
        return Task(
            description=dedent(f"""\
                Investigate the current status, debates, and evidence related to "{policy_topic}", focusing on specific research questions: "{research_questions}". 
                Collect and analyze recent developments, stakeholder opinions, and empirical evidence to grasp the policy's current situation and its potential impacts.
                Summarize the findings to highlight critical insights, conflicting views, and the evidence base supporting different perspectives to aid in policy brief formulation."""),
            expected_output=dedent("""\
                A comprehensive report synthesizing research on the policy topic, integrating data analysis, stakeholder perspectives, and recent studies. 
                This report aims to offer a robust evidence base for formulating policy briefs and recommendations, effectively addressing the specified research questions."""),
            agent=agent,
            output_pydantic=PolicyResearch
        )

    def decision_making_and_legislation_task(self, agent, policy_topic, external_factors):
        return Task(
            description=dedent(f"""\
                Evaluate how {external_factors} such as economic conditions, technological advancements, and public opinion trends affect the legislative process and decision-making for "{policy_topic}". 
                Examine the policy's main legislative challenges and opportunities, taking into account political dynamics, societal expectations, and recent news or events.
                Suggest strategies for navigating the legislative landscape, achieving consensus among policymakers, and optimizing the policy's chances of successful enactment."""),
            expected_output=dedent("""\
                A strategic framework that elucidates the relationship between external factors and the legislative progression of the policy. 
                This framework should provide pragmatic recommendations for addressing legislative challenges, engaging stakeholders, and leveraging opportunities to facilitate policy approval."""),
            agent=agent,
            output_pydantic=PolicyLegislation
        )

    def analyze_policy_options_task(self, agent, policy_topic):
        return Task(
            description=dedent(f"""\
                Based on the research conducted, analyze potential policy options for "{policy_topic}". 
                Evaluate the pros and cons of each option, considering effectiveness, feasibility, and potential impact. 
                Develop a set of evidence-based policy recommendations that align with policy objectives and societal needs."""),
            expected_output=dedent("""\
                A set of policy recommendations that are clearly justified with evidence and analysis, outlining the advantages and challenges of each proposed option. 
                Recommendations should align with overarching policy goals and societal benefits."""),
            agent=agent
        )

    def draft_policy_brief_task(self, agent, policy_topic, recommendations_summary):
        return Task(
            description=dedent(f"""\
                Draft a policy brief for "{policy_topic}" using the research findings and policy recommendations. 
                Start with an executive summary that encapsulates the issue and recommendations, followed by a detailed discussion on the policy context, analysis, and proposed recommendations. 
                Ensure the brief is concise, engaging, and persuasive, tailored to inform and influence policy stakeholders.
                Summary of recommendations: "{recommendations_summary}"""),
            expected_output=dedent("""\
                A well-structured policy brief that includes an executive summary, context analysis, and evidence-based recommendations. 
                The document should be engaging and persuasive, effectively communicating the policy issue and proposed solutions to stakeholders."""),
            agent=agent
        )

    def review_and_refine_policy_brief_task(self, agent, policy_topic):
        return Task(
            description=dedent(f"""\
                Review the draft policy brief on "{policy_topic}". 
                Ensure the document is coherent, concise, and effectively communicates the policy analysis and recommendations. 
                Check for clarity, accuracy, and alignment with policy advocacy goals. Refine the brief to enhance persuasiveness and impact, incorporating feedback for final revisions."""),
            expected_output=dedent("""\
                A polished, final version of the policy brief that is clear, compelling, and aligned with advocacy goals. 
                Feedback on improvements and final approval for dissemination. Formatted in markdown."""),
            agent=agent,
            output_file="output/policy_brief.md"
        )