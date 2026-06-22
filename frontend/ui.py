import streamlit as st

def show_header():

    st.markdown("""
    <div class="hero">
    <h1>🎯 Skill Gap Analyzer</h1>
    <p>Match your resume against job requirements and get personalized learning recommendations.</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    steps = ["① Upload Resume", "② Job Description", "③ Analyze", "④ Learning Plan"]
    colors = ["step-green", "step-blue", "step-yellow", "step-red"]

    for col, step, color in zip([col1, col2, col3, col4], steps, colors):
        col.markdown(f'<div class="step-card {color}">{step}</div>', unsafe_allow_html=True)

    st.divider()