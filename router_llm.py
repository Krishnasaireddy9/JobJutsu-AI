import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def choose_tool(user_input):
    prompt = f"""
You are a routing agent.

Available tools:
resume
jd
skill
interview

Return ONLY one tool name.

Examples:
Review my resume
Output: resume

Analyze my CV
Output: resume

Compare my resume with this job
Output: jd

How well does my resume fit this role?
Output: jd

What skills should I improve?
Output: skill

Generate interview questions
Output: interview

Generate interview questions based on the JD
Output: interview

Ask me AI Engineer interview questions
Output: interview

Mock interview
Output: interview

User:
{user_input}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    tool = response.text.strip().lower()

    if "resume" in tool:
        return "resume"
    elif "jd" in tool:
        return "jd"
    elif "skill" in tool:
        return "skill"
    elif "interview" in tool:
        return "interview"

    return "resume"