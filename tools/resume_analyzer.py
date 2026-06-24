from pypdf import PdfReader
from ollama import chat

def analyze_resume():

    reader = PdfReader("data/resume.pdf")

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text()

    prompt = f"""
    Analyze this resume.

    Provide:

    1. Summary
    2. Strengths
    3. Weaknesses
    4. Suggested Roles

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