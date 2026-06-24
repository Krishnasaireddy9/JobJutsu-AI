from pypdf import PdfReader
from ollama import chat

def match_resume_jd():

    reader = PdfReader("data/resume.pdf")

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text()

    with open(
        "data/jd.txt",
        "r",
        encoding="utf-8"
    ) as file:

        jd_text = file.read()

    prompt = f"""
    Compare the resume and job description.

    Provide:

    1. Match Score
    2. Matching Skills
    3. Missing Skills
    4. Hiring Recommendation

    Resume:
    {resume_text}

    Job Description:
    {jd_text}
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