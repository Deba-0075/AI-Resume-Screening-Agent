import os
import tempfile
import pandas as pd
import streamlit as st

from ranking.candidate_ranker import CandidateRanker

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Screening Agent")
st.caption("Analyze and rank multiple resumes against a Job Description")

# ---------------------------------------
# Sidebar
# ---------------------------------------

with st.sidebar:

    st.header("📂 Upload Files")

    jd_file = st.file_uploader(
        "Upload Job Description (.txt)",
        type=["txt"]
    )

    resume_files = st.file_uploader(
        "Upload Candidate Resumes",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )

    analyze = st.button(
        "🚀 Analyze Resumes",
        use_container_width=True
    )

# ---------------------------------------
# Analysis
# ---------------------------------------

if analyze:

    if jd_file is None:
        st.error("Please upload a Job Description.")
        st.stop()

    if not resume_files:
        st.error("Please upload at least one resume.")
        st.stop()

    jd_text = jd_file.read().decode("utf-8")

    temp_dir = tempfile.mkdtemp()

    for file in resume_files:

        with open(
            os.path.join(temp_dir, file.name),
            "wb"
        ) as f:

            f.write(file.getbuffer())


    with st.spinner("Analyzing resumes..."):

        ranker = CandidateRanker()

        results = ranker.rank_all(
            temp_dir,
            jd_text
        )

    df = pd.DataFrame(results)


    st.divider()

    st.subheader("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📄 Total Resumes",
        len(df)
    )

    col2.metric(
        "🏆 Highest Score",
        f"{df['final_score'].max():.2f}"
    )

    col3.metric(
        "📈 Average Score",
        f"{df['final_score'].mean():.2f}"
    )


    st.divider()

    st.subheader("🏆 Best Candidate")

    top = df.iloc[0]

    st.success(
        f"""
Candidate : {top['candidate']}

Resume : {top['resume_file']}

Final Score : {top['final_score']}

Recommendation : {top['recommendation']}
"""
    )


    st.divider()

    st.subheader("📈 Candidate Scores")

    chart = df[
        ["candidate", "final_score"]
    ].set_index("candidate")

    st.bar_chart(chart)


    st.divider()

    st.subheader("📋 Ranked Candidates")

    st.dataframe(
        df,
        use_container_width=True
    )


    st.divider()

    st.subheader("📑 Candidate Details")

    for _, row in df.iterrows():

        with st.expander(
            f"🏅 Rank {row['rank']} - {row['candidate']}"
        ):

            st.write("**Resume:**", row["resume_file"])
            st.write("**Email:**", row["email"])
            st.write("**Phone:**", row["phone"])

            st.write("### Scores")

            st.write("Semantic :", row["semantic_score"])
            st.write("Skill :", row["skill_score"])
            st.write("Education :", row["education_score"])
            st.write("Experience :", row["experience_score"])
            st.write("Final :", row["final_score"])

            st.write("### Recommendation")

            st.success(row["recommendation"])

            st.write("### Matched Skills")

            st.write(row["matched_skills"])

            st.write("### Missing Skills")

            st.write(row["missing_skills"])


    st.divider()

    st.subheader("⬇ Download Reports")

    col1, col2 = st.columns(2)

    csv = df.to_csv(index=False)

    with col1:

        st.download_button(
            "⬇ Download CSV",
            csv,
            file_name="ranked_candidates.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:

        st.download_button(
            "⬇ Download JSON",
            df.to_json(
                orient="records",
                indent=4
            ),
            file_name="ranked_candidates.json",
            mime="application/json",
            use_container_width=True
        )