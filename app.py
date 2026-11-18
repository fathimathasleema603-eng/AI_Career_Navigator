
import streamlit as st

from modules.resume_builder import resume_builder
from modules.resume_analyzer import resume_analyzer
from modules.skill_gap import skill_gap_analyzer
from modules.interview_coach import interview_coach
from modules.learning_mentor import learning_mentor


# =================================
# PAGE CONFIGURATION
# =================================

st.set_page_config(
    page_title="Career Navigator AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =================================
# CUSTOM CSS
# =================================

st.markdown("""
<style>

/* Main background */
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #FAFAF8 !important;
}

/* Dark Navy Sidebar */
[data-testid="stSidebar"] {
    background-color: #14243A !important;
    border-right: 1px solid #263B56;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Sidebar navigation spacing */
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 10px 12px;
    border-radius: 9px;
    margin-bottom: 5px;
}

/* Sidebar hover */
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background-color: #263B56 !important;
}

/* Sidebar dividers */
[data-testid="stSidebar"] hr {
    border-color: #40516A !important;
}
/* Main content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* Headings */
h1 {
    color: #24211C !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #3B3328 !important;
    font-weight: 700 !important;
}

/* Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E9DFC9 !important;
    border-radius: 16px !important;
    padding: 15px !important;
    box-shadow: 0 4px 15px rgba(40, 32, 20, 0.07) !important;
}

/* Buttons */
.stButton button {
    background-color: #C49A45 !important;
    color: #171717 !important;
    border-radius: 10px !important;
    border: none !important;
    font-weight: 700 !important;
}

.stButton button:hover {
    background-color: #A77D2E !important;
    color: #FFFFFF !important;
}

/* Dividers */
hr {
    border-color: #E5D9C2 !important;
}

/* Home page module card colours */

.module-card-1 {
    background-color: #E8EFFD !important;
}

.module-card-2 {
    background-color: #E5F4EF !important;
}

.module-card-3 {
    background-color: #FFF0D9 !important;
}

.module-card-4 {
    background-color: #F2E9FA !important;
}

.module-card-5 {
    background-color: #FCE8E8 !important;
}

</style>
""", unsafe_allow_html=True)

# =================================
# SIDEBAR NAVIGATION
# =================================

st.sidebar.title("🚀 Career Navigator")

st.sidebar.caption("YOUR AI CAREER COMPANION")

st.sidebar.divider()

st.sidebar.subheader("WORKSPACE")

selected_module = st.sidebar.radio(
    "Choose a module",
    [
        "🏠 Home",
        "📄 AI Resume Builder",
        "🔍 Resume Analyzer",
        "🎯 Skill Gap Analyzer",
        "💬 AI Interview Coach",
        "🎓 AI Learning Mentor"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

st.sidebar.caption("POWERED BY GENERATIVE AI")


# =================================
# HOME DASHBOARD
# =================================

if selected_module == "🏠 Home":

    # Welcome banner

    st.title("🚀 AI Career Navigator")

    st.subheader("Your Personal AI-Powered Career Assistant")

    st.write(
     "Build your resume, analyze your skills, "
     "prepare for interviews, and plan your career with AI."
   )

    st.divider()


    # Workspace heading

    st.header("Your Career Workspace")

    st.write(
        "Choose a tool to take the next step in your career journey."
    )

    st.write("")

    # =================================
    # COLOURED MODULE CARDS
    # =================================

    st.subheader("Explore Your Career Tools")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background:#E8EFFD; padding:20px;
        border-radius:15px; min-height:170px;">
            <h2>📄</h2>
            <h3 style="color:#263B65;">AI Resume Builder</h3>
            <p style="color:#334B78;">
            Create a professional ATS-friendly resume.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background:#E5F4EF; padding:20px;
        border-radius:15px; min-height:170px;">
            <h2>🔍</h2>
            <h3 style="color:#28634F;">Resume Analyzer</h3>
            <p style="color:#28634F;">
            Discover resume strengths and improvement areas.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background:#FFF0D9; padding:20px;
        border-radius:15px; min-height:170px;">
            <h2>🎯</h2>
            <h3 style="color:#81551A;">Skill Gap Analyzer</h3>
            <p style="color:#81551A;">
            Identify missing skills for your target career.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("""
        <div style="background:#F2E9FA; padding:20px;
        border-radius:15px; min-height:170px;">
            <h2>💬</h2>
            <h3 style="color:#68438A;">AI Interview Coach</h3>
            <p style="color:#68438A;">
            Practice interviews and improve your answers.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div style="background:#FCE8E8; padding:20px;
        border-radius:15px; min-height:170px;">
            <h2>🎓</h2>
            <h3 style="color:#914B4B;">AI Learning Mentor</h3>
            <p style="color:#914B4B;">
            Learn technical concepts with personalized AI guidance.
            </p>
        </div>
        """, unsafe_allow_html=True)


    # =================================
    # FOOTER MESSAGE
    # =================================

    st.divider()

    st.success("✨ Your career journey starts here!")


# =================================
# AI RESUME BUILDER
# =================================

elif selected_module == "📄 AI Resume Builder":

    resume_builder()


# =================================
# RESUME ANALYZER
# =================================

elif selected_module == "🔍 Resume Analyzer":

    resume_analyzer()


# =================================
# SKILL GAP ANALYZER
# =================================

elif selected_module == "🎯 Skill Gap Analyzer":

    skill_gap_analyzer()


# =================================
# AI INTERVIEW COACH
# =================================

elif selected_module == "💬 AI Interview Coach":

    interview_coach()


# =================================
# AI LEARNING MENTOR
# =================================

elif selected_module == "🎓 AI Learning Mentor":

    learning_mentor()


# =================================
# APPLICATION FOOTER
# =================================

st.divider()

st.caption(
    "CAREER NAVIGATOR AI | BUILT WITH GENERATIVE AI"
)
