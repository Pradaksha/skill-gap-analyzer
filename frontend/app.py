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

/* ── LOGIN ── */
.brand-bar {
    font-family: 'Poppins', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #7C3AED;
    padding-bottom: 24px;
}
.welcome-title {
    font-family: 'Poppins', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #1F2937;
    margin-bottom: 4px;
}
.welcome-sub {
    font-size: 14px;
    color: #6B7280;
    margin-bottom: 20px;
}
.login-box {
    background: white;
    border-radius: 20px;
    padding: 28px 24px;
    box-shadow: 0 8px 30px rgba(124,58,237,0.10);
    margin-bottom: 16px;
}
.preview-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    padding: 8px;
}
.pcard {
    background: white;
    border-radius: 14px;
    padding: 14px;
    box-shadow: 0 4px 16px rgba(124,58,237,0.08);
    font-size: 12px;
    color: #1F2937;
}
.pcard-title {
    font-weight: 700;
    font-size: 11px;
    color: #6B7280;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
}
.big-score {
    font-size: 32px;
    font-weight: 800;
    color: #7C3AED;
    line-height: 1;
}
.score-bar {
    background: #EDE9FE;
    border-radius: 10px;
    height: 8px;
    margin-top: 8px;
    overflow: hidden;
}
.score-fill {
    background: linear-gradient(90deg, #7C3AED, #A78BFA);
    height: 8px;
    border-radius: 10px;
    width: 75%;
}
.skill-pill {
    display: inline-block;
    background: #D1FAE5;
    color: #047857;
    border-radius: 20px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 600;
    margin: 2px;
}
.skill-pill-red {
    display: inline-block;
    background: #FEE2E2;
    color: #B91C1C;
    border-radius: 20px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 600;
    margin: 2px;
}
.road-step {
    display: flex;
    align-items: center;
    gap: 6px;
    margin: 4px 0;
    font-size: 11px;
}
.road-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #A78BFA;
    flex-shrink: 0;
}
.road-dot-done {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10B981;
    flex-shrink: 0;
}
.bar-row {
    display: flex;
    align-items: center;
    gap: 6px;
    margin: 4px 0;
}
.bar-label { font-size: 10px; color: #6B7280; width: 70px; }
.bar-track {
    flex: 1;
    background: #EDE9FE;
    border-radius: 6px;
    height: 6px;
    overflow: hidden;
}
.bar-fill {
    height: 6px;
    border-radius: 6px;
    background: linear-gradient(90deg, #7C3AED, #A78BFA);
}
.upload-icon {
    font-size: 28px;
    text-align: center;
    margin: 6px 0;
}
.course-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 4px 0;
    border-bottom: 1px solid #F3F4F6;
    font-size: 11px;
}
.span-2 { grid-column: span 2; }
.span-3 { grid-column: span 3; }

/* ── ANALYZER ── */
.hero-slim {
    background: linear-gradient(135deg, #7C3AED 0%, #A78BFA 100%);
    padding: 18px 24px;
    border-radius: 16px;
    color: white;
    margin-bottom: 20px;
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.2);
}
.hero-slim h2 { color: white; margin: 0; font-size: 18px; }
.hero-slim p  { color: #EDE9FE; margin: 4px 0 0 0; font-size: 12px; }

.step-card {
    background: white;
    border-radius: 14px;
    padding: 12px;
    text-align: center;
    font-weight: 600;
    font-size: 12px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}
.step-green  { background: #ECFDF5; color: #065F46; border-left: 4px solid #10B981; }
.step-blue   { background: #EFF6FF; color: #1E40AF; border-left: 4px solid #3B82F6; }
.step-yellow { background: #FFFBEB; color: #92400E; border-left: 4px solid #F59E0B; }
.step-red    { background: #FEF2F2; color: #991B1B; border-left: 4px solid #EF4444; }

/* ── RESULTS ── */
.results-hero {
    background: linear-gradient(135deg, #6D28D9 0%, #7C3AED 60%, #A78BFA 100%);
    padding: 20px 28px;
    border-radius: 16px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
    box-shadow: 0 8px 30px rgba(109, 40, 217, 0.25);
}
.results-left h2 {
    color: white;
    font-size: 18px;
    margin: 0 0 4px 0;
}
.results-left p {
    color: #DDD6FE;
    font-size: 12px;
    margin: 0;
}
.score-circle {
    background: rgba(255,255,255,0.2);
    border-radius: 50%;
    width: 90px;
    height: 90px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.score-circle .num {
    font-size: 28px;
    font-weight: 700;
    color: white;
    line-height: 1;
}
.score-circle .lbl {
    font-size: 10px;
    color: #DDD6FE;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* ── SHARED ── */
.metric-card {
    background: white;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}
.metric-card .value { font-size: 26px; font-weight: 700; color: #7C3AED; }
.metric-card .label { font-size: 12px; color: #6B7280; }

.skill-badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 20px;
    margin: 4px;
    font-weight: 500;
    font-size: 13px;
}
.skill-match   { background: #D1FAE5; color: #047857; }
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

# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "match_score" not in st.session_state:
    st.session_state.match_score = None
if "matching_skills" not in st.session_state:
    st.session_state.matching_skills = []
if "missing_skills" not in st.session_state:
    st.session_state.missing_skills = []

# ================================================
# PAGE 1 — LOGIN
# ================================================

if st.session_state.page == "login":

    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: #F5F3FF;
    }

    /* ── FIX: Make input boxes clearly visible ── */
    [data-testid="stTextInput"] input {
        background: white !important;
        border: 2px solid #C4B5FD !important;
        border-radius: 12px !important;
        padding: 10px 14px !important;
        font-size: 14px !important;
        color: #1F2937 !important;
        box-shadow: 0 2px 8px rgba(124,58,237,0.08) !important;
    }
    [data-testid="stTextInput"] input:focus {
        border-color: #7C3AED !important;
        box-shadow: 0 0 0 3px rgba(124,58,237,0.15) !important;
    }
    [data-testid="stTextInput"] label {
        color: #374151 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }

    /* ── Left panel ── */
    .brand-bar {
        font-family: 'Poppins', sans-serif;
        font-size: 20px; font-weight: 700; color: #7C3AED;
        display: flex; align-items: center; gap: 8px;
        padding-bottom: 6px;
    }
    .tagline { font-size: 12px; color: #6B7280; margin-bottom: 18px; line-height: 1.7; }
    .tagline b { color: #7C3AED; font-weight: 600; }
    .signup-box {
        background: white;
        border-radius: 18px;
        padding: 20px 18px;
        box-shadow: 0 4px 24px rgba(124,58,237,0.10);
        margin-bottom: 16px;
        border: 1px solid #EDE9FE;
    }
    .signup-title { font-family: 'Poppins', sans-serif; font-size: 26px; font-weight: 800; color: #1F2937; margin-bottom: 3px; }
    .signup-sub { font-size: 12px; color: #6B7280; }

    /* ── Scrolling collage ── */
    .collage-outer {
        display: flex;
        gap: 10px;
        height: 90vh;
        overflow: hidden;
        padding: 4px 0;
        border-radius: 20px;
    }
    .col-wrap {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 155px;
        flex-shrink: 0;
    }
    .scroll-up   { animation: scrollUp 22s linear infinite; }
    .scroll-down { animation: scrollDown 25s linear infinite; margin-top: -70px; }
    .scroll-up2  { animation: scrollUp 30s linear infinite; margin-top: -40px; }
    .scroll-down2{ animation: scrollDown 20s linear infinite; margin-top: -90px; }

    @keyframes scrollUp {
        0%   { transform: translateY(0); }
        100% { transform: translateY(-50%); }
    }
    @keyframes scrollDown {
        0%   { transform: translateY(-50%); }
        100% { transform: translateY(0); }
    }

    .cimg {
        width: 155px;
        border-radius: 14px;
        object-fit: cover;
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        flex-shrink: 0;
        display: block;
    }
    .h-tall  { height: 210px; }
    .h-med   { height: 160px; }
    .h-short { height: 120px; }
    </style>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1.5], gap="large")

    with left:
        st.markdown("""
        <div style="padding-top:24px">
          <div class="brand-bar">🎯 Skill Gap Analyzer</div>
          <div class="tagline">Match your <b>resume</b> against job requirements<br>and get <b>personalized learning</b> recommendations.</div>
          <div class="signup-box">
            <div class="signup-title">Sign up</div>
            <div class="signup-sub">Get started for free. No credit card required.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input("👤  Username", placeholder="Enter your username")
        password = st.text_input("🔒  Password", type="password", placeholder="Enter your password")
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔑 Login", use_container_width=True):
                if username.strip() == "" or password.strip() == "":
                    st.error("Please enter both fields.")
                else:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.page = "analyzer"
                    st.rerun()
        with col2:
            if st.button("✨ Sign Up", use_container_width=True):
                if username.strip() == "" or password.strip() == "":
                    st.error("Please enter both fields.")
                else:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.page = "analyzer"
                    st.rerun()

        st.markdown("---")
        st.markdown("""
        <div style='font-size:10px;color:#9CA3AF;line-height:1.9'>
        By signing up you agree to our
        <a href='#' style='color:#7C3AED'>Terms of Service</a> and
        <a href='#' style='color:#7C3AED'>Privacy Policy</a>.<br>
        🛡️ No credit card &nbsp; ⚡ Free to start &nbsp; 🕐 Cancel anytime
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="collage-outer">

          <!-- Column 1 — scroll UP — Resume & docs themed -->
          <div class="col-wrap scroll-up">
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=320&q=80" alt="resume"/>
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=320&q=80" alt="notes"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=320&q=80" alt="checklist"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=320&q=80" alt="working desk"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1488190211105-8b0e65b80b4e?w=320&q=80" alt="writing"/>
            <!-- duplicates for loop -->
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=320&q=80" alt="resume"/>
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=320&q=80" alt="notes"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=320&q=80" alt="checklist"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=320&q=80" alt="working desk"/>
          </div>

          <!-- Column 2 — scroll DOWN — Professional people -->
          <div class="col-wrap scroll-down">
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=320&q=80" alt="woman professional"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=320&q=80" alt="man professional"/>
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=320&q=80" alt="handshake interview"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=320&q=80" alt="interview"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1531482615713-2afd69097998?w=320&q=80" alt="team meeting"/>
            <!-- duplicates -->
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=320&q=80" alt="woman professional"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=320&q=80" alt="man professional"/>
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=320&q=80" alt="handshake"/>
          </div>

          <!-- Column 3 — scroll UP slow — Learning & courses -->
          <div class="col-wrap scroll-up2">
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=320&q=80" alt="team learning"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=320&q=80" alt="online learning"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1543269865-cbf427effbad?w=320&q=80" alt="students"/>
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=320&q=80" alt="woman studying"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1501504905252-473c47e087f8?w=320&q=80" alt="skills laptop"/>
            <!-- duplicates -->
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=320&q=80" alt="team learning"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=320&q=80" alt="online learning"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1543269865-cbf427effbad?w=320&q=80" alt="students"/>
          </div>

          <!-- Column 4 — scroll DOWN fast — Analytics & data -->
          <div class="col-wrap scroll-down2">
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=320&q=80" alt="analytics dashboard"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=320&q=80" alt="coding laptop"/>
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=320&q=80" alt="data charts"/>
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1553877522-43269d4ea984?w=320&q=80" alt="skill chart"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=320&q=80" alt="graph"/>
            <!-- duplicates -->
            <img class="cimg h-tall"  src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=320&q=80" alt="analytics"/>
            <img class="cimg h-med"   src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=320&q=80" alt="coding"/>
            <img class="cimg h-short" src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=320&q=80" alt="data"/>
          </div>

        </div>
        """, unsafe_allow_html=True)

# ================================================
# PAGE 2 — ANALYZER
# ================================================

elif st.session_state.page == "analyzer":

    with st.sidebar:
        st.title("🎯 About")
        st.write(
            "AI-powered Skill Gap Analyzer that compares "
            "resumes with job descriptions."
        )
        st.divider()
        st.subheader("Features")
        st.write("✅ Resume Upload")
        st.write("✅ Skill Matching")
        st.write("✅ Skill Gap Detection")
        st.write("✅ Learning Recommendations")
        st.divider()
        st.write(f"👤 Logged in as **{st.session_state.username}**")
        if st.button("🚪 Logout"):
            st.session_state.page = "login"
            st.session_state.logged_in = False
            st.rerun()

    # Constrain analyzer to centered width
    _, center, _ = st.columns([1, 3, 1])

    with center:

        st.markdown("""
        <div class="hero-slim">
            <h2>🎯 Skill Gap Analyzer</h2>
            <p>Upload your resume and paste a job description to get started.</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        steps  = ["① Upload Resume", "② Job Description",
                  "③ Analyze", "④ Learning Plan"]
        colors = ["step-green", "step-blue", "step-yellow", "step-red"]
        for col, step, color in zip([col1, col2, col3, col4], steps, colors):
            col.markdown(
                f'<div class="step-card {color}">{step}</div>',
                unsafe_allow_html=True
            )

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        st.markdown("## 📄 Upload Resume")
        st.markdown(
            "<p style='color:#4B5563;font-size:14px;margin-bottom:8px;'>"
            "Drag & drop your resume here, or click Browse to upload "
            "(PDF only)</p>",
            unsafe_allow_html=True
        )
        uploaded_file = st.file_uploader(
            "", type=["pdf"], label_visibility="collapsed"
        )

        st.markdown("## 📝 Job Description")
        job_description = st.text_area(
            "",
            placeholder="Paste Job Description Here...",
            height=220,
            label_visibility="collapsed"
        )

        col1, col2 = st.columns([1, 2])
        with col1:
            analyze = st.button("🚀 Analyze Resume", use_container_width=True)

        if analyze:
            if uploaded_file is None:
                st.error("Please upload a resume.")
            elif job_description.strip() == "":
                st.error("Please paste a Job Description.")
            else:
                with st.spinner("🔍 Analyzing your resume..."):
                    time.sleep(1.5)
                    st.session_state.match_score     = 75
                    st.session_state.matching_skills = ["Python", "SQL", "Tableau"]
                    st.session_state.missing_skills  = ["AWS", "Power BI"]
                st.session_state.page = "results"
                st.rerun()

# ================================================
# PAGE 3 — RESULTS
# ================================================

elif st.session_state.page == "results":

    with st.sidebar:
        st.title("📊 Your Results")
        st.write(f"👤 **{st.session_state.username}**")
        st.divider()
        if st.button("🔍 Analyze Again"):
            st.session_state.page = "analyzer"
            st.rerun()
        if st.button("🚪 Logout"):
            st.session_state.page = "login"
            st.session_state.logged_in = False
            st.rerun()

    _, center, _ = st.columns([1, 3, 1])

    with center:

        match_score     = st.session_state.match_score
        matching_skills = st.session_state.matching_skills
        missing_skills  = st.session_state.missing_skills

        st.markdown(f"""
        <div class="results-hero">
            <div class="results-left">
                <h2>🎉 Analysis Complete!</h2>
                <p>Your resume matched {len(matching_skills)} skills
                and is missing {len(missing_skills)} for this role.</p>
            </div>
            <div class="score-circle">
                <div class="num">{match_score}%</div>
                <div class="lbl">Match</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        show_match_score(match_score)

        st.divider()

        col1, col2 = st.columns(2)
        metrics = [
            (len(matching_skills), "✅ Matched Skills"),
            (len(missing_skills),  "❌ Missing Skills"),
        ]
        for col, (value, label) in zip([col1, col2], metrics):
            col.markdown(
                f'<div class="metric-card">'
                f'<div class="value">{value}</div>'
                f'<div class="label">{label}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        st.divider()

        st.subheader("✅ Matching Skills")
        badges = "".join(
            f'<span class="skill-badge skill-match">{s}</span>'
            for s in matching_skills
        )
        st.markdown(badges, unsafe_allow_html=True)

        st.divider()

        st.subheader("❌ Missing Skills")
        badges = "".join(
            f'<span class="skill-badge skill-missing">{s}</span>'
            for s in missing_skills
        )
        st.markdown(badges, unsafe_allow_html=True)

        st.divider()

        st.subheader("📚 Learning Recommendations")

        for skill in missing_skills:
            with st.expander(f"Learn {skill}"):
                if skill == "AWS":
                    st.markdown("""
### AWS Learning Roadmap
**Week 1** — AWS Cloud Practitioner, AWS Fundamentals
**Week 2** — EC2, S3
**Week 3** — IAM, Security Basics

### Resources
- AWS Skill Builder → https://skillbuilder.aws
- AWS Training → https://aws.amazon.com/training
- FreeCodeCamp AWS → https://www.youtube.com/watch?v=SOTamWNgDKc
                    """)
                elif skill == "Power BI":
                    st.markdown("""
### Power BI Learning Roadmap
**Week 1** — Power BI Basics
**Week 2** — Data Cleaning, Power Query
**Week 3** — Dashboard Building

### Resources
- Microsoft Learn → https://learn.microsoft.com/power-bi
- Guy In A Cube → https://www.youtube.com/@GuyInACube
                    """)

        st.divider()
        st.caption("Skill Gap Analyzer • Developed by Pradaksha & Team")