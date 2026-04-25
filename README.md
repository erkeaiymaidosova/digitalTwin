# Final Generative AI Project  
# The Digital Twin Career Engine

## Project Overview

The **Digital Twin Career Engine** is an AI-powered personal career assistant designed to analyze a user's digital footprint, identify strengths, predict the most suitable future career paths, and provide a personalized development roadmap.

This project combines multiple modern AI concepts:

- Generative AI
- Machine Learning
- Recommendation Systems
- Personal Analytics
- Career Path Prediction
- Interactive Web Applications

The final result is a smart assistant that transforms scattered personal data into actionable career insights.

---

# Main Objective

The purpose of this project is to create a **Digital Twin** of the user — a virtual professional version of the person based on skills, interests, soft skills, and learning behavior.

The system answers questions such as:

- What career suits me best?
- What are my strongest skills?
- Which skills are missing?
- How can I improve professionally?
- What should I learn next?

---

# Core Idea

Every person leaves a digital footprint:

- CV / Resume
- Academic Transcript
- Chat History
- Learning Interests
- Search Topics
- Productivity Habits

By analyzing these sources, AI can detect patterns and generate realistic career recommendations.

---

# 5-Layer Generative AI Architecture

---

## Platform Layer

### Purpose:
Collect and organize user data.

### Implementation:

The following structured files were used:

- `data.json`
- Resume data
- Skills list
- Soft skills
- Interests

### Why this matters:

Without structured input data, AI systems cannot generate valuable output.

This follows the principle:

> Garbage In = Garbage Out

---

## Model Layer

### Purpose:
Predict the most suitable career paths.

### Technology Used:

- Python
- Scikit-learn
- Cosine Similarity Algorithm

### How it Works:

The user's skill set is converted into text vectors and compared with predefined job profiles:

Examples:

- AI Engineer
- Data Analyst
- Product Manager
- UI/UX Designer

### Output Example:

| Career | Match Score |
|--------|------------|
| AI Engineer | 84% |
| Product Manager | 79% |
| Data Analyst | 73% |

### Why Cosine Similarity?

Cosine Similarity is efficient for comparing text-based skill profiles and measuring similarity between vectors.

---

## Agent Layer

### Purpose:
Turn recommendations into action.

### Implementation:

After predicting the best career match, the system generates personalized learning resources.

Example:

If best match = AI Engineer

Resources:

- Learn Python Advanced
- Study Machine Learning
- Build Portfolio Projects
- Practice SQL

### Logic:

Instead of giving static advice, the assistant adapts recommendations based on prediction results.

---

## Application Layer

### Purpose:
Provide a user-friendly interface.

### Technology Used:

- Streamlit
- Plotly

### Features:

## Profile Page

Displays:

- Technical skills
- Soft skills
- Interests
- Radar Chart

## Career Match Page

Displays:

- Top career matches
- Match percentages
- Animated progress bars
- Metrics dashboard

## AI Assistant

Interactive chatbot that answers questions about:

- Career
- Learning path
- Motivation
- Growth strategy

## Resources Page

Shows custom learning roadmap.

## Roast Mode

A humorous mode that critiques procrastination and lack of execution.

---

## Infrastructure Layer

### Purpose:
Explain where computation happens.

### Local Machine:

Runs locally on user's computer:

- Streamlit server
- Python scripts
- Machine Learning logic

### Cloud Services:

Can optionally integrate:

- OpenAI API
- NotebookLM
- GitHub

### Benefit:

Hybrid architecture reduces cost while keeping performance fast.

---

# Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Core programming |
| Streamlit | Web UI |
| Plotly | Charts |
| Scikit-learn | Machine Learning |
| JSON | User data storage |
| GitHub | Version control |

---

# Project Structure

```text
Digital Twin/

app.py
model.py
agent.py
data.json
requirements.txt
README.md
