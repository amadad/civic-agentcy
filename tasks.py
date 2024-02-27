from textwrap import dedent
from crewai import Task

class PolicyTasks:
    def research_policy_issues_task(self, agent, policy_topic, research_questions):
        return Task(
            description=dedent(f"""\
                Investigate current policy debates and evidence on "{policy_topic}". Address the research questions: "{research_questions}". 
                Gather relevant data, studies, and expert opinions to understand the scope, impact, and perspectives related to the policy issue.
                Compile a report summarizing key findings, data insights, and expert viewpoints to inform the policy brief."""),
            expected_output=dedent("""\
                A comprehensive report detailing findings on the policy topic, including data insights, expert opinions, and relevant studies. 
                This report should lay the foundation for developing informed and evidence-based policy recommendations."""),
            agent=agent
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
            agent=agent
        )

    def industry_and_policy_impact_analysis_task(self, agent, policy_topic, external_factors):
        return Task(
            description=dedent(f"""\
                Conduct a comprehensive analysis of how external factors such as economic trends, societal issues, and technological advancements impact the policy topic: "{policy_topic}". 
                Evaluate the interaction between these factors and the policy landscape, identifying potential challenges and opportunities for policy implementation.
                Analyze how the policy could influence industry practices, societal norms, and technological innovation. 
                Include insights on leveraging these impacts to strengthen the policy recommendations and their expected outcomes."""),
            expected_output=dedent("""\
                An in-depth analysis report that highlights the interplay between the policy topic and external factors. 
                The report should offer strategic insights on enhancing the policy's effectiveness and leveraging industry, societal, and technological trends to support policy objectives."""),
            agent=agent
        )
