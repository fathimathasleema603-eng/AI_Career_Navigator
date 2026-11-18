
import streamlit as st

from utils.llm_helper import generate_response
from utils.rag_helper import ask_learning_mentor


def learning_mentor():

    st.header("📚 AI Learning Mentor")

    st.write(
        "Your personal AI tutor. Learn new skills with "
        "personalized roadmaps and simple explanations."
    )

    # --------------------------------
    # 1. Learning Roadmap
    # --------------------------------

    st.subheader("1. Create Your Learning Roadmap")

    topic = st.text_input(
        "What do you want to learn?",
        placeholder="Example: Generative AI"
    )

    level = st.selectbox(
        "Your current knowledge level",
        [
            "Complete Beginner",
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    days = st.number_input(
        "How many days can you spend learning?",
        min_value=1,
        max_value=365,
        value=30
    )

    if st.button("Generate Learning Roadmap"):

        if not topic.strip():

            st.warning("Please enter a learning topic.")

        else:

            prompt = f"""
            Act as an expert Generative AI career mentor
            and technical instructor.

            Create a structured learning roadmap.

            Topic: {topic}
            Knowledge Level: {level}
            Available Time: {days} days

            IMPORTANT INSTRUCTIONS:

            1. Start with prerequisites before advanced topics.
            2. Follow a logical learning sequence.
            3. Divide topics into daily learning tasks.
            4. Explain why each topic is important.
            5. Include practical Python coding exercises.
            6. Include mini projects.
            7. Include revision and interview preparation.
            8. Separate topics into:
               - MUST LEARN
               - GOOD TO KNOW
               - OPTIONAL

            For Generative AI, follow this sequence:

            Python fundamentals
            NumPy and Pandas
            Machine Learning foundations
            Deep Learning foundations
            NLP
            Transformers and Attention
            LLMs
            Prompt Engineering
            LLM APIs
            Embeddings
            Vector Databases
            RAG
            LangChain
            AI Agents
            LangGraph
            Deployment
            Real-world GenAI projects

            Do not prioritize GAN, VAE or advanced research
            topics over practical LLM application development.

            Use simple English and beginner-friendly explanations.
            """

            with st.spinner("Creating your learning roadmap..."):

                roadmap = generate_response(prompt)

            st.session_state["learning_roadmap"] = roadmap

    # Display roadmap

    if "learning_roadmap" in st.session_state:

        st.subheader("Your Personalized Learning Roadmap")

        st.write(st.session_state["learning_roadmap"])

    st.divider()

    # --------------------------------
    # 2. RAG-powered AI Tutor with Memory
    # --------------------------------

    st.subheader("2. Ask Your AI Learning Mentor")

    st.info(
        "Ask questions about your study materials. "
        "Your AI mentor remembers your conversation."
    )

    # Initialize conversation history
    if "mentor_chat_history" not in st.session_state:
        st.session_state.mentor_chat_history = []

    # Display previous conversation
    for message in st.session_state.mentor_chat_history:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    question = st.chat_input(
        "Ask your learning question..."
    )

    if question:

        # Save user question
        st.session_state.mentor_chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):

            with st.spinner(
                "Searching your books and preparing an answer..."
            ):

                answer, sources = ask_learning_mentor(
                    question,
                    st.session_state.mentor_chat_history[:-1]
                )

            st.write(answer)

            st.caption("📖 Sources used:")

            for source in sources:
                st.write("📄", source)

        # Save AI answer
        st.session_state.mentor_chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    # Clear conversation button
    if st.button("🗑️ Clear Conversation"):

        st.session_state.mentor_chat_history = []

        st.rerun()
