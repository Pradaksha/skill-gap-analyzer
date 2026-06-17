import streamlit as st


def show_results():

    # Dummy data (will later come from backend)

    match_score = 75

    matching = [
        "Python",
        "SQL",
        "Tableau",
        "Pandas",
        "Machine Learning",
        "Git"
    ]

    missing = [
        "AWS",
        "Power BI"
    ]

    st.subheader("📊 Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Match Score", f"{match_score}%")

    with col2:
        st.metric("Matching Skills", len(matching))

    with col3:
        st.metric("Missing Skills", len(missing))

    st.progress(match_score / 100)

    st.caption(
        f"Resume matches {match_score}% of the job requirements."
    )

    st.markdown("---")

    st.subheader("✅ Matching Skills")

    for skill in matching:
        st.markdown(f"• {skill}")

    st.markdown("---")

    st.subheader("❌ Missing Skills")

    for skill in missing:
        st.markdown(f"• {skill}")

    st.markdown("---")

    st.subheader("💡 Recommended Learning Resources")

    with st.expander("☁️ AWS Learning Resources"):

        st.markdown("""
**AWS Skill Builder**

https://skillbuilder.aws

**AWS Documentation**

https://docs.aws.amazon.com

**AWS Cloud Practitioner Course (FreeCodeCamp)**

https://www.youtube.com/watch?v=SOTamWNgDKc
""")

    with st.expander("📊 Power BI Learning Resources"):

        st.markdown("""
**Microsoft Learn Power BI**

https://learn.microsoft.com/power-bi

**Power BI Documentation**

https://learn.microsoft.com/power-bi

**Power BI Full Course (FreeCodeCamp)**

https://www.youtube.com/watch?v=NNSHu0rkew8
""")