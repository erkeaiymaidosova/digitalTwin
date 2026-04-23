import streamlit as st
import json
import pandas as pd
import plotly.express as px
import time
import random

from model import predict_jobs
from agent import get_learning_resources

st.set_page_config(page_title="Digital Twin", layout="wide")

# ---------- LOAD DATA ----------
with open("data.json", "r") as file:
    data = json.load(file)

# ---------- SIDEBAR ----------
st.sidebar.title("🚀 Navigation")

page = st.sidebar.radio(
    "Choose Page",
    ["🏠 Profile", "💼 Career Match", "🤖 AI Assistant", "📚 Resources", "🔥 Roast Mode"]
)

# =====================================================
# PROFILE
# =====================================================

if page == "🏠 Profile":

    st.title("👤 Your Digital Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Technical Skills")
        for skill in data["skills"]:
            st.progress(80)
            st.write(skill)

    with col2:
        st.subheader("Soft Skills")
        for skill in data["soft_skills"]:
            st.progress(75)
            st.write(skill)

    st.subheader("🎯 Interests")
    st.write(", ".join(data["interests"]))

    # Radar Chart
    st.subheader("📊 Skill Radar")

    radar_data = pd.DataFrame({
        "Skill": ["Python", "AI", "Research", "Communication", "Creativity"],
        "Score": [8, 6, 7, 9, 9]
    })

    fig = px.line_polar(
        radar_data,
        r="Score",
        theta="Skill",
        line_close=True
    )

    fig.update_traces(fill="toself")

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# CAREER MATCH
# =====================================================

elif page == "💼 Career Match":

    st.title("💼 Career Match Engine")

    results = predict_jobs(data["skills"])

    st.metric("Top Match", results[0][0])
    st.metric("Total Careers Analysed", "4")
    st.metric("Growth Potential", "High")

    st.subheader("Career Scores")

    for job, score in results:
        st.write(f"### {job}")
        progress = st.progress(0)

        for i in range(int(score * 100)):
            time.sleep(0.005)
            progress.progress(i + 1)

        st.write(f"Match Score: {round(score * 100,1)}%")

# =====================================================
# AI ASSISTANT
# =====================================================

elif page == "🤖 AI Assistant":

    st.title("🤖 Personal AI Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # show old messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ask about career, motivation, learning...")

    if prompt:

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.write(prompt)

        q = prompt.lower()

        if "career" in q:
            answers = [
                "AI Engineer fits you strongly.",
                "Product Manager suits your communication skills.",
                "Data Analyst is realistic with SQL practice."
            ]

        elif "learn" in q:
            answers = [
                "Focus on Python + SQL + projects.",
                "Stop passive learning. Build real things.",
                "Consistency will beat intensity."
            ]

        elif "motivation" in q:
            answers = [
                "Action creates motivation.",
                "Discipline beats feelings.",
                "Start ugly, improve later."
            ]

        else:
            answers = [
                "Interesting question.",
                "That depends on your long-term goals.",
                "You should keep building practical experience."
            ]

        reply = random.choice(answers)

        with st.chat_message("assistant"):
            st.write(reply)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

# =====================================================
# RESOURCES
# =====================================================

elif page == "📚 Resources":

    st.title("📚 Learning Resources")

    results = predict_jobs(data["skills"])
    top_job = results[0][0]

    st.subheader(f"For {top_job}")

    resources = get_learning_resources(top_job)

    for item in resources:
        st.success(item)

# =====================================================
# ROAST
# =====================================================

elif page == "🔥 Roast Mode":

    st.title("🔥 Roast My Stack")

    st.error(
        "Too many plans. Too few finished projects. "
        "Your future employer cannot hire potential forever."
    )