
from utils.vector_store import load_vector_store
from utils.llm_helper import generate_response



def ask_learning_mentor(question, chat_history=None):

    
    # load vector store
    vector_store=load_vector_store()

    #retrieve relevant documents from vector store
    results = vector_store.similarity_search(
        question,
        k=3
    )

    # Step 3: Prepare PDF context
    context = ""
    sources = []

    for doc in results:

        context += doc.page_content + "\n\n"

        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "Unknown")

        sources.append(f"{source} - Page {page}")

    # Step 4: Prepare previous conversation
    conversation = ""

    if chat_history:

        for message in chat_history:

            conversation += (
                f"{message['role']}: "
                f"{message['content']}\n"
            )

    # Step 5: Create prompt
  
    prompt = f"""
    You are an expert AI Learning Mentor and a patient
    technical teacher.

    Your student is a beginner. Teach concepts in
    very simple English.

    Use the conversation history to understand
    follow-up questions.

    IMPORTANT:
    - Use ONLY the information in the PDF context
      for factual explanations.
    - Do not invent information.
    - If the answer is unavailable in the PDF context,
      clearly say so.
    - Use simple words and short sentences.

    Follow this teaching format:

    1. SIMPLE EXPLANATION
    Explain the concept as if teaching a beginner.

    2. REAL-LIFE ANALOGY
    Give an everyday example to make it easy to understand.

    3. TECHNICAL EXPLANATION
    Explain how the concept works internally.

    4. PRACTICAL EXAMPLE
    If relevant, provide a simple Python code example
    with its expected output.

    5. KEY TAKEAWAYS
    List 3 to 5 important points.

    6. MINI QUIZ
    Ask 2 simple questions to test understanding.
    Do not provide the answers immediately.

    Conversation History:
    {conversation}

    PDF Context:
    {context}

    Current Question:
    {question}
    """

    # Step 6: Generate answer using Qwen
    answer = generate_response(prompt)

    return answer, list(set(sources))
