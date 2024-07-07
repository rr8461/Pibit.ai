import openai

openai.api_key = "sk-proj-Ay63pvW8bZ4FhhDxFgGXT3BlbkFJRRHlI9awhILJ9gvNRCIl"

resume_content = """
[Paste your resume content here]
"""

prompt = f"""
Please parse the following resume content into a structured JSON format. Each section should be appropriately labeled, such as "contact_info", "education", "experience", "skills", etc.

Resume Content:
{resume_content}

Expected JSON format:
{{
  "contact_info": {{
    "name": "",
    "email": "",
    "phone": "",
    "address": ""
  }},
  "education": [
    {{
      "degree": "",
      "institution": "",
      "graduation_year": "",
      "details": ""
    }}
  ],
  "experience": [
    {{
      "job_title": "",
      "company": "",
      "start_date": "",
      "end_date": "",
      "responsibilities": ""
    }}
  ],
  "skills": [
    ""
  ],
  "certifications": [
    {{
      "name": "",
      "institution": "",
      "year": ""
    }}
  ],
  "projects": [
    {{
      "title": "",
      "description": "",
      "technologies": ""
    }}
  ]
}}
"""

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=500
)

print(response.choices[0].text.strip())
