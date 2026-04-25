import streamlit as st
import json
import pandas as pd
import plotly.express as px
import time
import random

from model import predict_jobs
from agent import get_learning_resources

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Digital Twin Career Engine",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
with open("data.json", "r") as file:
    data = json.load(file)

# ---------------------------------------------------
# PURPLE UI STYLE (same features, only new look)
# ---------------------------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #d8c4db;
}

section[data-testid="stSidebar"] {
    background-color: #eee4ef;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1300px;
}

h1, h2, h3, h4 {
    color: #4a2c52;
}

div[data-testid="stMetric"] {
    background-color: #f6eff7;
    border-radius: 18px;
    padding: 15px;
    border: 1px solid #dbc8df;
}

.stButton > button {
    background-color: #8f6aa8;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #6f4e86;
}

.stTextInput input {
    border-radius: 12px;
}

div[data-testid="stChatMessage"] {
    background-color: #f7f0f8;
    border-radius: 14px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("🚀 Navigation")

page = st.sidebar.radio(
    "Choose Page",
    ["🏠 Profile", "💼 Career Match", "🤖 AI Assistant", "📚 Resources", "🔥 Roast Mode"]
)

# =====================================================
# PROFILE (same features)
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
    fig.update_layout(
        paper_bgcolor="#f7f0f8",
        plot_bgcolor="#f7f0f8",
        font_color="#4a2c52"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# CAREER MATCH (same features)
# =====================================================
elif page == "💼 Career Match":

    st.title("💼 Career Match Engine")

    results = predict_jobs(data["skills"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Top Match", results[0][0])

    with col2:
        st.metric("Total Careers Analysed", "4")

    with col3:
        st.metric("Growth Potential", "High")

    st.subheader("Career Scores")

    for job, score in results:
        st.write(f"### {job}")

        progress = st.progress(0)

        for i in range(int(score * 100)):
            time.sleep(0.003)
            progress.progress(i + 1)

        st.write(f"Match Score: {round(score*100,1)}%")

# =====================================================
# AI ASSISTANT (same features)
# =====================================================
elif page == "🤖 AI Assistant":

    st.title("🤖 Personal AI Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # old messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ask about career, learning, motivation...")

    if prompt:

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        q = prompt.lower()

        if "career" in q:
            answers = [
                "AI Engineer fits you strongly.",
                "Product Manager matches your leadership and communication.",
                "Data Analyst is realistic if you improve SQL."
            ]

        elif "learn" in q:
            answers = [
                "Focus on Python + SQL + projects.",
                "Build portfolio first, consume less tutorials.",
                "Consistency will outperform motivation."
            ]

        elif "motivation" in q:
            answers = [
                "Discipline beats feelings.",
                "Action creates motivation.",
                "Small progress daily wins."
            ]

        else:
            answers = [
                "Interesting question.",
                "That depends on your goals.",
                "You should keep building real experience."
            ]

        reply = random.choice(answers)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        st.rerun()

# =====================================================
# RESOURCES (same features)
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
# ROAST MODE (same feature)
# =====================================================
elif page == "🔥 Roast Mode":

    st.title("🔥 Roast My Stack")

    st.error(
        "Too many saved tutorials. Too few finished projects. "
        "Potential means nothing without execution."
    )