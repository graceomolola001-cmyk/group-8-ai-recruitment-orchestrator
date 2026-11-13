from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import List
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)


class ScreeningInput(BaseModel):
    candidateId: str
    resumeText: str
    jobDescription: str
    matchedSkills: List[str]
    missingSkills: List[str]
    experienceAlignment: str

class ScreeningQuestion(BaseModel):
    id: str
    question: str
    competency: str

class ScreeningOutput(BaseModel):
    candidateId: str
    questions: List[ScreeningQuestion] = Field(
        min_length=8,
        max_length=8
    )

    @model_validator(mode="after")
    def validate_question_ids(self):
        expected_ids = [f"Q{i}" for i in range(1, 9) ]
        actual_ids = [question.id for question in self.questions]

        if actual_ids != expected_ids:
            raise ValueError(
                "Question IDs must be unique and ordered from Q1 to Q8."
            )
        return self

    @model_validator(mode="after")
    def validate_competency_coverage(self):
        required_competencies = {
            "Technical skill depth",
            "Practical application and problem-solving",
            "Relevant experience",
            "Alignment with the job",
            "Missing skills and ability to learn",
            "Continuous learning",
            "Teamwork and collaboration",
            "Overall competency through a practical scenario"
        }

        actual_competencies = {
            question.competency
            for question in self.questions
        }

        missing_competencies = (
            required_competencies - actual_competencies
        )

        if missing_competencies:
            raise ValueError(
                f"Missing required competencies: {missing_competencies}"
            )

        return self

screening_prompt = PromptTemplate( input_variables=[ "candidateId", "resumeText", "jobDescription", "matchedSkills", "missingSkills", "experienceAlignment" ], template=""" You are an expert technical recruiter conducting an initial candidate screening.
    Your task is to generate exactly 8 screening questions based specifically on the candidate's background and the job requirements.
    Candidate ID: {candidateId}
    Candidate Resume: {resumeText}
    Job Description: {jobDescription}
    Matched Skills: {matchedSkills}
    Missing Skills: {missingSkills}
    Experience Alignment: {experienceAlignment}
    The questions should assess:
    Technical skill depth
    Practical application and problem-solving
    Relevant experience
    Alignment with the job
    Missing skills and ability to learn
    Continuous learning
    Teamwork and collaboration
    Overall competency through a practical scenario

    Generate exactly one question for each of the eight competencies listed above.

    Use the exact competency labels provided in the list. Do not rename, abbreviate, or paraphrase them.

    Each question must assess a different primary competency. Do not assign the same competency to multiple questions.

    Return exactly eight questions, with IDs ordered from Q1 to Q8. Ensure that every required competency appears exactly once.

    Questions should be specific to this candidate and role, not generic interview questions.

    Use only the information provided in the candidate's resume and job context.

    Do not assume the candidate has worked on specific projects, handled
    production incidents, used particular tools, or performed responsibilities
    unless the supplied information supports those claims.

    When the resume does not establish relevant experience, ask a hypothetical
    question or invite the candidate to describe a relevant example if they
    have one.

    Use the matched skills, missing skills, and experience alignment to tailor
    the questions to the candidate and the job requirements.

    Do not invent candidate qualifications or treat missing information as
    proof that the candidate lacks a skill.
    
    Return exactly 8 questions.
    
    For every question, provide:
    - id: A unique question identifier, starting with Q1 and ending with Q8.
    - question: The complete screening question.
    - competency: the competency being assessed.
    
    Return the candidate ID as well as the list of questions. """ )

structured_llm = llm.with_structured_output(ScreeningOutput)
chain = screening_prompt | structured_llm

candidate = ScreeningInput(
    candidateId="CAND-001",
    resumeText="Python developer with 3 years of backend experience.",
    jobDescription="Looking for a Python backend developer.",
    matchedSkills=["Python", "SQL"],
    missingSkills=["Docker"],
    experienceAlignment="Strong"
)


try: 
    response = chain.invoke({ 
        "candidateId": candidate.candidateId,
        "resumeText": candidate.resumeText,
        "jobDescription": candidate.jobDescription,
        "matchedSkills": ", ".join(candidate.matchedSkills),
        "missingSkills": ", ".join(candidate.missingSkills),
        "experienceAlignment": candidate.experienceAlignment
    })
    print(response.model_dump_json(indent=2))

except ValidationError as error:
    print("The generated screening questions failed validation.")
    print(error)

except Exception as error:
    print("An error occurred while generating screening questions.")
    print(error)