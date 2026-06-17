import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.header("About")

        st.write(
            "AI-powered Skill Gap Analyzer that compares a resume "
            "with a job description and identifies missing skills."
        )

        st.markdown("---")

        st.subheader("Analyzes")

        st.write("• Technical Skills")
        st.write("• Frameworks & Tools")
        st.write("• Soft Skills")


def show_header():
    st.title("🎯 Skill Gap Analyzer")

    st.markdown(
        "Upload your resume and paste a job description "
        "to identify skill gaps."
    )