
import streamlit as st
from pypdf import PdfReader

from utils.llm_helper import generate_response


def resume_analyzer():

    st.header("🔍 AI Resume Analyzer")

    st.write(
        "Upload your resume and receive AI-powered feedback."
    )

    # Upload PDF
    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        # Extract text from PDF
        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page in reader.pages:
            resume_text += page.extract_text() or ""

        st.success("Resume uploaded successfully!")

        if not resume_text.strip():

            st.warning(
                "No readable text found. Please upload a text-based PDF."
            )

        else:

            with st.expander("View Extracted Resume Text"):
                st.write(resume_text)

            # Analyze Resume
            if st.button("Analyze My Resume"):

                prompt = f"""
                Act as a professional resume reviewer.

                Analyze the following resume.

                RESUME:
                {resume_text}

                Provide the following:

                1. Overall Resume Score out of 100.
                2. Resume Strengths.
                3. Weaknesses and missing information.
                4. Technical Skills Analysis.
                5. Suggestions for improvement.
                6. Three specific recommendations to improve this resume.

                Be honest and do not invent information.
                Use simple professional English.
                """

                with st.spinner("AI is analyzing your resume..."):

                    result = generate_response(prompt)

                st.subheader("Resume Analysis")

                st.write(result)
