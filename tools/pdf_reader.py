from pypdf import PdfReader

def get_resume_text():

    reader = PdfReader("data/resume.pdf")

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text