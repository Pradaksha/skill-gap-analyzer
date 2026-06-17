import streamlit as st
from ui import show_sidebar, show_header
from charts import show_results


st.set_page_config(
    page_title="Skill Gap Analyzer",
    layout="centered"
)

# Sidebar
show_sidebar()

# Header
show_header()

st.markdown("---")

# Resume Upload

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Job Description

job_description = st.text_area(
    "Paste Job Description",
    height=180,
    placeholder="Paste the full job description here..."
)

st.markdown("")

# Analyze Button

if st.button(
    "🔍 Analyze Resume",
    use_container_width=True
):

    if not uploaded_file or not job_description.strip():

        st.warning(
            "Please upload a resume and paste a job description."
        )

    else:

        with st.spinner("Analyzing your resume..."):

            show_results()

# Footer

st.markdown("---")

st.caption(
    "Skill Gap Analyzer • Developed by Pradaksha & Team"
)