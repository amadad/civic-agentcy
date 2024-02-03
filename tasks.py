from crewai import Task
from textwrap import dedent

class PublicPolicyResearchTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def policy_analysis(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(
                f"""
            Analyze the policy area: {policy_area}.
            Additional details provided: {policy_details}.

            Focus on understanding the policy's objectives, effectiveness,
            and areas for improvement. Consider the impact on various stakeholders,
            and the social, economic, and environmental implications.

            Your final report should offer a comprehensive evaluation of the policy,
            highlighting strengths, weaknesses, and recommendations for refinement or future direction.
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
    
            Use these variable: {policy_area} and {policy_details}.
        """
            ),
            agent=agent,
        )

    def stakeholder_analysis(self, agent, policy_area, stakeholder_details):
        return Task(
            description=dedent(
                f"""
            Conduct a stakeholder analysis for the policy area: {policy_area}.
            Stakeholder details: {stakeholder_details}.
            
            Identify key stakeholders, their interests, positions, influence, and potential impact on policy outcomes.
            Analyze how the policy affects different stakeholders and their likely responses.
            
            Your final report should map stakeholders, summarize their perspectives,
            and suggest strategies for engagement or consensus-building.
                                       
            {self.__tip_section()}

            Use these variable: {policy_area} and {stakeholder_details}.
        """
            ),
            agent=agent,
        )
    
    def policy_recommendation(self, agent, policy_area, analysis_details):
        return Task(
            description=dedent(
                f"""
            Develop policy recommendations based on your analysis of: {policy_area}.
            Analysis insights: {analysis_details}.
            
            Propose actionable, evidence-based policy changes or interventions.
            Include rationale, expected outcomes, and considerations for implementation.
            
            Your recommendations should be clear, targeted, and feasible,
            with a focus on addressing identified issues or capitalizing on opportunities.
                                       
            {self.__tip_section()}

            Use these variable: {policy_area} and {analysis_details}.
        """
            ),
            agent=agent,
        )
    
    def legislative_briefing(self, agent, policy_area, briefing_details):
        return Task(
            description=dedent(
                f"""
            Prepare a legislative briefing for the policy area: {policy_area}.
            Briefing details: {briefing_details}.
            
            Summarize key findings, analysis, and recommendations in a format suitable for policymakers.
            Highlight the policy's importance, implications, and the urgency for action or revision.
            
            Your briefing should be concise, persuasive, and accessible,
            aimed at informing decision-making and advancing policy objectives.
                                       
            {self.__tip_section()}

            Use these variable: {policy_area} and {briefing_details}.
        """
            ),
            agent=agent,
        ) 
    
    def implementation_plan(self, agent, policy_recommendation, plan_details):
        return Task(
            description=dedent(
                f"""
            Prepare a legislative briefing for the policy area: {policy_recommendation}.
            Briefing details: {plan_details}.
            
            Summarize key findings, analysis, and recommendations in a format suitable for policymakers.
            Highlight the policy's importance, implications, and the urgency for action or revision.
            
            Your briefing should be concise, persuasive, and accessible,
            aimed at informing decision-making and advancing policy objectives.
                                       
            {self.__tip_section()}

            Use these variable: {policy_recommendation} and {plan_details}.
        """
            ),
            agent=agent,
        ) 