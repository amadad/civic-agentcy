from crewai import Task
from textwrap import dedent

class PublicPolicyResearchTasks:
    def __init__(self):
        pass  # Initialize any necessary attributes
    
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def policy_analysis(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(f"""\
                               Conduct comprehensive research the policy's objectives, effectiveness,
                               and areas for improvement. Consider the impact on various stakeholders,
                               and the social, economic, and environmental implications.

                               {self.__tip_section()}

                               Analyze the policy area: {policy_area}.
                               Additional details provided: {policy_details}."""),
            expected_output=dedent(f"""\
                                   Your final report should offer a comprehensive evaluation of the policy,
                                   highlighting strengths, weaknesses, and recommendations for refinement or future direction."""),
            max_inter=3,
            agent=agent
        )

    def stakeholder_analysis(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(f"""\
                               Identify key stakeholders, their interests, positions, influence, and potential impact on policy outcomes.
                               Analyze how the policy affects different stakeholders and their likely responses.
                               
                               {self.__tip_section()}
                               
                               Conduct a stakeholder analysis for the policy area: {policy_area}.
                               Additional details provided: {policy_details}."""),
            expected_output=dedent("""\
                                   Your final report should map stakeholders, summarize their perspectives
                                   and suggest strategies for engagement or consensus-building."""),
            max_inter=3,
            agent=agent
        )
    
    def policy_recommendation(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(f"""
                               Propose actionable, evidence-based policy changes or interventions.
                               Include rationale, expected outcomes, and considerations for implementation.
                               
                               {self.__tip_section()}
                               
                               Policy area: {policy_area}
                               Additional details provided: {policy_details}."""),    
            expected_output=dedent("""\
                                   Your recommendations should be clear, targeted, and feasible,
                                   with a focus on addressing identified issues or capitalizing on opportunities."""),
            max_inter=3,
            agent=agent
        )
    
    def legislative_briefing(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(f"""\
                               Prepare a legislative briefing that condenses essential findings, strategic analysis, and actionable 
                               recommendations specifically for legislative stakeholders. Emphasize the implications of the policy for 
                               law-making, regulatory adjustments, and the critical need for legislative intervention or reform.
                               
                               {self.__tip_section()}
                               
                               Policy area: {policy_area}
                               Additional details provided: {policy_details}."""),            
            expected_output=dedent("""\
                                   Your briefing should be concise, persuasive, and accessible,
                                   specifically designed to guide legislative decisions and foster policy advancements."""),
            max_inter=3,
            agent=agent
    )  
    
    def implementation_plan(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(f"""\
                               Develop a detailed implementation plan that outlines how to operationalize the key findings and recommendations 
                               within the specified policy area. This plan should identify actionable steps, potential barriers to implementation, 
                               and strategies for addressing these challenges.
                               
                               {self.__tip_section()}
                               
                               Policy area: {policy_area}
                               Additional details provided: {policy_details}."""),    
            expected_output=dedent("""\
                               Your plan should be comprehensive, structured, and actionable,
                               providing a clear roadmap for executing policy objectives and ensuring impactful decision-making."""),
            max_inter=3,
            agent=agent
    ) 
    
    def summary_and_briefing_task(self, agent, policy_area, policy_details):
        return Task(
            description=dedent(f"""\
                               Compile all the policy analysis, stakeholder analysis, policy recommendation, legislative briefing, 
                               and implementation plan points into a concise, comprehensive briefing document.

                               Ensure the briefing is easy to digest and comprehesive to equip
                               participants with all necessary information and strategies.
                               
                               Policy area: {policy_area}
                               Additional details provided: {policy_details}."""),    
            expected_output=dedent("""\
                                   A well-structured briefing document that includes an executive summary
                                   and sections for each of the areas: policy analysis, stakeholder analysis, policy recommendation, legislative briefing, 
                                   and implementation plan"""),
            agent=agent
        )