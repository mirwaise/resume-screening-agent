from parser import extract_text
from embedder import get_embedding
from ranker import calculate_similarity
from ai_feedback import get_feedback

import pandas as pd
import os

# ==========================
# Read Job Description
# ==========================

with open("job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

# Create embedding for Job Description
jd_embedding = get_embedding(job_description)

# Get all resume files
files = os.listdir("resumes")

results = []

# ==========================
# Process Each Resume
# ==========================

for file in files:

    print(f"\n📄 Processing {file}...")

    # Extract Resume Text
    text = extract_text("resumes/" + file)

    # Create Resume Embedding
    resume_embedding = get_embedding(text)

    # Calculate Similarity Score
    score = calculate_similarity(
        jd_embedding,
        resume_embedding
    )

    # Convert score into percentage
    score = round(float(score) * 100, 2)

    # Generate AI Feedback
    feedback = get_feedback(
        job_description,
        text
    )

    # Save Result
    results.append({
        "Resume": file,
        "Score (%)": score,
        "Feedback": feedback
    })

# ==========================
# Sort Results
# ==========================

results.sort(
    key=lambda x: x["Score (%)"],
    reverse=True
)

# ==========================
# Display Results
# ==========================

print("\n")
print("=" * 80)
print("🏆 AI RESUME SCREENING RESULTS")
print("=" * 80)

for result in results:

    print(f"\n📄 Resume : {result['Resume']}")
    print(f"🎯 Match Score : {result['Score (%)']}%")

    print("\n🤖 AI Feedback")
    print("-" * 80)
    print(result["Feedback"])
    print("=" * 80)

# ==========================
# Save CSV
# ==========================

df = pd.DataFrame(results)

df.to_csv(
    "output/results.csv",
    index=False
)

print("\n✅ Results saved successfully!")
print("📁 File saved to: output/results.csv")