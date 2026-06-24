from pypdf import PdfReader
from ollama import chat

def generate_questions():

    reader = PdfReader("data/resume.pdf")

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text()

    prompt = f"""
You are a Senior AI Engineering Interviewer.

Generate 10 interview questions.

Rules:
- Only use technologies explicitly present in the resume.
- Do not invent technologies.
- Do not ask about skills not mentioned in the resume.
- Include:
  - 4 project-based questions
  - 3 machine learning questions
  - 2 Python questions
  - 1 behavioral question

Resume:

{resume_text}
"""

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]