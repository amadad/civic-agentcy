from crewai import Task
from textwrap import dedent
from pydantic import BaseModel, Field
from typing import List, Optional

class Policy(BaseModel):
    name: str
    date: Optional[int] = None
    facts: List[str] = Field(..., description="Key facts about the policy, including background and rationale")
    objectives: List[str] = Field(..., description="The goals or objectives that the policy aims to achieve")
    stakeholders: List[str] = Field(..., description="A list of stakeholders involved in or affected by the policy")
    strategies: List[str] = Field(..., description="Strategies and activities planned to achieve the objectives")
    challenges_and_solutions: List[str] = Field(..., description="Identified challenges and proposed solutions or mitigations")
    expected_outcomes: List[str] = Field(..., description="The anticipated short-term and long-term results of implementing the policy")
    impact_assessment: List[str] = Field(..., description="Analysis of potential positive and negative impacts, including on legal and regulatory contexts")
    evaluation_and_feedback: List[str] = Field(..., description="Criteria and mechanisms for evaluating the policy's effectiveness and collecting stakeholder feedback")
    resources: List[str] = Field(..., description="Overview of funding sources and other resources necessary for implementation")
    timeline_and_milestones: List[str] = Field(None, description="The implementation timeline and key milestones")
    examples_and_precedents: List[str] = Field(..., description="References to similar policies or precedents that inform the current policy")

class TheoryOfChange(BaseModel):
    policy_name: str
    policy_area: str
    development_date: Optional[int] = None
    underlying_assumptions: List[str] = Field(..., description="Key assumptions underlying the policy's theory of change")
    long_term_goals: List[str] = Field(..., description="The ultimate goals the policy aims to achieve in the long term")
    short_term_outcomes: List[str] = Field(..., description="Expected short-term outcomes that lead towards the long-term goals")
    intermediate_outcomes: List[str] = Field(..., description="Mid-term outcomes that serve as milestones towards achieving long-term goals")
    activities: List[str] = Field(..., description="Key activities or interventions planned to achieve the outcomes")
    inputs: List[str] = Field(..., description="Resources and inputs required to carry out the activities")
    stakeholders_involved: List[str] = Field(..., description="Stakeholders involved in or affected by the policy")
    contextual_factors: List[str] = Field(..., description="External factors that could influence the policy's success")
    indicators_of_success: List[str] = Field(..., description="Metrics and indicators used to measure the progress and success of the policy")
    barriers_to_success: List[str] = Field(..., description="Potential obstacles or challenges that could impede policy success")
    strategies_for_scaling: List[str] = Field(..., description="Strategies for scaling the policy's impact")
    mechanisms_for_adaptation: List[str] = Field(..., description="Mechanisms in place for adapting the policy based on feedback and changing circumstances")
    evidence_base: List[str] = Field(..., description="Evidence or research supporting the policy's approach")
    feedback_loops: List[str] = Field(..., description="Processes for collecting and integrating feedback from stakeholders and monitoring outcomes")
    evaluation_plan: List[str] = Field(..., description="Plan for evaluating the policy's effectiveness and impact over time")

class PublicPolicyResearchTasks:
    def policy_analysis(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(f"""\
                               Conduct comprehensive research the policy's objectives, effectiveness,
                               and areas for improvement. Consider the impact on various stakeholders,
                               and the social, economic, and environmental implications.
                               Analyze the policy area: {policy_area}.
                               Additional details provided: {policy_details}."""),
            expected_output="Your final report should label and summarize the analysis. Formatted in markdown.",
            max_inter=2,
            agent=agent,
            output_pydantic=Policy,
            output_file= "output/policy_analysis.md"
        )

    def change_analysis(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(f"""\
                               Craft a strategic framework for a {policy_area} in {policy_details} using the TheoryOfChange class. 
                               Specify the policy's name, area, and development date to provide a foundational overview. Identify underlying 
                               assumptions and define clear long-term goals, alongside short-term and intermediate outcomes that act as progress 
                               markers. Outline planned activities, required resources, and stakeholder analysis, including their influence and 
                               potential responses. Consider external factors affecting the policy's success and detail strategies for overcoming barriers. 
                               Establish success metrics, adaptation mechanisms, and evidence supporting the policy's approach. Incorporate 
                               feedback loops for ongoing evaluation and adjustment, ensuring a comprehensive plan for achieving and evaluating 
                               the policy's impact."""),
            expected_output="Your final report should label and summarize the analysis. Formatted in markdown.",
            max_inter=2,
            agent=agent,
            output_pydantic=TheoryOfChange,
            output_file= "output/change_analysis.md"
        )
    
    def policy_brief(self, agent, policy_analysis, change_analysis):
        return Task(
            description=f"Convert JSON {policy_analysis} and {change_analysis} to markdown. Include an executive summary.",
            expected_output=dedent("""\
                                   A well-structured briefing document that includes sections for: 
                                   #Policy Identification: name, policy_name, date, development_date, policy_area,
                                   #Executive Summary: 2 paragraph summary,
                                   #Analysis and Objectives: facts, objectives, long_term_goals, underlying_assumptions,
                                   #Stakeholders: stakeholders, stakeholders_involved,
                                   #Strategic Planning: strategies, strategies_for_scaling, activities, inputs,
                                   #Challenges and Solutions: challenges_and_solutions, barriers_to_success, mechanisms_for_adaptation,
                                   #Outcomes and Impacts: expected_outcomes, short_term_outcomes, intermediate_outcomes, impact_assessment,
                                   #Evaluation and Feedback: evaluation_and_feedback, indicators_of_success, feedback_loops, evaluation_plan,
                                   #Resources and Implementation: resources, timeline_and_milestones,
                                   #Additional Considerations: examples_and_precedents, contextual_factors, evidence_base
                                   """),
            agent=agent,
            output_file= "output/final_brief.md"
)