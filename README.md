# AI Resume Screening Agent

An AI-powered Resume Screening Agent that ranks resumes against a Job Description using semantic embeddings and generates recruiter-style feedback using Llama 3.3 via Groq.

## Features

- Extracts text from PDF resumes
- Reads Job Description
- Creates semantic embeddings
- Calculates similarity score using cosine similarity
- Generates AI recruiter feedback
- Exports ranked results to CSV

## Tech Stack

- Python
- pypdf
- Sentence Transformers
- scikit-learn
- Pandas
- Groq API
- Llama 3.3 70B

## Project Structure

```
resume-screening-agent/
│
├── resumes/
├── output/
├── parser.py
├── embedder.py
├── ranker.py
├── ai_feedback.py
├── app.py
├── job_description.txt
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Output

The application:

- Reads all resumes
- Compares them with the Job Description
- Ranks candidates
- Generates AI recruiter feedback
- Saves results to:

```
output/results.csv
```

## Author

Mirwaise Khan