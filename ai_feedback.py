from groq import Groq

client = Groq(
    api_key="GROQ_API_KEY"
)

def get_feedback(job_description, resume_text):

    prompt = f"""
You are an expert HR recruiter.

Compare the resume against the job description.

Job Description:
{job_description}

Resume:
{resume_text}

Provide your response exactly in this format.

Match Summary:
(2-3 sentences)

Strengths:
- Bullet 1
- Bullet 2
- Bullet 3

Missing Skills:
- Bullet 1
- Bullet 2
- Bullet 3

Recommendation:
(One short paragraph)

Keep the response professional and under 180 words.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=400
    )

    return response.choices[0].message.content

    



    