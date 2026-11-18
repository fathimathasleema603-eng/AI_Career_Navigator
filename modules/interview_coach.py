
import streamlit as st

from utils.llm_helper import generate_response


def interview_coach():

    st.header("🎤 AI Interview Coach")

    st.write(
        "Practice interview questions and receive "
        "personalized AI feedback."
    )

    # Interview settings
    st.subheader("1. Interview Settings")

    target_role = st.text_input(
        "Target Job Role",
        placeholder="Example: Generative AI Engineer"
    )

    difficulty = st.selectbox(
        "Interview Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    question_type = st.selectbox(
        "Question Category",
        [
            "Technical",
            "HR",
            "Scenario-Based",
            "Mixed"
        ]
    )

    # Generate questions
    if st.button("Generate Interview Questions"):

        if not target_role.strip():

            st.warning("Please enter your target job role.")

        else:

            prompt = f"""
            Act as a professional technical interviewer.

            Target Job Role: {target_role}
            Difficulty: {difficulty}
            Question Category: {question_type}

            Generate 5 realistic interview questions.

            Requirements:
            1. Questions must match the selected job role.
            2. Match the selected difficulty.
            3. Use clear and simple English.
            4. Include a mixture of conceptual and practical
               questions when appropriate.
            5. Number each question.
            6. Do not provide answers yet.
            """

            with st.spinner("Preparing your interview questions..."):

                questions = generate_response(prompt)

            st.session_state["interview_questions"] = questions
            st.session_state["interview_role"] = target_role

    # Display generated questions
    if "interview_questions" in st.session_state:

        st.subheader("2. Your Interview Questions")

        st.write(st.session_state["interview_questions"])

        st.divider()

        # Candidate answer
        st.subheader("3. Practice Your Answer")

        candidate_answer = st.text_area(
            "Write your answer to one of the questions",
            placeholder="Type your interview answer here..."
        )

        if st.button("Evaluate My Answer"):

            if not candidate_answer.strip():

                st.warning("Please enter your answer.")

            else:

                evaluation_prompt = f"""
                Act as an experienced interview coach.

                Job Role: {st.session_state["interview_role"]}

                Interview Questions:
                {st.session_state["interview_questions"]}

                Candidate Answer:
                {candidate_answer}

                Evaluate the candidate's answer.

                Provide:
                1. What was good about the answer?
                2. What needs improvement?
                3. Technical accuracy.
                4. Communication quality.
                5. A suggested improved answer.

                Be supportive and constructive.
                Do not invent candidate experience.
                """

                with st.spinner("Evaluating your answer..."):

                    feedback = generate_response(evaluation_prompt)

                st.subheader("4. Interview Feedback")

                st.write(feedback)
