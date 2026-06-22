import streamlit as st
import time

from ui import show_header
from charts import show_match_score

st.set_page_config(
    page_title="Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide"
)

# ---------------- CUSTOM STYLING ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
h1, h2, h3 {
    font-family: 'Poppins', sans-serif;
}

.hero {
    background: linear-gradient(135deg, #7C3AED 0%, #A78BFA 100%);
    padding: 36px;
    border-radius: 20px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 10px 30px rgba(124, 58, 237, 0.25);
}
.hero h1 { color: white; margin-bottom: 4px; }
.hero p { color: #EDE9FE; margin: 0; }

.step-card {
    background: white;
    border-radius: 14px;
    padding: 16px;
    text-align: center;
    font-weight: 600;
    color: #4C1D95;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    border-left: 4px solid #7C3AED;
}

.step-green { background: #ECFDF5; color: #065F46; border-left: 4px solid #10B981; }
.step-blue { background: #EFF6FF; color: #1E40AF; border-left: 4px solid #3B82F6; }
.step-yellow { background: #FFFBEB; color: #92400E; border-left: 4px solid #F59E0B; }
.step-red { background: #FEF2F2; color: #991B1B; border-left: 4px solid #EF4444; }

.upload-card {
    background: #F9F8FF;
    border: 2px dashed #C4B5FD;
    border-radius: 16px;
    padding: 30px;
    text-align: center;
}

.metric-card {
    background: white;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}
.metric-card .value { font-size: 28px; font-weight: 700; color: #7C3AED; }
.metric-card .label { font-size: 13px; color: #6B7280; }

.skill-badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 20px;
    margin: 4px;
    font-weight: 500;
    font-size: 14px;
}
.skill-match { background: #D1FAE5; color: #047857; }
.skill-missing { background: #FEE2E2; color: #B91C1C; }
            
[data-testid="stFileUploaderDropzone"] {
    background: #F9F8FF !important;
    border: 2px dashed #C4B5FD !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06) !important;
}

[data-testid="stTextArea"] textarea {
    background: #F9F8FF !important;
    border: 2px solid #C4B5FD !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06) !important;
    padding: 14px !important;
}
.stButton > button {
    background: linear-gradient(135deg, #7C3AED 0%, #A78BFA 100%) !important;
    color: white !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 0 !important;
    box-shadow: 0 4px 14px rgba(124, 58, 237, 0.25) !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.35) !important;
    transform: translateY(-1px);
    color: white !important;
}
</style>
            
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🎯 About")

    st.write(
        "AI-powered Skill Gap Analyzer that compares resumes "
        "with job descriptions."
    )

    st.divider()

    st.subheader("Features")

    st.write("✅ Resume Upload")
    st.write("✅ Skill Matching")
    st.write("✅ Skill Gap Detection")
    st.write("✅ Learning Recommendations")

# ---------------- HEADER ----------------

show_header()

# ---------------- UPLOAD SECTION ----------------

st.markdown("## 📄 Upload Resume")
st.markdown(
    "<p style='color:#4B5563; font-size:14px; margin-bottom:8px;'>Drag & drop your resume here, or click Browse to upload (PDF only)</p>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "",
    type=["pdf"],
    label_visibility="collapsed"
)

# ---------------- JOB DESCRIPTION ----------------

st.markdown("## 📝 Job Description")

job_description = st.text_area(
    "",
    placeholder="Paste Job Description Here...",
    height=220,
    label_visibility="collapsed"
)

# ---------------- ANALYZE BUTTON ----------------
col1, col2 = st.columns([1, 2])

with col1:
    analyze = st.button(
        "🚀 Analyze Resume",
        use_container_width=True
)


# ---------------- RESULTS ----------------

if analyze:

    if uploaded_file is None:

        st.error("Please upload a resume.")

    elif job_description.strip() == "":

        st.error("Please paste a Job Description.")

    

    else:

        with st.spinner("🔍 Analyzing your resume..."):

            time.sleep(1.5)

            # Dummy data
            match_score = 75

            matching_skills = [
                "Python",
                "SQL",
                "Tableau"
            ]

            missing_skills = [
                "AWS",
                "Power BI"
            ]

        st.success("Analysis Completed!")

        # Score

        show_match_score(match_score)

        
        # Metrics

        col1, col2, col3 = st.columns(3)

        metrics = [
            (f"{match_score}%", "Match Score"),
            (len(matching_skills), "Matched Skills"),
            (len(missing_skills), "Missing Skills"),
        ]

        for col, (value, label) in zip([col1, col2, col3], metrics):
            col.markdown(
                f'<div class="metric-card"><div class="value">{value}</div><div class="label">{label}</div></div>',
                unsafe_allow_html=True
            )

        st.divider()

        # Matching Skills

        st.subheader("✅ Matching Skills")

        badges = "".join(
            f'<span class="skill-badge skill-match">{skill}</span>'
            for skill in matching_skills
        )
        st.markdown(badges, unsafe_allow_html=True)

        st.divider()

        # Missing Skills

        st.subheader("❌ Missing Skills")

        badges = "".join(
            f'<span class="skill-badge skill-missing">{skill}</span>'
            for skill in missing_skills
        )
        st.markdown(badges, unsafe_allow_html=True)

        st.divider()

        # Learning Resources

        st.subheader("📚 Learning Recommendations")

        for skill in missing_skills:

            with st.expander(f"Learn {skill}"):

                if skill == "AWS":

                    st.markdown("""
### AWS Learning Roadmap

**Week 1**
- AWS Cloud Practitioner
- AWS Fundamentals

**Week 2**
- EC2
- S3

**Week 3**
- IAM
- Security Basics

### Resources

- AWS Skill Builder
- AWS Training & Certification
- FreeCodeCamp AWS Course
                    """)

                elif skill == "Power BI":

                    st.markdown("""
### Power BI Learning Roadmap

**Week 1**
- Power BI Basics

**Week 2**
- Data Cleaning
- Power Query

**Week 3**
- Dashboard Building

### Resources

- Microsoft Learn
- Guy In A Cube (YouTube)
- Power BI Documentation
                    """)

        st.divider()

        st.caption(
            "Skill Gap Analyzer • Developed by Pradaksha & Team"
        )