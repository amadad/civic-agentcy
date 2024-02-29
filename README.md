# Civic Agentcy 🗳️

## Overview

**Civic Agentcy** is a comprehensive framework designed to automate the process of analyzing public policies, engaging stakeholders, preparing legislative briefings, developing policy recommendations, and compiling detailed reports. Utilizing a combination of advanced language models and web scraping tools, this project aims to provide in-depth insights that guide policy formulation, refinement, and implementation planning.

**Civic Agentcy** is a sophisticated framework designed for public policy analysis and development, characterized by:

* **Automated Policy Analysis**: Utilizes advanced language models to analyze and evaluate policies.
* **Stakeholder Engagement**: Streamlines the process of identifying and engaging key stakeholders.
* **Legislative Briefing Preparation**: Facilitates the creation of briefings for policymakers.
* **Policy Recommendations**: Generates actionable, evidence-based recommendations.
* **Report Compilation**: Compiles in-depth reports, enhancing policy formulation and implementation.

This framework empowers policymakers with data-driven insights, optimizing the public policy lifecycle.

## Custom Agents

The **Civic Agentcy** framework is equipped with a suite of custom agents designed to streamline and enhance the policy analysis and development process. Each agent is specialized in a specific aspect of policy work, leveraging advanced tools and methodologies to deliver high-quality outcomes.

* **Policy Researcher**: This agent is tasked with investigating current policy issues, trends, and evidence through comprehensive web and database searches. It gathers relevant data and insights, utilizing tools like `you_search` to navigate complex policy landscapes.
* **Policy Writer**: The Policy Writer agent is skilled in crafting detailed, engaging, and impactful policy briefs. It uses insights from the Policy Researcher and employs tools such as `perplexity_search`, `search_internet`, and `file_read_tool` to articulate insights, key trends, and evidence-based recommendations.
* **Policy Brief Reviewer**: This agent critically reviews draft policy briefs for coherence, alignment with policy objectives, evidence strength, and persuasive clarity. It refines content to ensure high-quality, impactful communication, utilizing `search_internet` and `file_read_tool` to verify information and ensure accuracy.

## Tasks

The Civic Agentcy framework is designed to automate and streamline various tasks related to public policy analysis and development. These tasks are crucial for comprehensive policy formulation, refinement, and implementation planning.

* **Research Policy Issues**: Investigates the current status, debates, and evidence related to a specified policy topic, focusing on specific research questions. This task collects and analyzes relevant data and insights to provide a robust evidence base for policy brief formulation.
* **Decision Making and Legislation**: Evaluates how external factors affect the legislative process and decision-making for a policy topic. It examines the policy's main legislative challenges and opportunities, suggesting strategies for navigating the legislative landscape.
* **Analyze Policy Options**: Based on the research conducted, analyzes potential policy options for a policy topic. This task evaluates the pros and cons of each option, considering effectiveness, feasibility, and potential impact.
* **Draft Policy Brief**: Drafts a policy brief for a policy topic using the research findings and policy recommendations. The brief includes an executive summary, context analysis, and evidence-based recommendations, aiming to be concise, engaging, and persuasive.
* **Review and Refine Policy Brief**: Reviews the draft policy brief, ensuring the document is coherent, concise, and effectively communicates the policy analysis and recommendations. This task involves refining the brief to enhance persuasiveness and impact, incorporating feedback for final revisions.

This project utilizes the [CrewAI](https://www.crewai.io) powered by [LangChain](https://www.langchain.com) to define agents and tasks that automate the analysis and reporting process. 

## Roadmap

- [x] Integrate [Exa Search](http://exa.ai) for enhanced realtime search capabilities
- [x] Embeddings and vector search for improved policy analysis
- [x] Enable PDF/text document uploads for policy references.
- [x] Link user accounts for easy access to documents via Google Drive Integration.
- [x] Incorporate real-time notes and collaboration features with Meeting Notes Integration.
- [x] Distinguish between public and internal documents for clarity with Context Balancing

--

## Contributing

Contributions to the **Civic Agentcy** are welcome. Please ensure to follow the project's code standards and submit pull requests for review. Contact [Ali Madad](mailto:ali@scty.org) for any questions or issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details