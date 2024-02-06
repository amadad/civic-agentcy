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
            async_execution=True,
            max_inter=3,
            agent=agent
        )

    def stakeholder_analysis(self, agent, policy_area, stakeholder_details):
        return Task(
            description=dedent(f"""\
                               Identify key stakeholders, their interests, positions, influence, and potential impact on policy outcomes.
                               Analyze how the policy affects different stakeholders and their likely responses.
                               
                               {self.__tip_section()}
                               
                               Conduct a stakeholder analysis for the policy area: {policy_area}.
                               Stakeholder details: {stakeholder_details}."""),
            expected_output=dedent("""\
                                   Your final report should map stakeholders, summarize their perspectives
                                   and suggest strategies for engagement or consensus-building."""),
            async_execution=True,
            max_inter=3,
            agent=agent
        )
    
    def policy_recommendation(self, agent, policy_area, analysis_details):
        return Task(
            description=dedent(f"""
                               Develop policy recommendations based on your analysis of: {policy_area}.
                               Analysis insights: {analysis_details}.
                               
                               Propose actionable, evidence-based policy changes or interventions.
                               Include rationale, expected outcomes, and considerations for implementation.
                               
                               {self.__tip_section()}
                               
                               Policy area: {policy_area}
                               Analysis details: {analysis_details}"""),       
            expected_output=dedent("""\
                                   Your recommendations should be clear, targeted, and feasible,
                                   with a focus on addressing identified issues or capitalizing on opportunities."""),
            max_inter=3,
            agent=agent
        )
    
    def legislative_briefing(self, agent, policy_area, briefing_details):
        return Task(
            description=dedent(f"""\
                               Summarize key findings, analysis, and recommendations in a format suitable for policymakers.
                               Highlight the policy's importance, implications, and the urgency for action or revision.
                               
                               {self.__tip_section()}

                               Policy area: {policy_area}
                               Briefing details: {briefing_details}"""),          
            expected_output=dedent("""\
                                   Your briefing should be concise, persuasive, and accessible,
                                   aimed at informing decision-making and advancing policy objectives."""),
            max_inter=3,
            agent=agent
        ) 
    
    def implementation_plan(self, agent, policy_area, briefing_details):
        return Task(
            description=dedent(f"""\
                               Summarize key findings, analysis, and recommendations in a format suitable for policymakers.
                               Highlight the policy's importance, implications, and the urgency for action or revision.
                               {self.__tip_section()}
                               Policy area: {policy_area}
                               Briefing details: {briefing_details}"""),   
            expected_output=dedent("""\
                                   Your briefing should be comprehensive, structured, persuasive, and accessible,
                                   aimed at informing decision-making and advancing policy objectives."""),
            max_inter=3,
            agent=agent
        ) 
    
    def summary_and_briefing_task(self, agent, completed_tasks, policy_area, policy_details):
        # Filter out None values from task outputs before joining
        tasks_outputs = "\n".join([task.output for task in completed_tasks if task.output is not None])

        # Check if tasks_outputs is empty and provide a placeholder message if so
        if not tasks_outputs:
            tasks_outputs = "No outputs available from completed tasks."

        return Task(
            description=dedent(f"""\
                               Compile all the research findings, industry analysis, and strategic
                               talking points into a concise, comprehensive briefing document for
                               the meeting.
                               Ensure the briefing is easy to digest and equips the meeting
                               participants with all necessary information and strategies.
                               Policy area: {policy_area}
                               Details provided: {policy_details}
                               Briefing includes outputs from the following tasks:
                               {tasks_outputs}"""),
            expected_output="A comprehensive briefing document",
            agent=agent
        )