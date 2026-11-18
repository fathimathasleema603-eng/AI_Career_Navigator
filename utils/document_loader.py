
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents():

    documents = []

    folder_path = Path("knowledge_base")

    for file_path in folder_path.iterdir():

        if file_path.suffix.lower() == ".pdf":

            loader = PyPDFLoader(str(file_path))

            pdf_documents = loader.load()

            documents.extend(pdf_documents)

    print("Total pages loaded:", len(documents))

    return documents
