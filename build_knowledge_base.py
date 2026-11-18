
from utils.document_loader import load_documents
from utils.text_splitter import split_documents
from utils.vector_store import create_vector_store


print("Loading PDF documents...")

documents = load_documents()

print("\nSplitting documents...")

chunks = split_documents(documents)

print("\nCreating vector database...")

vector_store = create_vector_store(chunks)

print("\nKnowledge base created successfully!")
