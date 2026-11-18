
import streamlit as st
from io import BytesIO
from docx import Document
from utils.llm_helper import generate_response


def resume_builder():

    st.header("📄 AI Resume Builder")

    st.write(
        "Create a professional resume with the help of AI."
    )

    
        # Personal Information
    with st.container(border=True):

        st.subheader("👤 Personal Information")
        st.caption("Enter your basic contact details.")

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")

        with col2:
            phone = st.text_input("Phone Number")
            location = st.text_input("Location")

    # Career Information
    with st.container(border=True):

        st.subheader("🎓 Career Information")
        st.caption("Add your education and technical background.")

        education = st.text_area(
            "Education Details",
            placeholder="Example: B.E. Computer Science, Anna University, 2019",
            height=100
        )

        skills = st.text_area(
            "Technical Skills",
            placeholder="Example: Python, Machine Learning, Generative AI",
            height=100
        )

    # Projects
    with st.container(border=True):

        st.subheader("💻 Projects")
        st.caption("Describe the projects you have developed.")

        projects = st.text_area(
            "Project Details",
            placeholder="Enter project titles, technologies used and descriptions...",
            height=150
        )

    # Work Experience
    with st.container(border=True):

        st.subheader("💼 Work Experience")
        st.caption("Add your professional experience or internships, if applicable.")

        experience = st.text_area(
            "Experience Details",
            placeholder="Enter your work experience or internship details. Leave blank if you have none.",
            height=120
        )

    # Generate Resume
    if st.button("✨ Generate My Resume", type="primary", use_container_width=True):
        if not name or not education or not skills:

            st.warning(
                "Please enter your name, education and skills."
            )

        else:
            
            prompt = f"""
You are an expert professional resume writer, ATS resume specialist,
and technical recruiter specializing in Generative AI and software
development roles.

Your task is to create a professional, ATS-friendly resume using
ONLY the information provided by the candidate.

TARGET ROLE:
Generative AI Engineer

CANDIDATE INFORMATION:

Full Name: {name}
Email: {email}
Phone: {phone}
Location: {location}

EDUCATION:
{education}

TECHNICAL SKILLS:
{skills}

PROJECTS:
{projects}

WORK EXPERIENCE:
{experience}


==================================================
1. STRICT ACCURACY RULES
==================================================

1. Use only information explicitly provided by the candidate.
2. Never invent qualifications, employment history, internships,
   certifications, technologies, achievements or project results.
3. Never create fake percentages, performance metrics or numbers.
4. Do not describe academic or personal projects as professional
   industry experience.
5. Do not assume that a project uses a technology unless it is
   mentioned in the candidate's information.
6. Do not add unsupported claims such as:
   - Excellent communication skills
   - Strong team player
   - Improved accuracy
   - Increased efficiency
   - Successfully delivered business results
7. Do not repeat contact information.
8. Do not include empty sections.
9. Do not include references unless provided.
10. Do not add explanations before or after the resume.


==================================================
2. PROFESSIONAL SUMMARY
==================================================

Write a professional summary of approximately 50–75 words.

Requirements:

1. Position the candidate towards the Generative AI Engineer role.
2. Start with the candidate's educational or technical background.
3. Avoid generic openings such as:
   "Highly motivated professional"
   "Hardworking individual"
   "Technologically inclined professional"
   "Enthusiastic candidate"
4. Highlight relevant hands-on project experience.
5. Mention relevant technical skills naturally.
6. Highlight experience with LLM applications, RAG,
   Python and related technologies only when supported
   by the candidate's information.
7. Explain the type of AI applications the candidate has built.
8. Use confident, natural and professional language.
9. Do not exaggerate the candidate's experience.
10. Avoid simply listing every technical skill.


==================================================
3. TECHNICAL SKILLS
==================================================

Organize skills into relevant categories.

Possible categories include:

- Programming Languages
- Generative AI and LLM Technologies
- Machine Learning and Deep Learning
- NLP
- Frameworks and Libraries
- Vector Databases
- Tools and Platforms

Important:

1. Include only skills provided by the candidate.
2. Do not add technologies simply because they are popular.
3. Avoid unsupported soft skills.
4. Use correct technical spelling:
   Python, NumPy, Pandas, LangChain, ChromaDB,
   Streamlit, RAG, LLM.
5. Do not repeat the same skill in multiple categories.


==================================================
4. PROJECTS
==================================================

Projects are an important part of this candidate's resume.

For every project, use this structure:

PROJECT TITLE

Technologies Used:
Mention the actual technologies provided by the candidate.

Project Overview:
Explain what the application does in 2–3 sentences.

Key Technical Contributions:
Write 2–4 meaningful bullet points describing
the actual implementation and functionality.

Project writing requirements:

1. Start bullet points with suitable action verbs such as:
   Developed, Built, Implemented, Integrated,
   Designed, Created, Configured and Utilized.
2. Explain what the candidate actually implemented.
3. Highlight relevant technical concepts.
4. For RAG projects, mention document loading,
   text chunking, embeddings, vector storage,
   similarity search and LLM-based answer generation
   only when those features are implemented.
5. For LLM projects, describe the model and application
   functionality accurately.
6. For machine learning projects, mention preprocessing,
   feature extraction, model training and evaluation
   only when supported by the input.
7. Avoid generic statements such as:
   "Improved user experience."
   "Provided better performance."
   "Enhanced efficiency."
8. Never invent model accuracy or performance results.
9. Do not repeat identical bullet points across projects.
10. Keep descriptions concise, specific and technical.


==================================================
5. EDUCATION
==================================================

Present education in a clean professional format.

Include:
- Degree
- College or University
- Graduation year
- CGPA or percentage, if provided

Do not invent missing academic details.


==================================================
6. WORK EXPERIENCE
==================================================

Include this section only if actual work experience
or internship information is provided.

Requirements:

1. Mention the actual company and job title only
   when provided.
2. Include responsibilities only when provided.
3. Never create imaginary employment history.
4. Do not convert personal projects into work experience.
5. If no experience is provided, omit this section.


==================================================
7. CERTIFICATIONS
==================================================

Include certifications only when the candidate
provides certification details.

Never invent certification names or issuing organizations.


==================================================
8. ATS FORMATTING REQUIREMENTS
==================================================

1. Use standard resume section headings.
2. Use a professional and consistent writing style.
3. Use concise bullet points.
4. Avoid tables, graphics, icons and decorative symbols.
5. Avoid unnecessary personal details.
6. Avoid repeating contact information.
7. Use relevant keywords naturally without keyword stuffing.
8. Keep the resume easy for recruiters and ATS software to read.


==================================================
9. FINAL RESUME STRUCTURE
==================================================

Follow this order:

FULL NAME

Email | Phone | Location

PROFESSIONAL SUMMARY

TECHNICAL SKILLS

PROJECTS

EDUCATION

CERTIFICATIONS (only if provided)

WORK EXPERIENCE (only if provided)

ADDITIONAL INFORMATION (only if relevant and provided)


==================================================
10. FINAL QUALITY CHECK
==================================================

Before returning the resume, verify:

- Is the summary specific to Generative AI?
- Are the technical skills accurate?
- Are project descriptions technically meaningful?
- Are all claims supported by candidate information?
- Are there any invented achievements?
- Is contact information repeated?
- Are there empty or unnecessary sections?
- Is the language professional and concise?

Correct any issues before returning the final resume.

Return ONLY the completed resume using clear section headings
and properly formatted bullet points.
"""

            

            with st.spinner("AI is creating your resume..."):

                result = generate_response(prompt)

            st.divider()

            st.success("Your resume has been generated successfully!")

            st.subheader("📄 Resume Preview")

            with st.container(border=True):
             st.markdown(result)
            # Create Word document
            document = Document()

            document.add_heading("Professional Resume", 0)

            document.add_paragraph(result)

           # Save document in memory
            docx_file = BytesIO()

            document.save(docx_file)

            docx_file.seek(0)

           # Download button
            st.download_button(
            label="📥 Download Resume (Word)",
            data=docx_file,
            file_name="AI_Generated_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
      )


