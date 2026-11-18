
import streamlit as st

from utils.llm_helper import generate_response


def skill_gap_analyzer():

    st.header("🎯 AI Skill Gap Analyzer")

    st.write(
        "Discover which skills you need to learn "
        "to achieve your target career."
    )

    # User inputs
    st.subheader("1. Your Current Skills")

    current_skills = st.text_area(
        "Enter your existing skills",
        placeholder="Example: Python, NumPy, Pandas, Machine Learning"
    )

    st.subheader("2. Your Career Goal")

    target_role = st.text_input(
        "Which job role are you targeting?",
        placeholder="Example: Generative AI Engineer"
    )

    experience = st.selectbox(
        "Your experience level",
        [
            "Fresher",
            "Beginner",
            "Intermediate",
            "Experienced"
        ]
    )

    # Analyze button
    if st.button("Analyze Skill Gap"):

        if not current_skills.strip() or not target_role.strip():

            st.warning(
                "Please enter your current skills and target job role."
            )

        else:

            prompt = f"""
            Act as an experienced AI career mentor.

            Analyze the skill gap for this candidate.

            Current Skills: {current_skills}
            Target Job Role: {target_role}
            Experience Level: {experience}

            Provide the following sections:

            1. Existing Skills:
            Identify skills the candidate already has.

            2. Missing Skills:
            List important skills required for the target role.

            3. Priority Levels:
            Classify missing skills as:
            - High Priority
            - Medium Priority
            - Low Priority

            4. Learning Roadmap:
            Create a beginner-friendly, step-by-step learning roadmap.

            5. Project Recommendations:
            Suggest three practical projects for this career.

            6. Final Career Advice:
            Give useful advice to help the candidate become job-ready.

            Be realistic and use simple English.
            Do not assume skills the candidate has not mentioned.
            """

            with st.spinner("AI is analyzing your skill gaps..."):

                result = generate_response(prompt)

            st.subheader("Your Skill Gap Analysis")

            st.write(result)
