
import streamlit as st

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


@st.cache_resource
def load_vector_store():

    print("Loading ChromaDB and embedding model...")

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_store = Chroma(
        collection_name="genai_knowledge",
        embedding_function=embeddings,
        persist_directory="./vector_db"
    )

    print("Existing vector database loaded!")

    return vector_store


def create_vector_store(chunks):

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="genai_knowledge",
        persist_directory="./vector_db"
    )

    print("Vector database created successfully!")

    return vector_store
