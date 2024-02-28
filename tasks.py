from textwrap import dedent
from crewai import Task

class PolicyTasks:
    def research_policy_issues_task(self, agent, policy_topic, research_questions):
        return Task(
            description=dedent(f"""\
                Investigate the current debates and evidence surrounding "{policy_topic}", focusing on specific research questions: "{research_questions}". 
                Collect and analyze data, studies, and expert opinions to understand the policy's implications, stakeholders' perspectives, and the evidence base.
                Summarize the findings, highlighting key insights, divergent viewpoints, and the evidence supporting various positions to inform policy development."""),
            expected_output=dedent("""\
                A detailed report that synthesizes research on the policy issue, incorporating data analysis, expert perspectives, and study outcomes. 
                The report aims to provide a solid evidence base for crafting policy briefs and recommendations, addressing the posed research questions."""),
            agent=agent
        )
    
    def decision_making_and_legislation_task(self, agent, policy_topic, external_factors):
        return Task(
            description=dedent(f"""\
                Assess how {external_factors} like economic conditions and technological advancements influence the legislative process for "{policy_topic}". 
                Identify the main challenges and opportunities for the policy within legislative debates, considering political and societal contexts.
                Propose strategies to navigate the legislative environment, build consensus among decision-makers, and enhance the policy's legislative success."""),
            expected_output=dedent("""\
                A strategic report outlining the interplay between external factors and the policy's journey through the legislative process. 
                The report should offer actionable advice for overcoming barriers, engaging with key stakeholders, and improving the chances of policy enactment."""),
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
            agent=agent,
            output_file="policy_brief.md"
        )