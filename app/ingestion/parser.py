from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader
)

def parse_document(file_path):

    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    elif file_path.endswith(".md"):
        loader = UnstructuredMarkdownLoader(file_path)

    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path)

    else:
        return []

    documents = loader.load()

    return documents