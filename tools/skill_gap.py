from pypdf import PdfReader
from ollama import chat

def skill_gap():

    reader = PdfReader("data/resume.pdf")

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text()

    prompt = f"""
    Based on this resume,
    suggest missing skills needed
    to become a strong AI Engineer.

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