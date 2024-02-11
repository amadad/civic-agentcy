import archive.instructor as instructor
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List

class Policy(BaseModel):
    name: str
    date: int
    fact: List[str] = Field(..., description="A list of facts about the policy")
    recommendations: List[str] = Field(..., description="A list of recommendations")
    stakeholders: List[str] = Field(..., description="A list of stakeholders")
    challenges: List[str] = Field(..., description="A list of challenges")
    objectives: List[str] = Field(..., description="The goals or objectives that the policy aims to achieve")
    expected_outcomes: List[str] = Field(..., description="The anticipated results of implementing the policy")
    legal_context: List[str] = Field(..., description="Legal and regulatory considerations relevant to the policy")
    impact: List[str] = Field(..., description="Potential positive and negative impacts of the policy")
    evaluation_criteria: List[str] = Field(..., description="Criteria for monitoring and evaluating the policy's effectiveness")
    funding_sources: List[str] = Field(..., description="Sources of funding for the policy's implementation")
    implementation_timeline: List[str] = Field(None, description="The timeline over which the policy is expected to be implemented")
    policy_instruments: List[str] = Field(..., description="The tools and methods used to implement the policy")
    prior_examples: List[str] = Field(..., description="Examples of similar policies implemented in other contexts")
    feedback_mechanisms: List[str] = Field(..., description="Mechanisms for collecting feedback from stakeholders and the public")

# enables `response_model` in create call
client = instructor.patch(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    ),
    mode=instructor.Mode.JSON,
)

resp = client.chat.completions.create(
    model="openhermes:latest",
    messages=[
        {
            "role": "user",
            "content": "Tell me about marijuana legalisation in michigan",
        }
    ],
    response_model=Policy,
)
print(resp.model_dump_json(indent=2))